import unittest
from simian.scene.scene_manager import SceneManager
from template_game.template_scene import TemplateScene

class SceneManagerTest(unittest.TestCase):

    def setUp(self):
        self.scene = TemplateScene('dummy',1)
        self.scenes = (self.scene,)
        self.scene_manager = SceneManager()
        self.scene_manager.scene_list = []
        self.scene_manager.current_scene = None

    def tearDown(self):
        self.scene = None
        self.scene_manager = None

    def test_add_scene(self):
        self.scene_manager.add_scene(self.scenes)
        inserted_scene = self.scene_manager.scene_list.pop()

        self.assertEqual(self.scene, inserted_scene)

    def test_add_scene_that_is_already_in_list(self):
        self.scene_manager.add_scene(self.scenes)
        self.assertRaises(ValueError, self.scene_manager.add_scene, self.scenes)

    def test_remove_scene_that_exists(self):
        self.scene_manager.add_scene(self.scenes)
        self.scene_manager.remove_scene('dummy')
        self.assertRaises(ValueError, self.scene_manager.find_scene, 'dummy')

    def test_remove_current_scene(self):
        self.scene_manager.add_scene(self.scenes)
        self.scene_manager.load_scene('dummy')
        self.scene_manager.remove_scene('dummy')
        self.assertRaises(ValueError, self.scene_manager.find_scene, 'dummy')

    def test_remove_scene_that_doesnt_exist(self):
        self.assertRaises(ValueError, self.scene_manager.remove_scene, 'dummy')

    def test_load_next_scene(self):
        next_scene = BaseScene('dummy_two')

        self.scene_manager.add_scene(self.scene)
        self.scene_manager.add_scene(next_scene)

        self.scene_manager.current_scene = self.scene

        self.scene_manager.load_next_scene()

        self.assertEqual(self.scene_manager.current_scene, next_scene)

    def test_load_next_scene_after_last(self):
        self.scene_manager.add_scene(self.scenes)
        self.scene_manager.load_next_scene()

        self.assertRaises(ValueError, self.scene_manager.load_next_scene)

    def test_load_unexistent_next_scene(self):
        with self.assertRaises(ValueError) as error:
            self.scene_manager.load_next_scene()
        exception = str(error.exception)
        self.assertEqual(exception, "The current scene is the last scene")

    def test_load_scene(self):
        self.scene_manager.add_scene(self.scenes)
        self.scene_manager.load_scene('dummy')

        self.assertEqual(self.scene_manager.current_scene, self.scene)

    def test_load_unexistent_scene(self):
        self.assertRaises(ValueError,
                          self.scene_manager.load_scene, 'dummy')

    def test_is_scene_on_list(self):
        self.scene_manager.add_scene(self.scenes)

        self.assertTrue(self.scene_manager.is_scene_on_list('dummy'))

    def test_is_scene_on_list_with_unexistent_scene(self):
        self.assertFalse(self.scene_manager.is_scene_on_list('dummy'))

    def test_find_scene(self):
        self.scene_manager.add_scene(self.scenes)
        found_scene = self.scene_manager.find_scene('dummy')

        self.assertEqual(found_scene, self.scene)

    def test_find_scene_with_unexistent_scene(self):
        self.assertRaises(ValueError, self.scene_manager.find_scene, 'dummy')
