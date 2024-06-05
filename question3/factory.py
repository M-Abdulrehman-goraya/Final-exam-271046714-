from word_document import Word_document
from pdf_document import PDF_document
from execl_document import Execl_document
class Factory:
    def open(self,type):
        self.type = type
        return self.type.open()
    def save(self,type):
        self.type = type
        return self.type.save()
    def read(self,type):
        self.type = type
        return self.type.read()