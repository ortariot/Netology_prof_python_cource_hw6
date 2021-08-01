from shelf_case import get_person, get_shelf, add_doc,\
                       remove_doc, move, add_shelf, get_dir,\
                       documents, directories

from unittest import TestCase
from unittest.mock import patch


class ShelfTests(TestCase):

    def test_get_person(self):
        out = 'документ 2207 876234 зарегестрирован на имя Василий Гупкин'
        self.assertEqual(get_person(documents, '2207 876234'), out)

    def test_get_shelf(self):
        out = 'документ находится на полке - 1'
        out_f = 'документ с номером А888АА 777 на полках не найден'
        self.assertEqual(get_shelf(directories, '2207 876234'), out)
        self.assertEqual(get_shelf(directories, 'А888АА 777'), out_f)

    def test_add_doc(self):
        out_ok1 = ('Добавлен новый документ 1208-315678,'
                   ' он будет находится на полке 1')
        out_ok2 = 'документ 1208-315678 зарегестрирован на имя Сергей Серёгин'
        out_f = 'Полка, с указанным вами номером 345 не найдена'
        self.assertEqual(add_doc(documents, directories, 'diplom',
                         '1208-315678', 'Сергей Серёгин', '1'), out_ok1)
        self.assertEqual(get_person(documents, '1208-315678'), out_ok2)
        self.assertIn('1208-315678', directories['1'])
        self.assertEqual(add_doc(documents, directories, 'diplom',
                         '1208-315678', 'Сергей Серёгин', '345'), out_f)

    def test_remove_doc(self):
        out = 'документ с номером 10006 удалён'
        out_f = 'документ с номером 10006 не найден'
        self.assertEqual(remove_doc(documents, directories, "10006"), out)
        self.assertEqual(get_person(documents, '10006'), out_f)
        self.assertEqual(get_dir(directories, '10006'), None)

    def test_move(self):
        out = 'документ с номером 2207 876234 перемещён на полку 3'
        out_f1 = 'документ с номером 10006 уже находится на полке 2'
        out_f2 = 'документ с номером 7861221 не найден на полках'
        out_f3 = 'Вы указали несуществующую полку 987'
        self.assertEqual(move(directories, '2207 876234', '3'), out)
        self.assertEqual(move(directories, '10006', '2'), out_f1)
        self.assertEqual(move(directories, '7861221', '2'), out_f2)
        self.assertEqual(move(directories, '10006', '987'), out_f3)
        self.assertIn('2207 876234', directories['3'])

    def test_add_shelf(self):
        out_ok = 'Добавлена новая полка, ей присвоен номер 4'
        out_fail = ('Полка не была добавлена, поскольку полка'
                    ' с номером 1 уже существует'
                    )
        self.assertEqual(add_shelf(directories, '4'), out_ok)
        self.assertEqual(add_shelf(directories, '1'), out_fail)
        self.assertIn('4', directories)

    @patch('shelf_case.selector',
           return_value=get_person(documents, '2207 876234'))
    def test_selector_shelf(self, selector):
        out = 'документ 2207 876234 зарегестрирован на имя Василий Гупкин'
        self.assertEqual(selector('p'), out)
