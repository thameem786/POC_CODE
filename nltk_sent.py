import nltk

with open("pdf_txt.txt","r") as f:
    a= f.read()


# print(nltk.sent_tokenize(a))

sents = nltk.sent_tokenize(a)

# The sentence split had to be done this way because the sent_tokenize
# function sometime get sentences with the newline character in between
# so we need to split it again on the \n character
# And also remove blank lines
sentence_list = []
for sent in sents:
    sent = sent.split('\n')
    for s in sent:
        if s.strip() != '':
            sentence_list.append(s.strip())
print(sentence_list)

