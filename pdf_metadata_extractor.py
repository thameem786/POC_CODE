from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open(r"C:\Users\thameem.sakkarai\Desktop\check\security-guide.pdf", 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)

print (doc.info)