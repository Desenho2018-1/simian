
from simian.text.text_object import TextObject
import unittest

class TextObjectTest(unittest.TestCase):

     def setUp(self):
         self.text_object = TextObject('TestMessage',50,'Arial')
         self.font_object_none = self.text_object.font_object
         self.font_object_test_method = self.text_object.font_object

     def tearDown(self):
         self.text_object = None

     def test_message(self):
        message = self.text_object.text_message
        self.assertEqual(message,'TestMessage')

     def test_size(self):
         size = self.text_object.size
         self.assertEqual(size,50)


     def test_font(self):
         size = self.text_object.font_text
         self.assertEqual(size,'Arial')

     def test_font_object(self):
         font_object = self.font_object_none
         self.assertEqual(None,self.font_object_none)

    



if __name__ == '__main__':
    unittest.main()
