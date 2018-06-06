import unittest
from simian.scene.scene_manager import SceneManager
from simian.scene.base_scene import BaseScene


class SceneManagerTest(unittest.TestCase):
    
    def setUp(self):
        self.scene = BaseScene('dummy')
        self.scene_manager = SceneManager()

    def test_add_scene(self):
        self.scene_manager.add_scene(self.scene)
        inserted_scene = self.scene_manager.scene_list.pop()
        
        self.assertEqual(self.scene, inserted_scene)

    def test_add_scene_that_is_already_in_list(self):
        self.assertRaises(ValueError, self.scene_manager.add_scene(self.scene))

    def test_remove_scene_that_exists(self):
        self.scene_manager.add_scene(self.scene)
        self.scene_manager.remove_scene('dummy')
        inserted_scene = self.scene_manager.scene_list.pop()

        self.assertEquals(inserted_scene, None)
        
    def test_remove_scene_that_doesnt_exist(self):
        self.assertRaises(ValueError, self.scene_manager.remove_scene('dummy'))

    def test_load_next_scene(self):
        next_scene = BaseScene('dummy_two')
        
        self.scene_manager.add_scene(self.scene)
        self.scene_manager.add_scene(next_scene)

        self.scene_manager.current_scene = self.scene

        self.scene_manager.load_next_scene()

        self.assertEquals(self.scene_manager.current_scene, next_scene)

    def test_load_unexistent_next_scene(self):
        self.assertRaises(ValueError,
                          self.scene_manager.load_next_scene(self.scene))
    
    def test_load_scene(self):
        self.scene_manager.add_scene(self.scene)
        self.scene_manager.load_scene('dummy')

        self.assertEquals(self.scene_manager.current_scene, self.scene)

    def test_load_unexistent_scene(self):
        self.assertRaises(ValueError,
                          self.scene_manager.load_scene('dummy'))

    def test_is_scene_on_list(self):
        self.scene_manager.add_scene(self.scene)

        self.assertTrue(self.scene_manager.find_scene('dummy'))

    def test_is_scene_on_list_with_unexistent_scene(self):
        self.assertFalse(self.scene_manager.find_scene('dummy'))

    def test_find_scene(self):
        self.scene_manager.add_scene(self.scene)
        found_scene = self.scene_manager.find_scene('dummy')

        self.assertEquals(found_scene, self.scene)

    def test_find_scene_with_unexistent_scene(self):
        self.assertRaises(ValueError, self.scene_manager.find_scene('dummy'))
