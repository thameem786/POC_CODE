# from PyDictionary import PyDictionary
#
# dictionary=PyDictionary()
#
#
# print (dictionary.synonym("Life"))


from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("goal"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print (set(synonyms))


from thesaurus import Word
w = Word(purpose)
print(w.synonyms())
