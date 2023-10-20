from Node import Node

class Queue():
    def __init__(self) -> None:
        self._queue = []
    
    def enqueue(self, new_node: Node):
        self._queue.append(new_node)
    
    def dequeue(self):
        self._queue.pop(0)
    
    def __str__(self) -> str:
        for node in self._queue:
            print(f"Id: {node.get_id()}     Value: {node.get_value()}")
        return "Done"
    