from document import Document
class PDF_document(Document):
    def __init__(self, name, size, content):
        super().__init__(name, size, content)
    def open(self):
        return "Opening a pdf document"
    def read(self):
        return "reading a pdf document"
    def save(self):
        return "saving a pdf document"