from document import Document
class Word_document(Document):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)
    def open(self):
        return "Opening a word document"
    def read(self):
        return "reading a word document"
    def save(self):
        return "saving a word document"