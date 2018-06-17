from simian.scene.base_scene import BaseScene, State
from simian.utils.singleton import Singleton


class SceneManager(metaclass=Singleton):

    def __init__(self):
        self.current_scene = None
        self.next_scene = None
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

    def set_next_scene(self, scene_name):
        next_scene = self.find_scene(scene_name)

        if(next_scene):
            self.next_scene = next_scene
        else:
            raise ValueError("Can't set next scene ["+scene_name+"], \
                              scene not found.")

    def remove_scene(self, scene_name):
        scene_to_remove = self.find_scene(scene_name)

        if(scene_to_remove is not None):
            # If we removed the current Scene, update the member variable
            # So we don't run a scene that is not in the list
            if(scene_name == self.current_scene.name):
                self.current_scene = None

            self.scene_list.remove(scene_to_remove)

    def load_next_scene(self):
        if(self.next_scene):
            self.load_scene(self.next_scene.name)
        else:
            raise ValueError("No next scene to load!")

    def load_scene(self, scene_name):
        scene = self.find_scene(scene_name)

        if(scene is not None):
            if(self.current_scene):
                self.current_scene.unload()
            self.current_scene = scene
            self.current_scene.state = State.STARTED
            self.current_scene.load()

    def update(self, time_elapsed):
        if(self.current_scene):
            self.current_scene.update(time_elapsed)
        else:
            raise ValueError("Scene was not set, can't update.")

    def draw(self, graphics):
        if(self.current_scene):
            self.current_scene.draw(graphics)
            if(self.current_scene.state == State.FINISHED):
                self.load_next_scene()
        else:
            raise ValueError("Scene was not set, can't draw.")

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
