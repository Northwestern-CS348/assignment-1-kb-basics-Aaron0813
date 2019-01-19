import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)

    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")
        

    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")

    def test6(self):
        ask1 = read.parse_input("fact: (inst ?X pyramid)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : pyramid1")
        self.assertEqual(str(answer[1]), "?X : pyramid2")
        self.assertEqual(str(answer[2]), "?X : pyramid3")
        self.assertEqual(str(answer[3]), "?X : pyramid4")

    def test7(self):
        ask1 = read.parse_input("fact: (size ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : big")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : small")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : small")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : small")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : big")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : big")
'''
    def test6(self):
        ask1 = read.parse_input("fact: (container ?X big)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
'''
        

if __name__ == '__main__':
    unittest.main()
