import hashlib


# Hàm băm để tính ID của node hoặc key
def hash_function(key, max_id=16):
    return int(hashlib.sha1(key.encode()).hexdigest(), 16) % max_id


# Lớp Node biểu diễn các node trong hệ thống Chord
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.successor = None  # Node kế tiếp trong vòng

    def find_successor(self, key_id):
        """
        Tìm successor của key dựa trên vòng băm.
        """
        if self.successor is None or self.node_id == key_id:
            return self
        if self.node_id < key_id <= self.successor.node_id:
            return self.successor
        return self.successor.find_successor(key_id)


# Tạo vòng băm Chord
def create_chord_ring(nodes):
    nodes = sorted(nodes, key=lambda n: n.node_id)  # Sắp xếp node theo ID
    for i in range(len(nodes)):
        nodes[i].successor = nodes[(i + 1) % len(nodes)]  # Liên kết vòng
    return nodes


# Minh họa thuật toán
if __name__ == "__main__":
    # Tạo các node với ID cụ thể
    node_ids = [1, 4, 8, 12, 15]
    nodes = [Node(node_id) for node_id in node_ids]

    # Tạo vòng băm
    chord_ring = create_chord_ring(nodes)

    # Key cần ánh xạ
    key = "my_key"
    key_id = hash_function(key)

    # Tìm successor của key trong vòng băm
    successor_node = chord_ring[0].find_successor(key_id)

    # In kết quả
    print(f"Key '{key}' với ID {key_id} được ánh xạ tới Node {successor_node.node_id}")
