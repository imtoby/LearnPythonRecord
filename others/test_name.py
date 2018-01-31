# *- coding: utf-8 -*
# Created by: ZhaoDongshuang
# Created on: 2018/1/27

import unittest

from others.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        self.assertEqual(get_formatted_name('janis', 'joplin'),
                         'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
