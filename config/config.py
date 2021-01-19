import configparser
import os

__all__ = ('config', 'Config')


class Config:
    def __init__(self, file_name=os.path.join(os.path.dirname(__file__),
                                              '../configuration.cfg')):
        self._conf = self._load_screens(file_name)

    @property
    def logging(self):
        return self._conf.get('base', 'logging', fallback=True)

    @property
    def log_file(self):
        return self._conf.get('base', 'log_file', fallback=False)

    @property
    def dummy_data(self):
        return self._conf.get('base', 'dummy_data', fallback=False)

    @property
    def screens(self):
        screens = self._conf.get('base', 'screens', fallback='').strip('[]\n').split('\n')
        screens_conf = {}
        for screen in screens:
            screens_conf[screen] = dict(self._conf.items(screen))
        return screens_conf

    @property
    def refresh_interval(self):
        return self._conf.get('base', 'refresh_interval_minutes', fallback=15) * 60

    @staticmethod
    def _load_screens(file_name):
        conf = configparser.ConfigParser()
        conf.read_file(open(file_name))
        return conf


# we want to import the config across the files
config = Config()
