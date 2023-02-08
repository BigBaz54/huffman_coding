

class HuffmanTree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return self.root.__str__()


    def update(self, char):
        # re arrange tree when reading new char
        pass

    def get_depth(self):
        return self.root.get_depth_aux()

    def get_node(self, char):
        return self.root.get_node_aux(char)

    def get_code(self, char):
        return self.root.get_code_aux(char)
    
    def get_frequency(self, char):
        return self.get_node(char).frequency


class HuffmanNode:
    node_id = 0

    # to be able to use PriorityQueue and have a minimal variance in Huffman code
    def __lt__(self, other):
        if self.char is None:
            return False

    def __init__(self, left, right, char, frequency):
        self.id = HuffmanNode.node_id
        HuffmanNode.node_id += 1
        self.left = left
        self.right = right
        self.char = char
        self.frequency = frequency

    def __str__(self, depth=0):
        s = f"\"{self.char}\" : {str(self.frequency)}\n"
        if self.left is not None:
            s += f"\t"*(depth+1)+f"{self.left.__str__(depth=depth+1)}"
        if self.right is not None:
            s += f"\t"*(depth+1)+f"{self.right.__str__(depth=depth+1)}"
        return s

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_depth_aux(self):
        if self.is_leaf():
            return 0
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.get_depth_aux(), self.right.get_depth_aux())
        if self.left is not None:
            return 1 + self.left.get_depth_aux()
        if self.right is not None:
            return 1 + self.right.get_depth_aux()

    def get_node_aux(self, char):
        if self.is_leaf() and self.char == char:
            return self
        if self.left is not None:
            l = self.left.get_node_aux(char)
            if l is not None:
                return l
        if self.right is not None:
            r = self.right.get_node_aux(char)
            if r is not None:
                return r
        return None
    
    def get_code_aux(self, char):
        if self.is_leaf() and self.char == char:
            return ""
        if self.left is not None:
            l = self.left.get_code_aux(char)
            if l is not None:
                return "0" + l
        if self.right is not None:
            r = self.right.get_code_aux(char)
            if r is not None:
                return "1" + r
        return None



if __name__ == "__main__":
    e1 = HuffmanNode(None, None, 'a', 1)
    e2 = HuffmanNode(None, None, 'b', 1)
    e3 = HuffmanNode(None, None, 'c', 1)
    e4 = HuffmanNode(None, None, 'd', 1)
    i1 = HuffmanNode(None, None, None, 1)
    i2 = HuffmanNode(None, None, None, 2)
    i3 = HuffmanNode(None, None, None, 3)
    i1.left = e1
    i1.right = i2
    i2.left = e2
    i2.right = i3
    i3.left = e3
    i3.right = e4
    tree = HuffmanTree(i1)
    print(tree)
    print((tree.get_code('a')))
    print((tree.get_code('b')))
    print((tree.get_code('c')))
    print((tree.get_code('d')))
