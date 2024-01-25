import numpy as np
class main():
    
    current_board = None

    def make_starting_board(self) -> np.array:
        a = []
        b = []
        for i in range(8):
            a.append(0)
        for i in range(8):
            b.append(a)
        for x in b:
            for y in x:
                if (x.length() <= 2 and x.length() % 2 == 0 and y % 2 == 1):
                    y == -1
                
                elif(x >= 5 and x % 2 == 1 and y % 2 == 0):
                    y == 1
        for i in b:
            print(i)


    def __init__(self) -> None:
        current_board = []
        self.make_starting_board()

a = main()