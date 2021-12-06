class BankAccount:
    """ This represents a classs that creates a BankAccount object """

    def __init__(self, ID, Name, Balance=0.0):
        self.ID = ID
        self.Name = Name
        self.Balance = Balance

    def deposit(self, amount):
        self.Balance += amount

    def withdraw(self, amount):
        if amount > self.Balance:
            raise ValueError("insufficient funds")
        self.Balance -= amount
    
    def transfer(self, other, amount):
        if amount > self.Balance:
            raise ValueError("insufficient funds")        
        self.Balance -= amount
        other.Balance += amount

    def __str__(self):
        return "Account info: " + "ID:" + str(self.ID) + " Name:" + self.Name + " Balance:" + str(self.Balance)  
