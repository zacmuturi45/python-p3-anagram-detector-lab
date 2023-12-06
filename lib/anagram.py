# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, listy):
        new_word = []
        clean_word = []
        m = 0
        while m < len(listy):
            for wor in self.word:
                if wor in listy[m]:
                    new_word.append(wor)
            if len(new_word) == len(self.word):
                clean_word.append(listy[m])
            new_word = []
            m = m + 1
        return clean_word
