class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self ]
        
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        royalties = [inst.royalties for inst in Contract.all if inst.author == self]
        return sum(royalties)

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else: 
            raise Exception(f"{author} is not an instance of the Author class.")
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception (f"{book} is not an instance of the Book class.")

        if isinstance(date, str):
            self.date = date
        else:
            raise Exception ("Date must be a string")
        
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception ("Royalties must be an integer")
        
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]

