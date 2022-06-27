
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
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


class FlatIteratorTask3:

    def __init__(self, your_list: list):
        self.your_list = your_list
        self.my_list_iterator = iter(self.your_list)

    def __iter__(self):
        FlatIteratorTask3.list_redactor(self)
        return self

    def __next__(self):
        list_object = next(self.my_list_iterator)
        return list_object

    def list_redactor(self):
        list_in_list = []
        while type(list_in_list) == list:
            list_range = len(self.your_list)
            for num, obg in enumerate(self.your_list):
                if type(obg) is list:
                    for obg2 in obg:
                        self.your_list.append(obg2)
                else:
                    self.your_list.append(obg)
                if num == list_range - 1:
                    break
            i = 0
            while i < list_range:
                del(self.your_list[0])
                i += 1
            for obg in self.your_list:
                if type(obg) == list:
                    list_in_list = []
                    break
                else:
                    list_in_list = 0
        return self.your_list


def flat_generatortask4(your_list):
    list_in_list = []
    while type(list_in_list) == list:
        list_range = len(your_list)
        for num, obg in enumerate(your_list):
            if type(obg) is list:
                for obg2 in obg:
                    your_list.append(obg2)
                    yield obg2
            else:
                your_list.append(obg)
                yield obg
            if num == list_range - 1:
                break
        i = 0
        while i < list_range:
            del (your_list[0])
            i += 1
        for obg in your_list:
            if type(obg) == list:
                list_in_list = []
                break
            else:
                list_in_list = 0
        

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print('-' * 50)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-' * 50)

    for item in flat_generator(nested_list):
        print(item)
    print('-' * 50)

    for item in FlatIteratorTask3(nested_list):
        print(item)
    print('-' * 50)

    for item in flat_generatortask4(nested_list):
        print(item)
