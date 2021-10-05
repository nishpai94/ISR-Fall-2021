import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrectextCollection:

    def __init__(self):

        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        self.fp = open(Path.DataTextDir, 'r', encoding='utf-8')
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        docNo = ""
        content = ""
        curr_line = self.fp.readline().strip()  # read line and remove spaces from beginning and end of the line
        readflag = 0
        while '</DOC>' not in curr_line:  # read lines until you find </DOC>

            if '<DOCNO>' in curr_line and '</DOCNO>' in curr_line:
                docNo = curr_line.lstrip('<DOCNO>').rstrip('</DOCNO>').strip()

            elif '<TEXT>' in curr_line:
                readflag = 1

            elif '</TEXT>' in curr_line:
                readflag = 0

            elif readflag == 1:
                content = content + '\n' + curr_line

            elif curr_line == '':
                break

            curr_line = self.fp.readline().strip()

        if docNo == "":
            self.fp.close()
            return
        else:
            return [docNo, content]




