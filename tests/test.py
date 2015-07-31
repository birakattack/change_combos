#!/usr/bin/python

from lib.change_combos import ChangeCombos
import unittest


class TestComboCount(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.change_combos = ChangeCombos([1, 5, 10, 25, 50, 100])

    def test_combo_base_cases(self):
        self.assertEqual(self.change_combos.combo_count(1), 1)
        self.assertEqual(self.change_combos.combo_count(5), 2)
        self.assertEqual(self.change_combos.combo_count(10), 4)


if __name__ == '__main__':
    unittest.main()
