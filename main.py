# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять
#  следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека,
#  которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки,
#  на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить
#  несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате
# passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень
# полок, спросив его номер, тип, имя владельца и номер полки, на котором он
#  будет храниться.
#  Корректно обработайте ситуацию, когда пользователь будет пытаться добавить
#  документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
#  Функции должны иметь выразительное название, передающие её действие.
# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит его из
# каталога и из перечня полок.
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и
# переместит его с текущей полки
# на целевую. Корректно обработайте кейсы, когда пользователь пытается
# переместить несуществующий документ или переместить документ на
# несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит
# ее в перечень. Предусмотрите случай, когда пользователь добавляет полку,
#  которая уже существует.;

import sys
import pytest
import unittest

HELP = '''Список доступных команд:
* p – people – команда, которая спросит номер документа и выведет\
   имя человека, которому он принадлежит;
* s – shelf – команда, которая спросит номер документа и выведет\
   номер полки, на которой он находится;
* l – list – команда, которая выведет список всех документов;
* a – add – команда, которая добавит новый документ в каталог\
   и в перечень полок;
* d – delete – команда, которая спросит номер документа и удалит\
   его из каталога и из перечня полок;
* m – move – команда, которая спросит номер документа и целевую полку\
   и переместит его с текущей полки на целевую;
* as – add shelf – команда, которая спросит номер новой полки и добавит\
   ее в перечень;
* h - вызов справки
* q - выход из программы
'''


documents = [{"type": "passport", "number": "2207 876234",
              "name": "Василий Гупкин"
              },
             {"type": "invoice", "number": "11-2",
              "name": "Геннадий Покемонов"
              },
             {"type": "insurance", "number": "10006",
              "name": "Аристарх Павлов"
              }
             ]

directories = {'1': ['2207 876234', '11-2'],
               '2': ['10006'],
               '3': []
               }


# ID - list index
def get_id(doc_base, doc_num):
    for id, doc in enumerate(doc_base):
        if doc["number"] == doc_num:
            return id
    return None


# name return
def get_person(doc_base, doc_num):
    id = get_id(doc_base, doc_num)
    return (f"Документ {doc_num} зарегестрирован на имя"
            f"{doc_base[id]['name']}"
            ) if id is not None else f"Документ с номером {doc_num} не найден"


# dir - key in directories
def get_dir(shelf_base, doc_num):
    for key, values in shelf_base.items():
        if doc_num in values:
            return key
    return None


# shelf return
def get_shelf(shelf_base, doc_num):
    shelf_num = get_dir(shelf_base, doc_num)
    return (f"Документ находится на полке - "
            f"{shelf_num}"
            ) if shelf_num is not None else (f"Документ с номером {doc_num}"
                                             f" на полках не найден"
                                             )


# doc to shelf
def add_num_to_dir(dir_base, dir, doc_num):
    dir_base[dir].append(doc_num)


# add new doc in base
def add_doc(doc_base, dir_base, type_doc, doc_num, name_doc, shelf_num):
    if shelf_num in dir_base:
        doc_base.append({"type":  type_doc,
                         "number": doc_num,
                         "name": name_doc
                         }
                        )
        add_num_to_dir(dir_base, shelf_num, doc_num)
        return (f"Добавлен новый документ {doc_num},"
                f"он будет находится на полке {shelf_num}"
                )
    else:
        return f"Полка, с указанным вами номером {shelf_num} не найдена"


# remove from shelf
def remove_num_from_shelf(dir_base, doc_num, dir=None):
    if dir is not None:
        dir_base[dir].remove(doc_num)
    else:
        dir_base[get_dir(dir_base, doc_num)].remove(doc_num)


# remove from base
def remove_doc(doc_base, dir_base, doc_num):
    id = get_id(doc_base, doc_num)
    if id is None:
        return f"Документ с номером {doc_num} не найден"

    dir = get_dir(dir_base, doc_num)
    if dir is None:
        return f"Документ с номером {doc_num} не найден на полках"

    doc_base.pop(id)
    remove_num_from_shelf(dir_base, doc_num, dir)
    return f"Документ с номером {doc_num} удалён"


