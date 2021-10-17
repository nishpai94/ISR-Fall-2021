import Classes.Path as Path
import csv
import sys

csv.field_size_limit(sys.maxsize)

# Efficiency and memory cost should be paid with extra attention.
class MyIndexReader:

    def __init__(self, type):

        if type == "trecweb":
            self.rDict = open(Path.IndexWebDir+"IndexWebDict.csv", 'r', encoding='utf-8')
            self.rPost = open(Path.IndexWebDir+"IndexWebPost.csv", 'r', encoding='utf-8')
            self.rDocIdDict = open(Path.IndexWebDir+"IndexDocIdDict.csv", 'r', encoding='utf-8')

        else:  # if type == "trectext"
            self.rDict = open(Path.IndexTextDir+"IndexTextDict.csv", 'r', encoding='utf-8')
            self.rPost = open(Path.IndexTextDir+"IndexTextPost.csv", 'r', encoding='utf-8')
            self.rDocIdDict = open(Path.IndexTextDir+"IndexDocIdDict.csv", 'r', encoding='utf-8')

        print("finish reading the index")

    # Return the integer DocumentID of input string DocumentNo.
    def getDocId(self, docNo):
        self.rDocIdDict.seek(0)
        reader = csv.reader(self.rDocIdDict)
        for row in reader:
            if row[0] == docNo:
                return row[1]  # return docId
        # if docNo not found
        return -1

    # Return the string DocumentNo of the input integer DocumentID.
    def getDocNo(self, docId):
        self.rDocIdDict.seek(0)
        reader = csv.reader(self.rDocIdDict)
        for row in reader:
            if row[1] == docId:
                return row[0]  # return docNo
        # if docId not found
        return -1

    # Return DF.
    def DocFreq(self, token):
        self.rPost.seek(0)
        reader = csv.reader(self.rPost)
        for row in reader:
            if row[0] == token:
                dictInString = row[1].lstrip('{').rstrip('}')
                dict1 = dict(map(str.strip, sub.split(':', 1)) for sub in dictInString.split(', ') if ':' in sub)
                df = len(dict1.keys())
                return df
        # if token not found
        return 0

    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        self.rDict.seek(0)
        reader = csv.reader(self.rDict)
        for row in reader:
            if row[0] == token:
                return row[1]
        # if token not found
        return 0

    # Return posting list in form of {documentID:frequency}.
    def getPostingList(self, token):
        self.rPost.seek(0)
        reader = csv.reader(self.rPost)
        for row in reader:
            if row[0] == token:
                dictInString1 = row[1].lstrip('{').rstrip('}')
                dict2 = dict(map(str.strip, sub.split(':', 1)) for sub in dictInString1.split(', ') if ':' in sub)
                return dict2
        return

# object1 = MyIndexReader("trectext")
# print(object1.getDocId("lists-000-0000010"))
# print(object1.getDocNo("200001"))
# print(object1.DocFreq("normal"))
# print(object1.CollectionFreq("palestinian"))
# print(object1.getPostingList("normal"))