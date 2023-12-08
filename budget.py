class Category:

    def __init__(self, n):
        self.name = n
        self.balance = 0
        self.ledger = []
        self.expense = 0

    def deposit(self, amount, description=''):
        object1 = {"amount": amount, "description": description}
        self.ledger.append(object1)
        self.balance = self.balance + amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            object2 = {"amount": -amount, "description": description}
            self.ledger.append(object2)
            self.balance = self.balance - amount
            self.expense += amount
            return True
        else:
          return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, ins):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + ins.name)
            ins.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return not amount > self.balance

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']
        return title + items + 'Total: ' + str(total)


def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    percentage = []
    totalexpense = 0
    graph = ''
    #for i in range(len(categories)):
        #percentage[i] = categories[i].expense / sum(categories[i].expense) * 100
    #print(sum(categories[i].expense))

    #add the percentage to the list
    for i in categories:
        totalexpense += i.expense
    for i in range(len(categories)):
        percentage.append(int((categories[i].expense / totalexpense * 10)) * 10)

    #add the graph
    for i in range(100, -1, -10):
        graph += str(i).rjust(3) + '| '
        for p in percentage:
            if p >= i:
                graph += 'o  '
            else:
                graph += '   '
        graph += '\n'
      
    #add the dashes
    graph += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    #add the names
    names = []
    for i in range(len(categories)):
        names.append(categories[i].name)
    maxi = max(names, key=len)
    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += '   '
            else:
                nameStr += name[x] + '  '
        if (x != len(maxi) - 1):
            nameStr += '\n'
        graph += nameStr
    
    return title + graph
    

