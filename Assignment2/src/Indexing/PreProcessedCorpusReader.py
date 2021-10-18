import Classes.Path as Path

class PreprocessedCorpusReader:

    def __init__(self, type):

        if type == "trectext":
            self.fp = open(Path.ResultHM1 + type, 'r', encoding='utf-8')
        else: # if type == "trecweb":
            self.fp = open(Path.ResultHM1 + type, 'r', encoding='utf-8')
        return

    # Read a line for docNo from the corpus, read another line for the content, and return them in [docNo, content].
    def nextDocument(self):
        docNo = ""
        content = ""
        current_line = self.fp.readline().strip()  # read line and remove spaces from beginning and end of the line
        docNo = current_line

        if docNo != "":
            current_line = self.fp.readline().strip()
            content = current_line
            return [docNo, content]
        else:
            self.fp.close()
            return
