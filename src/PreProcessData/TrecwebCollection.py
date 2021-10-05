import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrecwebCollection:

    def __init__(self):
        # 1. Open the file in Path.DataWebDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        self.fp = open(Path.DataWebDir, 'r', encoding='utf-8')
        self.clean = re.compile('<.*?>')  # removing html tags
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        # 3. the HTML tags should be removed in document content.
        docNo = ""
        content = ""
        curr_line = self.fp.readline().strip()  # read line and remove spaces from end and beginning of the line
        readflag = 0
        while '</DOC>' not in curr_line:  # read lines until you find </DOC>

            if '<DOCNO>' in curr_line and '</DOCNO>' in curr_line:
                docNo = curr_line.lstrip('<DOCNO>').rstrip('</DOCNO>').strip()

            elif readflag == 1:
                content = content + '\n' + curr_line

            elif '</DOCHDR>' in curr_line:
                readflag = 1

            elif curr_line == '':
                break

            curr_line = self.fp.readline().strip()

        if docNo != "":
            clean_text = re.sub(self.clean, "", content)
            return [docNo, clean_text]
                    #re.sub(self.clean, "", content)]
        else:
            self.fp.close()
            return