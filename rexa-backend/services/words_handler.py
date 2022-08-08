import nltk

"""list of words to remove meaningless words"""

words = set(nltk.corpus.words.words())

def meaningful_check(word):
    word = word.lower()
    word_length = len(word.split(" "))
    if((word in words and word_length==1) or word_length>1):
        return True
    else:
        return False