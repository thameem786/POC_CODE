from tika import parser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser


path = "C:\Thameem\Testing\xxx\security-guide.pdf"
parsed_txt = parser.from_file(path)
text =parsed_txt["content"]
print(text)

if path.split(".")[1] =="pdf":
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    ToC_list =[i[1] for i in doc.get_outlines()]
    print(ToC_list)

# lst =[i for i in lst if re.search("[A-Za-z]{3,}",i) and re.sub("^[0-9]+","",i).strip() not in Filtered_ToC_list]
#     print(lst)
#     processed_txt= " ".join([re.sub("'|\"|\\\\","",x) for x in lst]
# text = " ".join([s for s in text.split("\n") if s and])
# print(text)
