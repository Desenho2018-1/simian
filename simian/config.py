import ConfigParser
import io

IMAGE_ASSETS_PATH = ''
AUDIO_ASSETS_PATH = ''

class Configuration():

    def __init__():
        self.paths_section = 'paths'
        self.image_assets_path = 'IMAGE_ASSETS_PATH'
        self.audio_assets_path = 'AUDIO_ASSETS_PATH'
        self.load_file()
        self.load_config()

    def load_file():
        with open("config.ini") as f:
            configuration = f.read()
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.readfp(io.BytesIO(configuration))

    def load_config():
        AUDIO_ASSETS_PATH = self.config.get(self.paths_section, self.audio_assets_path)
        IMAGE_ASSETS_PATH = self.config.get(self.paths_section, self.image_assets_path)
