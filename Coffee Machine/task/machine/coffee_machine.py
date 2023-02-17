
class CoffeeMachine():
    EWATER = 250
    EBEANS = 16
    ECOST= 4
    LWATER = 350
    LMILK = 75
    LBEANS = 20
    LCOST = 7
    CWATER = 200
    CMILK = 100
    CBEANS = 12
    CCOST = 6
    CURRWATER = 400
    CURRMILK = 540
    CURRBEANS = 120
    CURRCUPS = 9
    CURRMONEY = 550

    def __init__(self):
        #print("Write how many ml of water the coffee machine has:")
        #self.nWater = int(input())
        #print("Write how many ml of milk the coffee machine has:")
        #self.nMilk = int(input())
        #print("Write how many grams of coffee beans the coffee machine has:")
        #self.nBeans = int(input())
        #print("Write how many cups of coffee you will need:")
        #self.nCups = int(input())
        pass

    def printIngredients(self):
        print(f"For {self.nCups} cups of coffee you will need:")
        print(f'{self.nCups * self.CWATER} ml of water')
        print(f'{self.nCups * self.CMILK} ml of milk')
        print(f'{self.nCups * self.CBEANS} g of coffee beans')

    def checkIngredients(self, water, milk, beans, cost):
        checkWater = self.CURRWATER // water
        checkMilk = self.CURRMILK // milk
        checkBeans = self.CURRBEANS // beans
        checkCups = self.CURRCUPS - 1
        minCup = min([checkWater, checkMilk, checkBeans, checkCups])
        if minCup >= 1:
            print("I have enough resources, making you a coffee!")
            return True
        #if minCup > 1:
            #print(f"Yes, I can make that amount of coffee (and even {minCup - self.nCups} more than that)")
        #if minCup < 1:
            #print(f"No, I can make only {minCup} cups of coffee")
        if checkWater < 1:
            print("Sorry, not enough water!")
            return False
        if checkMilk < 1:
            print("Sorry, not enough milk!")
            return False
        if checkBeans < 1:
            print("Sorry, not enough bean!")
            return False
        if checkCups < 1:
            print("Sorry, not enough cup!")
            return False

    def showOptions(self):
        print("Write action (buy, fill, take, remaining, exit):  ")
        action = input()
        return action

    def showCoffeeChoices(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:  ")
        choice = input()
        return choice

    def showState(self):
        print("The coffee machine has:")
        print(f'{self.CURRWATER} ml of water')
        print(f'{self.CURRMILK} ml of milk')
        print(f'{self.CURRBEANS} g of coffee beans')
        print(f'{self.CURRCUPS} disposable cups')
        print(f'${self.CURRMONEY} of money')

    def buy(self):
        choice = self.showCoffeeChoices()
        if choice == "1":
            res = self.checkIngredients(self.EWATER, self.CURRMILK, self.EBEANS, self.ECOST)
            if res:
                self.CURRWATER -= self.EWATER
                self.CURRBEANS -= self.EBEANS
                self.CURRMONEY += self.ECOST
                self.CURRCUPS -= 1
            else:
                res

        elif choice == "2":
            res = self.checkIngredients(self.LWATER, self.LMILK, self.LBEANS, self.LCOST)
            if res:
                self.CURRWATER -= self.LWATER
                self.CURRMILK -= self.LMILK
                self.CURRBEANS -= self.LBEANS
                self.CURRMONEY += self.LCOST
                self.CURRCUPS -= 1
            else:
                res

        elif choice == "3":
            res = self.checkIngredients(self.CWATER, self.CMILK, self.CBEANS, self.CCOST)
            if res:
                self.CURRWATER -= self.CWATER
                self.CURRMILK -= self.CMILK
                self.CURRBEANS -= self.CBEANS
                self.CURRMONEY += self.CCOST
                self.CURRCUPS -= 1
            else:
                res

        elif choice == "back":
            self.brew()

    def fill(self):
        print("Write how many ml of water you want to add: ")
        self.CURRWATER += int(input())
        print("Write how many ml of milk you want to add: ")
        self.CURRMILK += int(input())
        print("Write how many grams of coffee beans you want to add: ")
        self.CURRBEANS += int(input())
        print("Write how many disposable cups you want to add: ")
        self.CURRCUPS += int(input())
        #self.remaining()

    def take(self):
        print(f'I gave you ${self.CURRMONEY}')
        self.CURRMONEY = 0
        #self.remaining()

    def remaining(self):
        print("The coffee machine has:")
        print(f'{self.CURRWATER} ml of water')
        print(f'{self.CURRMILK} ml of milk')
        print(f'{self.CURRBEANS} g of coffee beans')
        print(f'{self.CURRCUPS} disposable cups')
        print(f'${self.CURRMONEY} of money')

    def exit(self):
        exit()

    def brew(self):
        #self.showState()
        while True:
            action = self.showOptions()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                self.exit()


if __name__ == '__main__':
    CoffeeMachine().brew()
