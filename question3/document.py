from abc import ABC, abstractmethod
class Document(ABC):
    def __init__(self,name,size,content):
        self.name = name
        self.size = size
        self.content = content
    @abstractmethod
    def open(self):
        pass
    def read(self):
        pass
    def save(self):
        pass