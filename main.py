from collections import deque

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n -1):
            for j in range(0, n - i -1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i +1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) >1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            SortingAlgorithms.merge_sort(L)
            SortingAlgorithms.merge_sort(R)

            i = j = k =0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1

            while i < len(L):
                arr[k]=L[i]
                i+=1
                k+=1

            while j < len(R):
                arr[k]=R[j]
                j+=1
                k+=1
        return arr


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Yığın boş.")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Yığın boş.")

    def display(self):
        print("Yığın içeriği:", self.items)


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            print("Kuyruk boş.")

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Kuyruk boş.")

    def display(self):
        print("Kuyruk içeriği:", list(self.items))


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
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Bağlantılı Liste içeriği:", " -> ".join(map(str, elements)) + " -> None")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert_recursive(data, node.left)
        elif data > node.data:
            node.right = self._insert_recursive(data, node.right)
        else:
            # Aynı veriyi eklemeyin
            pass
        return node

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None:
            return None
        if data == node.data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)

def sorting_menu():
    try:
        arr = list(map(int, input("Sıralamak istediğiniz sayıları girin (boşlukla ayrılmış): ").split()))
        print("Sıralama algoritmasını seçin:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Merge Sort")
        choice = input("Seçiminiz: ")
        if choice == "1":
            SortingAlgorithms.bubble_sort(arr)
            print("Bubble Sort ile sıralanmış dizi:", arr)
        elif choice == "2":
            SortingAlgorithms.selection_sort(arr)
            print("Selection Sort ile sıralanmış dizi:", arr)
        elif choice == "3":
            SortingAlgorithms.merge_sort(arr)
            print("Merge Sort ile sıralanmış dizi:", arr)
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli sayılar girin.")

def stack_menu(stack):
    while True:
        print("\nYığın İşlemleri:")
        print("1. Push")
        print("2. Pop")
        print("3. Tepedeki Elemanı Göster")
        print("4. Yığını Göster")
        print("5. Geri Dön")
        choice = input("Seçiminiz: ")
        if choice == "1":
            element = input("Push edilecek elemanı girin: ")
            stack.push(element)
            print(f"{element} yığına eklendi.")
        elif choice == "2":
            element = stack.pop()
            if element is not None:
                print("Pop edilen eleman:", element)
        elif choice == "3":
            element = stack.peek()
            if element is not None:
                print("Tepedeki eleman:", element)
        elif choice == "4":
            stack.display()
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")

def queue_menu(queue):
    while True:
        print("\nKuyruk İşlemleri:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Öndeki Elemanı Göster")
        print("4. Kuyruğu Göster")
        print("5. Geri Dön")
        choice = input("Seçiminiz: ")
        if choice == "1":
            element = input("Enqueue edilecek elemanı girin: ")
            queue.enqueue(element)
            print(f"{element} kuyruğa eklendi.")
        elif choice == "2":
            element = queue.dequeue()
            if element is not None:
                print("Dequeue edilen eleman:", element)
        elif choice == "3":
            element = queue.front()
            if element is not None:
                print("Öndeki eleman:", element)
        elif choice == "4":
            queue.display()
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")

def linked_list_menu(linked_list):
    while True:
        print("\nBağlantılı Liste İşlemleri:")
        print("1. Append")
        print("2. Listeyi Göster")
        print("3. Geri Dön")
        choice = input("Seçiminiz: ")
        if choice == "1":
            data = input("Eklenecek veriyi girin: ")
            linked_list.append(data)
            print(f"{data} listeye eklendi.")
        elif choice == "2":
            linked_list.display()
        elif choice == "3":
            break
        else:
            print("Geçersiz seçim.")

def bst_menu(bst):
    while True:
        print("\nİkili Arama Ağacı İşlemleri:")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder Traversal")
        print("4. Geri Dön")
        choice = input("Seçiminiz: ")
        if choice == "1":
            try:
                data = int(input("Eklenecek veriyi girin: "))
                bst.insert(data)
                print(f"{data} ağaca eklendi.")
            except ValueError:
                print("Lütfen bir tam sayı girin.")
        elif choice == "2":
            try:
                data = int(input("Aranacak veriyi girin: "))
                result = bst.search(data)
                if result:
                    print(f"{data} ağaçta bulundu.")
                else:
                    print(f"{data} ağaçta bulunamadı.")
            except ValueError:
                print("Lütfen bir tam sayı girin.")
        elif choice == "3":
            elements = bst.inorder_traversal()
            print("Ağacın Inorder Traversal'ı:", elements)
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim.")

def main():
    print("Veri Yapıları ve Algoritmalar ")
    stack = Stack()
    queue = Queue()
    linked_list = LinkedList()
    bst = BinarySearchTree()

    while True:
        print("\nBir seçenek seçin:")
        print("1. Sıralama Algoritmaları")
        print("2. Yığın İşlemleri")
        print("3. Kuyruk İşlemleri")
        print("4. Bağlantılı Liste İşlemleri")
        print("5. İkili Arama Ağacı İşlemleri")
        print("6. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            sorting_menu()

        elif choice == "2":
            stack_menu(stack)

        elif choice == "3":
            queue_menu(queue)

        elif choice == "4":
            linked_list_menu(linked_list)

        elif choice == "5":
            bst_menu(bst)

        elif choice == "6":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
