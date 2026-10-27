class counter: 
    def __init__(self, gmails= 0, icloud = 0 , hotmail = 0, yahoo = 0, outlooks = 0, ymail = 0, other = 0):
        self.gmails = gmails
        self.outlooks = outlooks
        self.icloud = icloud 
        self.hotmail = hotmail
        self.yahoo =  yahoo
        self.ymail = ymail 
        self.other = other
    def ask_numbers(self, prompt):
        while True:
             try:
                return int(input(prompt))
             except ValueError:
                 print(f"Please enter a valid number") 
    def user_input(self):
        self.gmails = int(input("Gmails: "))
        self.outlooks = int(input("Outlooks:"))
        self.icloud = int(input("Iclouds: "))
        self.hotmail = int(input("Hotmail: "))
        self.yahoo = int(input("Yahoo: "))
        self.ymail = int(input("ymail: "))
        self.other  = int (input("other: "))

class calautor(counter): 
    def __init__(self, gmails=0, icloud=0, hotmail=0, yahoo=0, outlooks=0, ymail=0, other=0):
        super().__init__(gmails, icloud, hotmail, yahoo, outlooks, ymail, other)
        self.calu = 0

    def calulate(self):
        self.calu = (self.gmails + self.icloud + self.hotmail
                     + self.yahoo + self.outlooks + self.ymail + self.other)
        return self.calu / 7  * 100
        