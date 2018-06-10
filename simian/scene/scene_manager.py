from simian.scene.base_scene import BaseScene
from simian.utils.singleton import Singleton


class SceneManager(metaclass=Singleton):

    def __init__(self):
        self.current_scene = None

        self.scene_list = []

    def add_scene(self, *args):
        # Check if scene already exists in list.
        for scene in list(args[0]):
            if issubclass(type(scene), BaseScene):
                on_list = self.is_scene_on_list(scene.name)
                # If it isn't, append it in list.
                if(not on_list):
                    self.scene_list.append(scene)
                else:
                    raise ValueError(
                        "This scene [" + scene.name + "] already exists")

    def remove_scene(self, scene_name):
        scene_to_remove = self.find_scene(scene_name)

        if(scene_to_remove is not None):
            # If we removed the current Scene, update the member variable
            # So we don't run a scene that is not in the list
            if(scene_name == self.current_scene.name):
                self.current_scene = None

            self.scene_list.remove(scene_to_remove)

    def load_next_scene(self):
        scene_list_length = len(self.scene_list)
        if(self.current_scene):
            next_scene_index = self.scene_list.index(self.current_scene) + 1
        else:
            next_scene_index = 0
        # Check if the current scene is the last scene of the game
        if(next_scene_index < scene_list_length):
            self.load_scene(self.scene_list[next_scene_index].name)
        else:
            raise ValueError("The current scene is the last scene")

    def load_scene(self, scene_name):
        scene = self.find_scene(scene_name)

        if(scene is not None):
            self.current_scene = scene
            self.current_scene.load()

    def is_scene_on_list(self, scene_name):
        try:
            self.find_scene(scene_name)
            return True
        except(ValueError):
            return False

    def find_scene(self, scene_name):
        for scene in self.scene_list:
            if(scene.name == scene_name):
                return scene

        # If we didn't return any scene, that means that the scene doesn't
        # exist on the list, or that there are no scenes on the list.
        raise ValueError("This scene doesn't exist")
