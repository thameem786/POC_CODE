# a=["this" "isa" "page"]
# for i ,j in enumerate(a):
#     tlist=["is","a"]
#     del a[i]
#     for ix in range(len(tlist)):
#         a.insert(i+ix,tlist[ix])
# print(a)

from docx import *
doc= Document(r'Customer Portal.docx')
bolds=[]
italics=[]
for para in doc.paragraphs:
    print(para.text)
    for run in para.runs:
        # if run. :
        #     italics.append(run.text)
        if run.bold :
            bolds.append(run.text)
#
# with open("Customer Portal.docx","r") as fh:
#     a=fh.readlines()
# print(a)


# boltalic_Dict={'bold_phrases':bolds,
#               'italic_phrases':italics}
#
# print(boltalic_Dict)

