class DifferentBanks(Exception):
    pass

class SameAccount(Exception):
    pass

class InsufficientFunds(Exception):
    pass

class Account:
    def __init__(self, bank, id):
        self.bank = bank
        self.id = id

    @property
    def balance(self):
        return self.bank.get_balance(self.id)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.bank == other.bank
            and self.id == other.id
        )

class Bank:
    #TODO: Implement the Bank class
    def __init__(self):
        self.accounts = {}
        self.transfer_log = []
    def create_account(self, balance=0):
        account_id = len(self.accounts) + 1
        account = Account(self,account_id)
        self.accounts[account_id] = balance
        return account

    def get_balance(self, account_id):
        return self.accounts.get(account_id, 0)

    def set_balance(self, account_id, amount):
        self.accounts[account_id] = amount

    def transfer(self, from_account, to_account, amount):
        # Check if both accounts are in the same bank
        if from_account.bank != to_account.bank:
            raise DifferentBanks("Cannot transfer between different banks.")
        
        # Check if the transfer is between the same account
        if from_account == to_account:
            raise SameAccount("Cannot transfer to the same account.")

        # Check if the sender has enough funds
        if from_account.balance < amount:
            raise InsufficientFunds("Insufficient funds for the transfer.")
        
        # Perform the transfer
        from_account_id = from_account.id
        to_account_id = to_account.id

        from_balance = from_account.balance
        to_balance = to_account.balance

        # Update balances
        self.set_balance(from_account_id, from_balance - amount)
        self.set_balance(to_account_id, to_balance + amount)
        
        # Log the transaction
        self.transfer_log.append((from_account, to_account, amount))