# checking shelf existence
def shelf_check(dir_base, num_shelf):
    return True if num_shelf in dir_base else False


# move docs from shelf to new shelf
def move(dir_base, doc_num, shelf_num):
    dir = get_dir(dir_base, doc_num)
    if dir == shelf_num:
        return (f"Документ с номером {doc_num}"
                f" уже находится на полке {shelf_num}"
                )
    elif dir is None:
        return f"Документ с номером {doc_num} не найден на полках"
    if shelf_check(dir_base, shelf_num) is True:
        remove_num_from_shelf(dir_base, doc_num, dir)
        add_num_to_dir(dir_base, shelf_num, doc_num)
        return f"Документ с номером {doc_num} перемещён на полку {shelf_num}"
    return f"Вы указали несуществующую полку {shelf_num}"


# add new shelf
def add_shelf(dir_base, shelf_num):
    if shelf_check(dir_base, shelf_num) is False:
        dir_base[shelf_num] = []
        return f"Добавлена новая полка, ей присвоен номер {shelf_num}"
    return (f"Полка не была добавлена, поскольку"
            f" полка с номером {shelf_num} уже существует")


def main():
    print(HELP)
    while True:
        cmd = input("Введите команду: ")
        selector(cmd)


# numeric input
def enter_num(purpose=False):
    while True:
        num = input((f"Введите номер"
                     f" {'документа' if purpose is True else 'полки'}: "))
        if num:
            break
        else:
            print("Номер не может быть пустым")
    return num


# alphabetic input
def enter_text(purpose=False):
    while True:
        text = input((f"Введите "
                      f"{'тип' if purpose is True else 'имя пользователя'}"
                      f" документа "
                      )
                    )
        if text:
            if not text.isdigit():
                break
            else:
                print((f"{'Тип должен' if purpose is True else 'Имя пользователя должно'}"
                       f" стостоять из букв алфавита, вы ввели"
                       f" цифровой номер {text}")
                      )
        else:
            print((f"{'Тип' if purpose is True else 'Имя пользователя'}"
                   f" не может быть пустым"))
    return text


# switc-case constructions
def case_get_person():
    print(get_person(documents, enter_num(True)))


def case_get_shelf():
    print(get_shelf(directories, enter_num(True)))


def case_get_print(doc_base=documents):
    for entry in doc_base:
        print(f'{entry["type"]} "{entry["number"]}" "{entry["name"]}"')


def case_add_doc():
    print(add_doc(documents, directories, enter_text(True),
                  enter_num(True), enter_text(), enter_num()))


def case_remove_doc():
    print(remove_doc(documents, directories, enter_num(True)))


def case_move():
    print(move(directories, enter_num(True), enter_num()))


def case_add_shelf():
    print(add_shelf(directories, enter_num()))


def case_help():
    print(HELP)


def case_quit():
    sys.exit()


def selector(cmd):
    switcher = {
      "p": case_get_person,
      "s": case_get_shelf,
      "l": case_get_print,
      "a": case_add_doc,
      "d": case_remove_doc,
      "m": case_move,
      "as": case_add_shelf,
      "h": case_help,
      "q": case_quit
    }
    out = switcher.get(cmd, lambda: print("Неверная команда введена была"))
    return out()


def assert_test():
    assert get_person(documents, "2207 876234") == "Документ 2207 876234 зарегестрирован на имя Василий Гупкин"


class AddTests(unittest.TestCase):
    # def assert_test(self):
    #     assert  6 == get_person(documents, "2207 876234") #== "Документ 2207 876234 зарегестрирован на имя Василий Гупкин"
    def test_vvv(self):
        self.assertEqual(3, 2+1)

    def test_bbb(self):
        self.assertEqual(0, 2+1)




if __name__ == '__main__':
    # main()
    # assert_test()
    test = AddTests()
    test.test_vvv()
    # print(get_person(documents, "2207 876234"))


# documents = [{"type": "passport", "number": "2207 876234",
#               "name": "Василий Гупкин"
#               },
#              {"type": "invoice", "number": "11-2",
#               "name": "Геннадий Покемонов"
#               },
#              {"type": "insurance", "number": "10006",
#               "name": "Аристарх Павлов"
#               }
#              ]