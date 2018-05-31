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

    
    def is_scene_on_list(self, scene_name):
        scene = self.find_scene(scene_name)

        if(scene is None):
            return False
        else:
            return True

