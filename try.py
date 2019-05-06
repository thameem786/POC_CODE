# a=["this" "isa" "page"]
# for i ,j in enumerate(a):
#     tlist=["is","a"]
#     del a[i]
#     for ix in range(len(tlist)):
#         a.insert(i+ix,tlist[ix])
# print(a)

from docx import *

document = Document('sample.docx')
bolds=[]
italics=[]
for para in document.paragraphs:
    for run in para.runs:
        if run.italic :
            italics.append(run.text)
        if run.bold :
            bolds.append(run.text)

boltalic_Dict={'bold_phrases':bolds,
              'italic_phrases':italics}

