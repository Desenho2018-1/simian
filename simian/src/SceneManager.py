from BaseScene import BaseScene


class SceneManager(object):

    current_scene = BaseScene()

    scene_list = [current_scene]

    def add_scene(self, scene): 
        # Check if scene already exists in list.
        on_list = self.is_scene_on_list(scene.name)

        # If it isn't, append it in list.
        if(not on_list):
            self.scene_list.append(scene)
        else:
            raise ValueError("This scene already exists")

    def remove_scene(self, scene_name):
        scene_to_remove = self.find_scene(scene_name)

        if(scene_to_remove is not None):
            self.scene_list.remove(scene_to_remove)

            # If we removed the current Scene, update the member variable
            # So we don't run a scene that is not in the list
            if(scene_name == self.current_scene.name):
                self.current_scene = BaseScene()
        else:
            raise ValueError("This scene doesn't exist.")

    def load_scene(self, scene_name):
        scene = self.find_scene(scene_name)

        if(scene is not None):
            self.current_scene = scene
            self.current_scene.load()
        else:
            raise ValueError("This scene does not exist")

    def is_scene_on_list(self, scene_name):
        scene = self.find_scene(scene_name)

        if(scene is None):
            return False
        else:
            return True

    def find_scene(self, scene_name):
        for scene in self.scene_list:
            if(scene.name == scene_name):
                return scene
            else:
                raise ValueError("This scene doesn't exist")
