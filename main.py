from collections import deque

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        if not self.is_empty():
            return self.items[0]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        return self._search_recursive(data, node.right)


def main():
    print("Data Structures and Algorithms Demo")
    while True:
        print("\nSelect an option:")
        print("1. Sort an Array (Bubble Sort)")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Linked List Operations")
        print("5. Binary Search Tree Operations")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
            print("Bubble Sort Result:", SortingAlgorithms.bubble_sort(arr))

        elif choice == "2":
            stack = Stack()
            while True:
                stack_choice = input("\n1. Push\n2. Pop\n3. Display Top\n4. Back\nEnter choice: ")
                if stack_choice == "1":
                    element = input("Enter element to push: ")
                    stack.push(element)
                    print(f"{element} pushed to stack.")
                elif stack_choice == "2":
                    print("Popped element:", stack.pop())
                elif stack_choice == "3":
                    print("Top element:", stack.peek())
                elif stack_choice == "4":
                    break

        elif choice == "3":
            queue = Queue()
            while True:
                queue_choice = input("\n1. Enqueue\n2. Dequeue\n3. Display Front\n4. Back\nEnter choice: ")
                if queue_choice == "1":
                    element = input("Enter element to enqueue: ")
                    queue.enqueue(element)
                    print(f"{element} added to queue.")
                elif queue_choice == "2":
                    print("Dequeued element:", queue.dequeue())
                elif queue_choice == "3":
                    print("Front element:", queue.front())
                elif queue_choice == "4":
                    break

        elif choice == "4":
            linked_list = LinkedList()
            while True:
                list_choice = input("\n1. Append\n2. Display\n3. Back\nEnter choice: ")
                if list_choice == "1":
                    data = input("Enter data to append: ")
                    linked_list.append(data)
                elif list_choice == "2":
                    linked_list.display()
                elif list_choice == "3":
                    break

        elif choice == "5":
            bst = BinarySearchTree()
            while True:
                bst_choice = input("\n1. Insert\n2. Search\n3. Back\nEnter choice: ")
                if bst_choice == "1":
                    data = int(input("Enter data to insert: "))
                    bst.insert(data)
                    print(f"{data} inserted.")
                elif bst_choice == "2":
                    data = int(input("Enter data to search: "))
                    result = bst.search(data)
                    if result:
                        print(f"{data} found in the tree.")
                    else:
                        print(f"{data} not found.")
                elif bst_choice == "3":
                    break

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
