from __future__ import print_function
import Classes.Path as Path
import nltk.stem.porter as StemPorter

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    def __init__(self):
        self.stemmer = StemPorter.PorterStemmer()
        self.dict = dict()  # getting an empty dictionary
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        word = word.lower()
        return word

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        if word in self.dict:  # checking if the word is in the dictionary
            stemWord = self.dict[word]  # assign the dictionary key value to the stem word
        else:
            stemWord = self.stemmer.stem(word)  # do word stemming and assign it to the stem word
            self.dict[word] = stemWord  # then assign the stem word to the dictionary key value

        return stemWord

