import Classes.Document as Document
from operator import attrgetter


class QueryRetrievalModel:

    indexReader=[]
    def __init__(self, ixReader):
        self.indexReader = ixReader
        self.miu = 1980
        self.len = 0
        for x in range(self.indexReader.getDocCount()):
            self.len += self.indexReader.getDocLength(x)
        self.postingListDict = {}  # term:postingList
        self.collectionFreqDict = {}  # term:collectionFreq
        self.docLenDict = {}  # term:docLength
        return


    # query:  The query to be searched for.
    # topN: The maximum number of returned documents.
    # The returned results (retrieved documents) should be ranked by the score (from the most relevant to the least).
    # You will find our IndexingLucene.Myindexreader provides method: docLength().
    # Returned documents should be a list of Document.
    def retrieveQuery(self, query, topN):

        docIdList = []
        documentList = []

        for term in query.queryContent.split():
            postingList = self.indexReader.getPostingList(term)
            self.postingListDict[term] = postingList # taking a copy for using later
            self.collectionFreqDict[term] = self.indexReader.CollectionFreq(term)
            docIdList.append(set(list(postingList.keys())))

        # find the intersection of all the document ids to find document where all the words of the query is present
        resultsetDocId = set.intersection(*docIdList)

        # populate the documentList
        for docId in resultsetDocId:
            document = Document.Document()
            document.setDocId(docId)
            document.setDocNo(self.indexReader.getDocNo(docId))
            score = self.dirichletScore(query.queryContent, docId)
            document.setScore(score)
            documentList.append(document)

        # sort/rank the documentList as per the score
        sortedDocumentList = sorted(documentList, key=attrgetter('score'), reverse=True)

        # return topN from the list
        return sortedDocumentList[:topN]

    def dirichletScore(self, queryContent, docId):
        docScore = 1.0
        docLen = self.indexReader.getDocLength(docId)
        doc_adj_len = docLen + self.miu
        len_adj = self.miu/self.len
        for term in queryContent.split():
            colFreq = self.collectionFreqDict[term]
            docTermFreq = self.postingListDict[term][docId]
            docScore *= (docTermFreq + len_adj * colFreq) / doc_adj_len
        return docScore

