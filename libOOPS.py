class Library:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.sections = {
            'fantasy': [],
            'fiction': [],
        }
        self.members = []

    def auth(self):
        if self.user == "admin" and self.password == "1234":
            return True
        else:
            return False

    def add_book(self, genre, book_name):
        if genre in self.sections:
            self.sections[genre].append(book_name)
        else:
            print("Invalid genre")

    def show_all_books(self):
        return self.sections

    def add_member(self, card_number, name):
        self.members.append({'card_number': card_number, 'name': name})
        return f"Successfully registered as {name} with {card_number} card Number"


user = input("Enter Your UserName")
password = input("Enter Your Password")
lghive = Library(user.lstrip(), password.lstrip())


if not lghive.auth():
    print("Authentication failed. Exiting.")
    exit()

while True:
    print("1. Enter Books into Sections\n2. Add Members to the Section\n3. Show all books\n4. Exit")

    choice = input("\nEnter Your Choice")

    if choice == "1":
        print("1. Fantasy\n2. Fiction")
        choose = input("Choose the Genre")
        if choose.lstrip() == "1":
            fantasyBooks = input("Enter the Book Name")
            lghive.add_book('fantasy', fantasyBooks.lstrip())
        elif choose.lstrip()== "2":
            fictionBooks = input("Enter the Book Name")
            lghive.add_book('fiction', fictionBooks.lstrip())
        else:
            print("Invalid Choice")
    elif choice.lstrip() == "2":
        cardNumber = input("Enter Your card Number")
        name = input("Enter Your card name")
        print(lghive.add_member(cardNumber, name.lstrip()))
    elif choice.lstrip() == "3":
        print(lghive.show_all_books())
    elif choice.lstrip() == "4":
        exit(0)
    else:
        print("Invalid Choice")
