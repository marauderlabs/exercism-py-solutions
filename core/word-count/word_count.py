from collections import Counter
import string

def count_words(sentence):
    punc = string.punctuation.replace("'", "") #Get a list of punctuations without apostrophe

    translation = str.maketrans(punc, ' '*len(punc)) #map punctuation to space
    words = sentence.translate(translation).lower().split() #replace punctuations to space for easy split

    words =[w.strip("'") for w in words] #now strip off the apostrophes on either end
    return dict(Counter(words)) #count them
