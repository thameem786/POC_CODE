import spacy

nlp = spacy.load('en_core_web_md')
faqlist=["python","purpose python","Want to know more about python.","python serve?","python aspire achieve?","business area python?","role Contract Management?"]

while True:
     doc1 = nlp(input(u"enter first sentence"))
     doc2 = nlp(input(u"enter second sentence"))
     print("spacy :", doc1.similarity(doc2))
     for i in faqlist:
          print("spacy :"+i.lower(), doc1.similarity(nlp(i.lower())))
          print("spacy :"+i.lower(), doc2.similarity(nlp(i.lower())))

