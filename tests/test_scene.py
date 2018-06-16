from simian.scene.base_scene import BaseScene
from simian.exceptions.unimplemented_method import NotOverriddenMethod
import unittest


class BaseSceneTest(unittest.TestCase):

    def setUp(self):
        self.baseScene = BaseScene('test', 1)

    def tearDown(self):
        self.scene = None

    def test_name_scene(self):
        name = self.baseScene.name
        self.assertEqual(name, 'test')

    def test_id_scene(self):
        id = self.baseScene.id
        self.assertEqual(id, 1)

    def test_unimplemented_method_load(self):

        try:
            self.baseScene.load()
        except Exception as message:
            message_exception = str(message)
            self.assertEqual("the method load isn't overridden",
                             message_exception)

    def test_unimplemented_method_unload(self):

        try:
            self.baseScene.unload()
        except Exception as message:
            message_exception = str(message)
            self.assertEqual("the method unload isn't overridden",
                             message_exception)

    def test_unimplemented_method_draw(self):

        grafics = None
        try:
            self.baseScene.draw(grafics)
        except Exception as message:
            message_exception = str(message)
            self.assertEqual("the method draw isn't overridden",
                             message_exception)

    def test_unimplemented_method_update(self):

        time_elapsed = None
        try:
            self.baseScene.update(time_elapsed)
        except Exception as message:
            message_exception = str(message)
            self.assertEqual("the method update isn't overridden",
                             message_exception)

if __name__ == '__main__':
    unittest.main()
