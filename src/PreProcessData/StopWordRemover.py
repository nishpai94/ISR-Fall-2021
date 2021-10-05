import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        self.stopword_file = open(Path.StopwordDir, 'r', encoding='utf-8')
        self.stopWord_list = self.stopword_file.read().splitlines()
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        if word in self.stopWord_list:
            return True
        else:
            return False
