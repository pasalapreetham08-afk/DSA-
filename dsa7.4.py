class Queue:
    def __init__(self):
        print("CSE25139 P.B.V Preetham\n")
        self.queue = []

    # Enqueue
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted into queue")

    # Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            item = self.queue.pop(0)
            print(item, "deleted from queue")

    # Peek
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)


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
