class Words:
    def __init__(self):
        self.__fileName = "words_alpha.txt"
        self.words = []
        self.__readFile()    
        
    def __readFile(self):
        file = open(self.__fileName, "r")
        
        for line in file:
           self.words.append(line[:-1])
        
        file.close()
        
    def findMatches(self, word):
        count = 0
        length = len(word)
        
        if self.words.count(word) and length >= 3:
            return 1
        
        for w in self.words:
            if w[:length] == word:
                count += 1
            if count > 2:
                return 2
        
        return 0
    
