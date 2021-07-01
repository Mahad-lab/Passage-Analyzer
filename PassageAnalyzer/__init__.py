class PassageAnalyzer:
    def __init__(self, text):
        self.text = text

    def charactersCount(self):
        return len(self.text)

    def charactersWOSCount(self):
        return sum(len(x) for x in self.text.split())

    def wordsCount(self):
        return len([word for word in self.text.split()])

    def spacesCount(self):
        return self.text.count(' ')

    def digitsCounts(self):
        return len([c for c in self.text.split() if c.isdigit()])

    def numbersCounts(self):
        return len([c for c in self.text if c.isnumeric()])

    def sentencesCounts(self):
        return len([x for x in self.text.split('.') if x not in [None, '', ' ']])

    def paragraphCounts(self):
        return len(self.text.split('\n\n'))

    def uniqueCounts(self):
        return len({''.join(w for w in word if w.isalpha()) for word in self.text.split()})

    def minWordLength(self):
        return min([len(x) for x in self.text.split()])

    def maxWordLength(self):
        return max([len(x) for x in self.text.split()])

    def linesCount(self):
        return len(self.text.splitlines())

