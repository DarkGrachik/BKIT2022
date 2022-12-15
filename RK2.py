import unittest
from BKIT_RK1 import *

class test_rk(unittest.TestCase):
    def set(self):
        self.Streets = [
    Street(1, 'Новый Арбат'),
    Street(2, 'Тверская'),
    Street(3, 'Воздвиженка'),
 
    Street(11, 'Старый Арбат'),
    Street(22, 'Волхонка'),
    Street(33, 'Большая Никитская'),
    ]
        self.Houses = [
    House(1, 3, 64, 1),
    House(2, 4, 120, 2),
    House(3, 25, 40, 3),
    House(4, 24, 50, 3),
    House(5, 10, 100, 3),
    ]
        self.Houses_Streets = [
    HouseStreet(1,1),
    HouseStreet(2,2),
    HouseStreet(3,3),
    HouseStreet(3,4),
    HouseStreet(3,5),
 
    HouseStreet(11,1),
    HouseStreet(22,2),
    HouseStreet(33,3),
    HouseStreet(22,4),
    HouseStreet(33,5),
    ]

    def test_B1(self):
        expected_res = [[(25, 40, 'Воздвиженка'), (24, 50, 'Воздвиженка'), (3, 64, 'Новый Арбат'), (10, 100, 'Воздвиженка'), (4, 120, 'Тверская')]]
        res = [B1()]
        self.assertEqual(res, expected_res)
    def test_B2(self):
        expected_res = [[('Воздвиженка', 3), ('Новый Арбат', 1), ('Тверская', 1), ('Старый Арбат', 0), ('Волхонка', 0), ('Большая Никитская', 0)]]
        res = [B2()]
        self.assertEqual(res, expected_res)
    def test_B3(self):
        expected_res = [{25: ['Воздвиженка', 'Большая Никитская'], 24: ['Воздвиженка', 'Волхонка']}]
        res = [B3()]
        self.assertEqual(res, expected_res)

if __name__ == '__main__':
    unittest.main()

