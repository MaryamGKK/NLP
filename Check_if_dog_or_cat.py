from nltk.corpus import wordnet as wn
import re
def check(s):
    s = re.sub(r'[^\w]', ' ', s)
    s = s.lower().replace(" ",'_')
    dog = wn.synset("dog.n.01")
    types_of_dog = dog.hyponyms() 
    types_of_dog = sorted ([lemma.name() for synset in types_of_dog for lemma in synset.lemmas()])
    cat = wn.synset("cat.n.01")
    types_of_cat = cat.hyponyms() 
    types_of_cat = sorted ([lemma.name() for synset in types_of_cat for lemma in synset.lemmas()])
    if 'dog' in s or s in types_of_dog:
        return 'dog'
    elif 'cat' in s or s in types_of_cat:
        return 'cat'
    else:
        return s+ ' is not a cat or dog'
s = input()

print(check(s))





