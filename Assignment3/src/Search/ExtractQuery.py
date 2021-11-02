from __future__ import print_function
import Classes.Query as Query
import Classes.Path as Path
import nltk.stem.porter as StemPorter

class ExtractQuery:

    #query = Query.Query() # create an object of Query class

    def __init__(self):
        # 1. you should extract the 4 queries from the Path.TopicDir
        # 2. the query content of each topic should be 1) tokenized, 2) to lowercase, 3) remove stop words, 4) stemming
        # 3. you can simply pick up title only for query.
        self.topicFile = open(Path.TopicDir, 'r', encoding='utf-8')

        self.stopWordFile = open(Path.StopwordDir, 'r', encoding='utf-8')
        self.stopWords = self.stopWordFile.read().splitlines()

        self.stemmer = StemPorter.PorterStemmer()
        self.dict = dict()  # getting an empty dictionary for stemming
        self.queryList = []  # this is for list of queries

        count = 0
        for line in self.topicFile:
            if '<num>' in line:
                query = Query.Query()
                query.setTopicId(line.lstrip('<num> Number:').strip())
                self.queryList.append(query)
            if '<title>' in line:
                line1 = line.lstrip('<title>').strip()
                processedData = self.preProcessData(line1)
                self.queryList[count].setQueryContent(processedData)
                count+=1 #increment the count every query
        return

    # Tokenization of query content , lowercase, remove stopword & stem
    def preProcessData(self, content):
        processedContent = ""
        contentList = iter(content.split(' '))
        for word in contentList:
            # handling special cases
            if '"' in word:
                word = word.replace('"', '')
            # lower the case
            lowerCase = word.lower()
            # remove stopword
            if lowerCase not in self.stopWords:
                processedContent += self.stem(word) + " "
        return processedContent

    # stemming function
    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        if word in self.dict:  # checking if the word is in the dictionary
            stemWord = self.dict[word]  # assign the dictionary key value to the stem word
        else:
            stemWord = self.stemmer.stem(word)  # do word stemming and assign it to the stem word
            self.dict[word] = stemWord  # then assign the stem word to the dictionary key value
        return stemWord


    # Return extracted queries with class Query in a list.
    def getQuries(self):
        return self.queryList
