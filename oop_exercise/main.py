from Car import Car
from Queue import Queue
from Node import Node

def main():
    # kia_k5 = Car("Kia", "K5", 2020, 10000, "Gray")
    # kia_k5.start_car()
    # kia_k5.stop_car()
    # print(kia_k5)
    queue = Queue()
    
    node_1 = Node(0, 5.36)
    node_2 = Node(1, 9.36)
    node_3 = Node(2, -65.2)

    queue.enqueue(node_1)
    queue.enqueue(node_2)
    queue.enqueue(node_3)
    
    print(queue)
    
    queue.dequeue()
    print(queue)

if __name__ == "__main__":
    main()