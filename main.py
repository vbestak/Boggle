import random
import time

class Board:
    def __init__(self, size):
        self.size = size
        self.board = {}
        self.test = []
        self.shuffleBoard()
    
    def shuffleBoard(self):
        abc = "abcčćdđefghijklmnoprsštuvzž"
        random.seed(time.time())
        
        #preradi tako da oko 40% slova budu samoglasnici
        for i in range(self.size):
            for j in range(self.size):
                self.board[i, j] = abc[random.randint(0, len(abc) - 1)]
                
        self.findWords()
    
    def findWords(self):
        for i in range(self.size):
            for j in range(self.size):
                self.__findWords([i, j])
    
    def __findWords(self, currentLetter = [0, 0], used = (), currentWord = ""):
        used += (currentLetter,)
        currentWord += self.board[currentLetter[0], currentLetter[1]]
        self.test.append(currentWord)
        
        corners = self.getCorners(currentLetter)
        cornerUp = corners[0]
        cornerDown = corners[1]
        
       #sad imam sve mogucnosti skretanja
        for i in range(cornerUp[0], cornerDown[0] + 1):
            for j in range(cornerUp[1], cornerDown[1] + 1):
                if [i, j] in used:
                    continue
                #print(i, end=" ")
                #print(j, end=" ")
                #print(self.board[i, j])
                
                if len(currentWord) == self.size*2:
                    return
                
                #print(currentWord)
                self.__findWords([i, j], used, currentWord)
                
    def getCorners(self, letter:[2]):
        cornerUp = [letter[0]-1, letter[1]-1]
        cornerDown = [letter[0]+1, letter[1]+1]
        
        if cornerUp[0] < 0:
            cornerUp[0] = 0
            
        if cornerUp[1] < 0:
            cornerUp[1] = 0
            
        if cornerDown[0] > self.size - 1:
            cornerDown[0] = self.size - 1
            
        if cornerDown[1] > self.size - 1:
            cornerDown[1] = self.size - 1
            
        return [cornerUp, cornerDown]
    
    def drawBoard(self):
        print("")
        for i in range(self.size):
            if i >= 1:
                print("");
            
            for j in range(self.size):
                print(self.board[i, j], end = ' ')


b = Board(5)
b.drawBoard()

