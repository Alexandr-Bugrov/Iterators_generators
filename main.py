import itertools

nested_list = [
    ['a', 'b', 'c'],
    [['d', 'e'], ['f', 'h', False]],
    [1, 2, None,],
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



class FlatIteratorTest:

    def __init__(self, your_list: list):
        self.your_list = your_list
        self.list_range = len(self.your_list)
        self.my_list_iterator = iter(self.your_list)

    def __iter__(self):
        self.myitem = []
        self.myitem2 = 0
        return self

    def __next__(self):
        # if type(self.your_list[self.elem_num]) == list:
        #     list_range = len(self.your_list[self.elem_num])
        #     my_list_iterator = iter(self.your_list[self.elem_num])
        #     item = next(my_list_iterator)
        #     if type(item) == list:
        # if type(self.myitem) == list:

        self.myitem = next(self.my_list_iterator)
        if type(self.myitem) == list:
            index = self.your_list.index(self.myitem)
            self.your_list.insert(index)
            del(self.your_list[index+1])

def list_redactor(your_list):
    list_in_list = []
    while type(list_in_list) == list:
        a = len(your_list)
        for num, obg in enumerate(your_list):
            if type(obg) is list:
                for obg2 in obg:
                    your_list.append(obg2)
            else:
                your_list.append(obg)
            if num == a - 1:
                break
        i = 0
        while i < a:
            del(your_list[0])
            i += 1
        for obg in your_list:
            if type(obg) == list:
                list_in_list = []
                break
            else:
                list_in_list = 0
    return your_list









if __name__ == '__main__':
    # for item in FlatIterator(nested_list):
    #     print(item)
    #
    # flat_list = [item for item in FlatIterator(nested_list)]
    # print(flat_list)
    #
    # for item in flat_generator(nested_list):
    #     print(item)
    print(list_redactor(nested_list))
