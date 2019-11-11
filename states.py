import tkinter
import board

class FrameManager:
    def __init__(self):
        self._frame = None
        self.root = tkinter.Tk()
        self.root.geometry("500x400")
        self.root.title("Boggle")
        self.switch_frame(MenuFrame)
        self.root.mainloop()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame.frame
        self._frame.pack(fill='both', expand='true')
        
        

class MenuFrame:
    def __init__(self, frameMng:FrameManager):
        self.frame = tkinter.Frame(frameMng.root, highlightbackground="orange2", highlightthickness=10)
        self.frameMng = frameMng
        
        for i in range(7):
            self.frame.columnconfigure(i,weight=1)
            self.frame.rowconfigure(i, weight=1)

        titleLabel = tkinter.Label(self.frame, fg="black", text="Boggle").grid(row=1, column=3)
        startButton = tkinter.Button(self.frame, background="orange2", text ="New game", command=lambda:self.frameMng.switch_frame(GameFrame), width=25).grid(row=3, column=3, columnspan=1)
        exitButton = tkinter.Button(self.frame, background="burlywood1", text ="Exit", command=exit, width=25).grid(row=4, column=3, columnspan=1)

class GameFrame:
    def __init__(self, frameMng:FrameManager):
        self.frame = tkinter.Frame(frameMng.root, highlightbackground="orange2", highlightthickness=10)
        self.frameMng = frameMng
        self.board = board.Board(4)
        self.board.printAllWords()
        self.label = []
        self.score = 0
        self.timer = {"min":3, "sec":0}

        for i in range(12):
            self.frame.columnconfigure(i,weight=1)
            self.frame.rowconfigure(i, weight=1)

        center =   6 - self.board.size/2
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.label.append( tkinter.Label(self.frame, text=self.board.board[i, j].upper() ).grid(row=int(i+center-1), column=int(j+center)) )


        self.scoreLabel = tkinter.Label(self.frame, text="Score: %03d" % self.score)
        self.timerLabel = tkinter.Label(self.frame, text="Timer: %02d:%02d" % (self.timer["min"], self.timer["sec"]) )
        self.timerLabel.after(1000, self.refreshTimer)

        self.wordsInput = tkinter.Entry(self.frame, width=65)
        self.wordsInput.bind("<Return>", lambda e:self.checkGuessedWord())

        self.scoreLabel.grid(row=0, column=0)
        self.timerLabel.grid(row=0, column=11)
        self.wordsInput.grid(row=10, column=0, columnspan=12)

    def refreshTimer(self):
        if self.timer["min"] == 0 and self.timer["sec"] == 0:
            self.frameMng.switch_frame(MenuFrame)
            return 0

        if self.timer["sec"] == 0:
            self.timer["sec"] = 59
            self.timer["min"] -= 1
        
        else:
            self.timer["sec"] -= 1

        self.timerLabel.configure(text="Timer: %02d:%02d" % (self.timer["min"], self.timer["sec"]) )
        self.timerLabel.after(1000, self.refreshTimer)

    def checkGuessedWord(self):
        if self.board.test.count(self.wordsInput.get()):
            if len(self.wordsInput.get()) >= 8:
                self.score += 11
            elif len(self.wordsInput.get()) == 7:
                self.score += 5
            elif len(self.wordsInput.get()) == 6:
                self.score += 3
            elif len(self.wordsInput.get()) == 5:
                self.score += 2
            else:
                self.score += 1
    
            self.scoreLabel["text"] = "Score: %03d" % self.score
            self.wordsInput.delete(0, tkinter.END)
