from factory import Factory
from word_document import Word_document
from pdf_document import PDF_document
from execl_document import Execl_document
user = Factory()
print(user.open(Word_document("exam","32kb","This is my final exam")))
print(user.save(Word_document("exam","32kb","This is my final exam")))
print(user.read(Word_document("exam","32kb","This is my final exam")))
print(user.open(PDF_document("exam","32kb","This is my final exam")))
print(user.save(PDF_document("exam","32kb","This is my final exam")))
print(user.read(PDF_document("exam","32kb","This is my final exam")))
print(user.open(Execl_document("exam","32kb","This is my final exam")))
print(user.save(Execl_document("exam","32kb","This is my final exam")))
print(user.read(Execl_document("exam","32kb","This is my final exam")))