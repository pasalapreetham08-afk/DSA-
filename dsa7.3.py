class Node:
    print("CSE25139 P.B.V Preetham")
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def enqueue(self, item):
        newnode = Node(item)

        if self.front is None:
            self.front = newnode
            self.rear = newnode
            newnode.next = self.front
        else:
            newnode.next = self.front
            self.rear.next = newnode
            self.rear = newnode

        print(item, "inserted")

    # Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        item = self.front.data
        print(item, "deleted")

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    # Peek
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # Display
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        print("Queue:", end=" ")

        while True:
            print(temp.data, end=" ")

            if temp == self.rear:
                break

            temp = temp.next

        print()


q = CircularQueue()

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
