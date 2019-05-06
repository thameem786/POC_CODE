import re,string


doc = "viwejbv jovniovnwvwev"
re.sub(r"[(\[\])-]", "  ", doc)
tokens = doc.split()
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
tokens = [re_punc.sub('', w) for w in tokens]
