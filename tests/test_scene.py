
from simian.scene.base_scene import BaseScene

class BaseSceneTest(unittest.TestCase):

    def setUp(self):
        self.baseScene = BaseScene('test',1)


    def tearDown(self):
        self.scene = None


    def test_name_scene(self):
        name = self.base.name
        assertEqual(name,'test')


    def test_id_scene(self):
        id = self.baseScene.id
        assertEqual(id,1)
