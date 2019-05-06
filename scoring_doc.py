import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

sentence_list = ['SAP HANA – DATA REPLICATION', 'SAP HANA Replication allows migration of data from source systems to SAP HANA database.',]
filtered_sentence_list = []
for i in sentence_list:
    filtered_sentence = utils.clean_doc(i)
    filtered_sentence_list.append(" ".join(filtered_sentence))



def word_tfidf_score_generator(filtered_sentence_list):
    cv = CountVectorizer(ngram_range=(1, 2))
    # convert text data into term-frequency matrix
    data = cv.fit_transform(filtered_sentence_list)
    tfidf_transformer = TfidfTransformer()
    # convert term-frequency matrix into tf-idf
    tfidf_matrix = tfidf_transformer.fit_transform(data)
    # create dictionary to find a tfidf word each word
    word_idf_score = dict(zip(cv.get_feature_names(), tfidf_transformer.idf_))
    return word_idf_score


word_idf_score = word_tfidf_score_generator(filtered_sentence_list)
print(word_idf_score)
user_q=[('sap hana'), ('business suite')]

sentence_with_score={}

for sentence in filtered_sentence_list:
    score=0
    for i in user_q:
        if str(i) in sentence and str(i) in word_idf_score.keys():
            score+=word_idf_score[i]
    sentence_with_score[sentence]=score

sorted_sentence_with_score = dict(sorted(sentence_with_score.items(), key=lambda x: x[1], reverse=True))
print(sorted_sentence_with_score)

max = list(sorted_sentence_with_score.values())
sorted_sentences = []
for k,v in sorted_sentence_with_score.items():
    if v==max[0]:
        sorted_sentences.append(k)

print("sorted_sentences",sorted_sentences)
#
print(len(sorted_sentences))
sent =[0, 1, 43, 47, 55, 76, 77, 80, 88, 90, 96, 97, 98, 99, 100, 110, 112, 137, 146, 149, 151, 156, 157, 166]
sort_sentences = []
# for i in sent:
#     sort_sentences.append(sentence_list[i])
# print("sort sentences",sort_sentences)
# print(len(sort_sentences))
#
#
new_s_list =[]
if len(sorted_sentences)>5:
    for s in sorted_sentences:
        text = nltk.word_tokenize(s)
        # print(text)
        tag_tuple_list = nltk.pos_tag(text)
        # print(tag_tuple_list)
        verb_found = False
        for word, tag in tag_tuple_list:
            if tag.startswith("VB"):
                verb_found = True
                # print("WORD- {} \t\t TAG- {}".format(word, tag))

        if verb_found is True:
            new_s_list.append(s)

print("new_s_list",new_s_list)
print(len(new_s_list))





