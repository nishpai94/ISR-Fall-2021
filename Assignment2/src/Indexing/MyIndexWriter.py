import Classes.Path as Path
import csv

# Efficiency and memory cost should be paid with extra attention.
class MyIndexWriter:

    def __init__(self, type):

        self.docIdDict = {}  # storing Dictionary for docIds
        self.termDict = {}  # Term Dictionary
        self.posting = {}  # store Posting dict

        if type == "trecweb":
            self.wDict = open(Path.IndexWebDir + "IndexWebDict", 'w', encoding='utf-8')
            self.wPost = open(Path.IndexWebDir + "IndexWebPost", 'w', encoding='utf-8')
            self.wDocIdDict = open(Path.IndexWebDir + "IndexDocIdDict", 'w', encoding='utf-8')
        else:  # if type == "trectext"
            self.wDict = open(Path.IndexTextDir + "IndexTextDict", 'w', encoding='utf-8')
            self.wPost = open(Path.IndexTextDir + "IndexTextPost", 'w', encoding='utf-8')
            self.wDocIdDict = open(Path.IndexTextDir + "IndexDocIdDict", 'w', encoding='utf-8')

        # initialize the integer doc_id
        if type == "trecweb":
            self.docId = 1
        else:  # if type == "trectext"
            self.docId = 200000

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
                self.termDict[term] = 1   # assigning term collection frequency value as 1
            else:
                self.termDict[term] += 1   # increment collection frequency by 1

            # Adding term, docId and term frequency to posting dict
            # in form of posting[term][docId] = termFreq
            if term not in self.posting.keys():
                self.posting[term] = {}  # make a nested dictionary
                self.posting[term][self.docId] = 1  # assigning term frequency value to 1
            else:
                # this is only when the docId key is not found
                if self.docId not in self.posting[term].keys():
                    self.posting[term][self.docId] = 0  # initialize the term frequency value with zero
                self.posting[term][self.docId] += 1  # once the docId key is added we can just increment the count

        # dictionary for {docNo:docId}
        if docNo not in self.docIdDict:
            self.docIdDict[docNo] = self.docId
            self.docId += 1

        return

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):

        # write posting file to hard disk
        self.writeToFile(self.wPost, self.posting)

        # write dictionary term file to hard disk
        self.writeToFile(self.wDict, self.termDict)

        # write DocId dictionary file to hard disk
        self.writeToFile(self.wDocIdDict, self.docIdDict)

        return

    # Function to write to the above files
    def writeToFile(self, filename, dictname):
        # writing respective files to hard disk
        writer = csv.writer(filename)
        writer.writerows(dictname.items())  # write rows of respective dictionaries
        del dictname  # clear dictionary
        filename.close()
        return
