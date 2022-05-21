class Atm:
    def __init__(self, pinNum, cardNum):
        self.model=pinNum
        self.company=cardNum
        
    def cashwithdrawl(self):
        print("cahs withdrawn")

    def balanceinquiry(self):
        print("balance displayed")


Atm = Atm(1234,9873)
print(Atm.pinNum)
print(Atm.cardNum)
Atm.cashwithdrawl()
Atm.balanceinquiry()