class Tree():

    def __init__(self):
        self.children = []
        self.metadata = []

entries = [int(i) for i in open('Day8input.txt', 'r').read().strip().split()]

def get_meta(current_kids):

    my_tree = Tree()
    num_children = current_kids[0]
    num_meta = current_kids[1]

    if num_children == 0:
        my_tree.metadata = current_kids[2: 2 + num_meta]
        my_tree.children = []
        remaining = current_kids[2 + num_meta:]
        return my_tree, remaining
    else:
        remaining = current_kids[2:]
        for i in range(num_children):
            child, remaining = get_meta(remaining)
            my_tree.children.append(child)
        my_tree.metadata = remaining[:num_meta]
        return my_tree, remaining[num_meta:]

def add_meta(my_tree):
    if len(my_tree.children) == 0:
        return sum(my_tree.metadata)
    else:
        total = 0
        for child in my_tree.children:
            total += add_meta(child)
        return total + sum(my_tree.metadata)

complete_tree = get_meta(entries)[0]

print(add_meta(complete_tree))

# TASK 2 ################

def get_values(my_tree):
    if len(my_tree.children) == 0:
        return sum(my_tree.metadata)
    else:
        total = 0
        for data in my_tree.metadata:
            if data <= len(my_tree.children):
                total += get_values(my_tree.children[data - 1])
        return total

print(get_values(complete_tree))

