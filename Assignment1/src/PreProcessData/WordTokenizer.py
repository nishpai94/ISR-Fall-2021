import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.

class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        list = []
        finalList = []  # this list consists of tokenized words (words without special characters)
        strip_content = content.strip()  # to remove the spaces from beginning and end of the line
        strip_content = strip_content.replace('\n', ' ')  # replace /n with a space
        list = strip_content.split(' ')  # splits the list at whitespaces
        # handling special cases
        specialCharList = [',', '.', "'s", '(', ')', ';', ':', "--", '!', '"', "``", "'"]
        for item in list:
            for specialChar in specialCharList:
                while specialChar in item:
                    # recursive method to remove multiple special characters
                    item = self.replaceWithNull(specialChar, item)

            # sometimes item can be just a null string
            if item != '':
                finalList.append(item)

        self.finalListIter = iter(finalList)
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        word = ""
        word = next(self.finalListIter, None)
        return word

    def replaceWithNull(self, specialChar, word):
        # Replaces special characters with null/nothing
        resultWord = word.replace(specialChar, '')
        return resultWord
