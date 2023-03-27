from huffman_tree import *
from code_characteristics import *
from queue import PriorityQueue

def read(file):
    freq = {}
    with open(file, "r", encoding="utf-8") as f:
        char = f.read(1)
        while char:
            if char in freq.keys():
                freq[char] += 1
            else:
                freq[char] = 1
            char = f.read(1)
    return freq

def build_tree(freq):
    q_leaves = PriorityQueue()
    q_internal = PriorityQueue()
    for char in freq.keys():
        q_leaves.put((freq[char], HuffmanNode(None, None, char, freq[char])))
    while q_leaves.qsize() + q_internal.qsize() > 1:
        if q_leaves.qsize() == 0:
            left = q_internal.get()[1]
            right = q_internal.get()[1]
        elif q_internal.qsize() == 0:
            left = q_leaves.get()[1]
            right = q_leaves.get()[1]
        else:
            l1 = q_leaves.get()
            i1 = q_internal.get()
            if l1[0] <= i1[0]:
                left = l1[1]
                if q_leaves.qsize() == 0:
                    right = q_internal.get()[1]
                    q_internal.put(i1)
                else:
                    l2 = q_leaves.get()
                    if l2[0] <= i1[0]:
                        right = l2[1]
                        q_internal.put(i1)
                    else:
                        right = i1[1]
                        q_leaves.put(l2)
            else:
                left = i1[1]
                if q_internal.qsize == 0:
                    right = q_leaves.get()[1]
                    q_leaves.put(l1)
                else:
                    i2 = q_internal.get()
                    if l1[0] <= i2[0]:
                        right = l1[1]
                        q_internal.put(i2)
                    else:
                        right = i2[1]
                        q_leaves.put(l1)
        q_internal.put((left.frequency + right.frequency, HuffmanNode(left, right, None, left.frequency + right.frequency)))
    return HuffmanTree(q_internal.get()[1])


if __name__ == "__main__":
    freq = read("msg.txt")
    tree = build_tree(freq)
    print("\n\n", tree)

    myCode = tree.get_code()
    print(myCode)
    print(is_prefix(tree.get_code()))
    print(get_average_bit_length(tree.get_code(), freq))
    print(get_variance(tree.get_code(), freq))

    dcode = {' ': '00', 'y': '111', 'r': '100', 'g': '1100', 't': '11010', 'v': '11011', 'a': '101', 'f': '0100', 'ç': '0101', 'z': '011'}
    print(is_prefix(dcode))
    print(get_average_bit_length(dcode, freq))
    print(get_variance(dcode, freq))
