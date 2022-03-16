nested_list_modified = [
    'a', 'b', 'c',[222,333],
	['d', 'e', 'f', 'h', False,[444,[555,[666,[777,888]]]]],
	[1, 2, None]
]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


def flat_generator_recursive(list_):
    for li in list_:
        if isinstance(li, list):
            yield from flat_generator_recursive(li)
        else:
            yield li


def flat_generator(list_):
    i = 0
    j = 0
    while i < len(list_):
        while j < len(list_[i]):
            yield list_[i][j]
            j += 1
        j = 0
        i += 1


class FlatIterator:
    def __init__(self, list_):
       self.hw_list = list_

    def __iter__(self):
        self.list_index = 0
        self.elem_index = 0
        return self

    def __next__(self):
        if self.list_index >= len(self.hw_list):
            raise StopIteration

        res = self.hw_list[self.list_index][self.elem_index]

        if self.elem_index < len(self.hw_list[self.list_index])-1:
            self.elem_index += 1
        else:
            self.elem_index = 0
            self.list_index += 1
        return res


class FlatIteratorRecursive:
    def __init__(self, list_):
        self.res_list = list()
        self.follow_list(list_)
        self.list_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_index >= len(self.res_list):
            raise StopIteration

        res = self.res_list[self.list_index]
        self.list_index += 1
        return res

    def follow_list(self,list_):
        i = 0
        while i < len(list_):
            if isinstance(list_[i], list):
                self.follow_list(list_[i])
            else:
                self.res_list.append(list_[i])
            i += 1

def Task1():
    #ЗАДАЧА 1
    print('=-' * 5 + 'Результат задачи 1' + '=-' * 10)
    for item in FlatIterator(nested_list):
        print(item)
    print('Комперхеншн:')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-'*30)
    print()


def Task2():
    #ЗАДАЧА 2
    print('=-' * 5 + 'Результат задачи 2' + '=-' * 10)
    for item in flat_generator(nested_list):
        print(item)
    print('-'*30)
    print()


def Task3():
    #ЗАДАЧА 3
    print('=-' * 5 + 'Результат задачи 3' + '=-' * 10)
    for item in FlatIteratorRecursive(nested_list_modified):
        print(item)
    print('Комперхеншн:')
    flat_list = [item for item in FlatIteratorRecursive(nested_list_modified)]
    print(flat_list)
    print('-'*30)
    print()


def Task4():
    #ЗАДАЧА 4
    print('=-' * 5 + 'Результат задачи 4' + '=-' * 10)
    for item in flat_generator_recursive(nested_list_modified):
        print(item)
    print('-'*30)
    print()

c = ''
while c!='x':
    print("Домашняя работа по теме"+" Iterators. Generators. Yield")
    for i in range(1,5):
        print(f"Задача {i}: {i}")
    c = input("Введите номер задачи (x для выхода):")
    if c == '1':
        Task1()
    elif c == '2':
        Task2()
    elif c == '3':
        Task3()
    elif c == '4':
        Task4()
    elif c =='x' or c == 'х':
        c = 'x'
