nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, your_list: list):
        self.your_list = your_list
        self.list_range = len(self.your_list)

    def __iter__(self):
        self.elem_num = 0
        self.item_num = 0 - 1
        return self

    def __next__(self):
        if self.item_num == len(self.your_list[self.elem_num]) - 1:
            self.elem_num += 1
            self.item_num = 0 - 1
        self.item_num += 1
        if self.elem_num == self.list_range:
            raise StopIteration
        return self.your_list[self.elem_num][self.item_num]


def flat_generator(your_list, elem_num=0, item_num=0 - 1):
    list_range = len(your_list)
    while elem_num <= list_range - 1:
        item_num += 1
        yield your_list[elem_num][item_num]
        if item_num == len(your_list[elem_num]) - 1:
            elem_num += 1
            item_num = 0 - 1


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
