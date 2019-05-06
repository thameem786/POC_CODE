from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io,re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import logging
from tika import parser

logging.debug('This is a debug message')

path = "C:\Thameem\Testing\LG_Twilight\security-guide.pdf"


def convert_pdf_to_txt(path_to_file):
    try:
        # rsrcmgr = PDFResourceManager()
        # retstr = io.StringIO()
        # device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
        # fp = open(path_to_file, 'rb')
        # parser = PDFParser(fp)
        # doc = PDFDocument(parser)
        # ToC_list = []
        # for i in doc.get_outlines():
        #     ToC_list.append(i[1])
        # interpreter = PDFPageInterpreter(rsrcmgr, device)
        # for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="",caching=True, check_extractable=True):
        #     interpreter.process_page(page)
        # text = retstr.getvalue()
        # fp.close()
        # device.close()
        # retstr.close()
        # Filtered_ToC_list = [re.sub("^[0-9]+", "", i).strip() for i in ToC_list]
        parsed_txt = parser.fromfile(path_to_file)
        text = parsed_txt["content"]
        fp = open(path, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument(parser)
        ToC_list = [i[1] for i in doc.get_outlines()]
        Filtered_ToC_list = [re.sub("^[0-9]+", "", i).strip() for i in ToC_list]
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    return text,Filtered_ToC_list

parsed_text,Filtered_ToC_list = convert_pdf_to_txt(path)


def pdf_txt_preprocessing(text,Filtered_ToC_list):
    file = text.split("\n")
    lst=[i.encode('utf8','ignore').decode("utf8").strip() for i in file if i!=""]
    lst = [re.sub("\s+"," ",i) for i in lst]
    lst =[i for i in lst if re.search("[A-Za-z]{3,}",i) and re.sub("^[0-9]+","",i).strip() not in Filtered_ToC_list]
    print(lst)
    processed_txt= " ".join([re.sub("'|\"|\\\\","",x) for x in lst])
    return processed_txt

processed_txt = pdf_txt_preprocessing(parsed_text,Filtered_ToC_list)

print(processed_txt)
