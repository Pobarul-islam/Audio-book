import PyPDF2
import pyttsx3

book = open("oop.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
page = pdfReader.getPage(1-111)
text = page.extractText()

friend = pyttsx3.init()
friend.say(text)
friend.runAndWait()
