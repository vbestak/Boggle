class Words:
    def __init__(self):
        self.__fileName = "words_alpha.txt"
        self.words = {}
        self.__readFile()    
        
    def __readFile(self):
        file = open(self.__fileName, "r")
        
        for line in file:
            if self.words.get(line[0:3], True) == True:
                self.words[line[0:3]] =  [line[:-1]]
            else:
                self.words[line[0:3]].append(line[:-1])
        
        file.close()
        
    def findMatches(self, word):
        count = 0
        length = len(word)
        
        if self.words.get(word[0:3], False) == False:
            return 0
        elif self.words[word[0:3]].count(word):
            return 1
        
        for w in self.words[word[0:3]]:
            if w[:length] == word:
                count += 1
            if count > 2:
                return 2
        
        return 0

# b = Words()
# print(b.words)