from abc import *


class APIProxy(ABC):
    def __init__(self):
        self.url = "None"
        self.app_key = ' '

    @abstractmethod
    def enter_data(self, action):
        pass

        
    @abstractmethod
    def fallback(self):
        pass