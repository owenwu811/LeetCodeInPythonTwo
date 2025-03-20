
#3484
#medium

#A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

#Implement the Spreadsheet class:

#Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
#void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
#void resetCell(String cell) Resets the specified cell to 0.
#int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
#Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

 

#Example 1:

#Input:
#["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
#[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

#Output:
#[null, 12, null, 16, null, 25, null, 15]


#my own solution using python3:

#lots of trial and error but misread the question but finally got it

class Spreadsheet:

    def __init__(self, rows: int):
        print(rows, "rows")
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.res = []
        for i in range(26):
            cur = []
            for j in range(rows + 1):
                cur.append(0)
            self.res.append(cur)
        #print(self.res)
        #print(len(self.res), len(self.res[0]))

    def setCell(self, cell: str, value: int) -> None:
        number = cell[0]
        val = cell[1:]
        x = self.letters.index(number) 
        y = int(val)
        #print(x, y, value, "setcell")
        #print(len(self.res), len(self.res[0]))
        if x < len(self.res) and y < len(self.res[x]):
            self.res[x][y] = value
            #print(self.res[x][y])
    

    def resetCell(self, cell: str) -> None:
        number = cell[0]
        val = cell[1:]
        x = self.letters.index(number)
        y = int(val)
        #print(x, y)
        self.res[x][y] = 0
        pass

    def getValue(self, formula: str) -> int:
        #print(formula)
        #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 88383, 0, 0, 0, 0, 0, 0, 0]
        f = formula[1:].split("+")
        #print(f)
        #print(len(self.res), "now")
        
        ans = []
        for a in f:
            if a[0] in self.letters:
                print(a, "l")
                number = a[0]
                val = a[1:]
                x = self.letters.index(number) 
                y = int(val) 
                #print(x, y, "x, y")
                #if x < len(self.res):
                    #print(self.res[x])
                if x < len(self.res) and y < len(self.res[0]):
                    #print(self.res[x])
                    ans.append(self.res[x][y])
            else:
                #print(a, "n")
                ans.append(int(a))
        #print(ans)
        return sum(ans)
        
 
 


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
