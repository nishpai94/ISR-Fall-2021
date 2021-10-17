import Classes.Path as Path
import csv
from collections import OrderedDict

# Efficiency and memory cost should be paid with extra attention.
class MyIndexWriter:

    def __init__(self, type):

        self.docIdDict = OrderedDict()  # storing Dictionary for docIds
        self.termDict = OrderedDict()  # Term Dictionary
        self.posting = {}  # store posting dict

        if type == "trecweb":
            self.wDict = open(Path.IndexWebDir+"IndexWebDict.csv", 'w', encoding='utf-8')
            self.wPost = open(Path.IndexWebDir+"IndexWebPost.csv", 'w', encoding='utf-8')
            self.wDocIdDict = open(Path.IndexWebDir+"IndexDocIdDict.csv", 'w', encoding='utf-8')
        else:  # if type == "trectext"
            self.wDict = open(Path.IndexTextDir+"IndexTextDict.csv", 'w', encoding='utf-8')
            self.wPost = open(Path.IndexTextDir+"IndexTextPost.csv", 'w', encoding='utf-8')
            self.wDocIdDict = open(Path.IndexTextDir+"IndexDocIdDict.csv", 'w', encoding='utf-8')

        # initialize the integer doc_id
        if type == "trecweb":
            self.docId = 1
        else:  # if type == "trectext"
            self.docId = 200000

        #initialize count as 0
        #self.count = 0
        return

    # This method build index for each document.
	# NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
    # and in MyIndexReader, you should be able to request the integer docid for each docno.
    def index(self, docNo, content):

        termList = content.split()  # creating list of terms from the content

        # Adding term to dictionary & calculating collection frequency
        # in form of termDict[term] = collectionFreq
        for term in termList:
            if term not in self.termDict:
                self.termDict[term] = 1
            else:
                self.termDict[term] += 1
            # Adding term, docId and term frequency to posting dict
            # in form of posting[term][docId] = termFreq
            if term not in self.posting.keys():
                self.posting[term] = {}
                self.posting[term][self.docId] = 1
            else:
                # this only when the docId key is not found
                if self.docId not in self.posting[term].keys():
                    self.posting[term][self.docId] = 0  # initialize the term frequency value with zero
                self.posting[term][self.docId] += 1  # once the docId key is added we can just increment the count
        # TODO : to remove this
        #print(self.posting)
        #print(self.termDict)

        # dictionary for {docNo:docId}
        if docNo not in self.docIdDict:
            self.docIdDict[docNo] = self.docId
            self.docId += 1
        # TODO: to remove print
        #print(self.docIdDict)

        return

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):

        # write posting file to hard disk
        writer = csv.writer(self.wPost)
        for key, value in self.posting.items():
            writer.writerow([key, value])

        del self.posting
        self.wPost.close()

        # write dictionary term file to hard disk
        writer = csv.writer(self.wDict)
        for key, value in self.termDict.items():
            writer.writerow([key, value])

        del self.termDict
        self.wDict.close()

        # write DocId dictionary file to hard disk
        writer = csv.writer(self.wDocIdDict)
        for key, value in self.docIdDict.items():
            writer.writerow([key, value])

        del self.docIdDict
        self.wDocIdDict.close()

        return

# object2 = MyIndexWriter("trectext")
# object2.index('lists-000-0000000', "normal egypt activ support anti iraq coalit gulf crisi symbol visit egyptian presid hosni mubarak jordan januari time jordan improv ti palestinian dispel fear arous palestinian due jordan' special role jerusalem jordanian isra accord addit jordan made effort push forward palestinian isra negoti expand palestinian autonomi west bank benefit jordan' peac treati israel attitud baghdad brought warmer")
# object2.index('lists-000-0000010', "normal normal egypt activ support anti iraq coalit gulf crisi symbol visit egyptian presid hosni mubarak jordan januari time jordan improv ti palestinian dispel fear arous palestinian due jordan' special role jerusalem jordanian isra accord addit jordan made effort push forward palestinian isra negoti expand palestinian autonomi west bank benefit jordan' peac treati israel attitud baghdad brought warmer")
# object2.close()
#TODO: senior code

# if self.type == "trecweb":
#     docId = "00" + (docNo[6:9]) + (docNo[10:len(docNo)])
# else:  # if self.type = "trectext"
#     if (docNo[0:3]) == "XIE":
#         docId = "01" + (docNo[3:11]) + (docNo[12:len(docNo)])  # converting to integer docIds
#     else:
#         docId = "02" + (docNo[3:11]) + (docNo[12:len(docNo)])