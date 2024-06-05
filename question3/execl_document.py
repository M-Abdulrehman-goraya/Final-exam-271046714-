from document import Document
class Execl_document(Document):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)
    def open(self):
        return "Opening a execl document"
    def read(self):
        return "reading a execl document"
    def save(self):
        return "saving a execl document"