class Node:
    print("CSE25139 P.B.V Preetham\n")
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def enqueue(self, item):
        newnode = Node(item)

        if self.rear is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

        print(item, "inserted into queue")

    # Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            item = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print(item, "deleted from queue")

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
        else:
            temp = self.front

            print("Queue:", end=" ")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


q = Queue()

while True:
    print("\n--- QUEUE MENU ---")
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
