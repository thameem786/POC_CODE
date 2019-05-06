from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import re,string
exclude = set(string.punctuation)
print (exclude)
file = open(r"sample.txt", "r")
# doc = re.sub(r"[(\[\]),;:\.]", "", file.read())
stop_words = set(stopwords.words('english'))
print(stop_words)
tokens =file.read().split()
print(tokens)
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
word_tokens = [re_punc.sub('', w) for w in tokens]
# print(word_tokens)
# wordcount = Counter(word_tokens)
# print(wordcount)
# for i in set(word_tokens):
#     print(i,word_tokens.count(i))

# csv_file = open('word.csv','a')
# for i in set(word_tokens):
#     result=i+','+str(word_tokens.count(i))+'\n'
#     csv_file.write(result)
# csv_file.close()
filtered_sentence = [w for w in word_tokens if  not w.lower() in stop_words and w not in ""]
#
wordcount = Counter(filtered_sentence)
print(wordcount)
first3pairs =[word for word,cnt in wordcount.most_common(3)]
print(first3pairs)