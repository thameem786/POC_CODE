from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,json
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
path = "C:\Thameem\Testing\LG_Twilight\security-guide.pdf"



def convert_pdf_to_txt(path_to_file):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    # codec = 'utf-8'
    # laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    fp = open(path_to_file, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    # doc.set_parser(parser)
    # parser.set_document(doc)
    # a=""
    ToC_list = []
    for i in doc.get_outlines():
        # print(i[1])
        ToC_list.append(i[1])
        # a=a+i[1]+" "
    # print(a)
    # print(ToC_list)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text,ToC_list

text,ToC_list = convert_pdf_to_txt(path)
# text = convert_pdf_to_txt("C:\\Thameem\\Testing\\admin.pdf")
# importing required modules
import PyPDF2

# creating a pdf file object
# pdfFileObj = open(r"C:\Users\thameem.sakkarai\Desktop\check\security-guide.pdf", 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# num_pages = pdfReader.numPages
# count = 0
# text = ""
# #The while loop will read each page
# while count < num_pages:
#     pageObj = pdfReader.getPage(count)
#     count +=1
#     text += pageObj.extractText()
# with open("pdf_txt.txt","w") as f:
#     f.write(str(text))
# print(text)
# printing number of pages in pdf file
# print(pdfReader.numPages)

# creating a page object
# pageObj = pdfReader

# extracting text from page
# print(pageObj.getContents())

# closing the pdf file object
# pdfFileObj.close()

# import slate
# with open(r"C:\Users\thameem.sakkarai\Desktop\check\security-guide.pdf") as f:
#     text= slate.PDF(f)
#
with open("pdf_txt.txt","w") as f:
    f.write(str(text))

print(ToC_list)
# print(text)
# with open("pdf_txt.txt","r") as f:
#     print(f.read())
#     json_txt = json.loads(f.read())
# print(json_txt)
