
from simian.text.text_object import TextObject
import unittest

class TextObjectTest(unittest.TestCase):

     def setUp(self):
         self.text_object = TextObject('TestMessage',50,'Arial')

     def tearDown(self):
         self.text_object = None

     def test_message(self):
        message = self.text_object.text_message
        self.assertEqual(message,'TestMessage')

if __name__ == '__main__':
    unittest.main()
