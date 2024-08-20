import datetime

class AuctionItem:
    def __init__(self, title, description, min_bid, start_time, end_time):
        self.title = title
        self.description = description
        self.min_bid = min_bid
        self.start_time = start_time
        self.end_time = end_time
        self.highest_bid = 0
        self.highest_bidder = None

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuctionSystem:
    def __init__(self):
        self.users = {}
        self.auctions = {}
        self.logged_in_user = None

        # Predefined auctions
        self.auctions[1] = AuctionItem(
            "Antique Vase", "A rare antique vase from the Ming dynasty.", 1000,
            datetime.datetime(2024, 8, 20, 10, 0, 0),
            datetime.datetime(2024, 8, 21, 10, 0, 0)
        )
        self.auctions[2] = AuctionItem(
            "Vintage Guitar", "A classic Gibson Les Paul guitar from 1960.", 1500,
            datetime.datetime(2024, 8, 20, 11, 0, 0),
            datetime.datetime(2024, 8, 21, 11, 0, 0)
        )
        self.auctions[3] = AuctionItem(
            "Luxury Watch", "A Rolex Submariner watch, in mint condition.", 5000,
            datetime.datetime(2024, 8, 20, 12, 0, 0),
            datetime.datetime(2024, 8, 21, 12, 0, 0)
        )

    def register_user(self, username, password):
        if username in self.users:
            print("User already exists!")
            return
        self.users[username] = User(username, password)
        print("User registered successfully!")

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.logged_in_user = username
            print("Login successful!")
        else:
            print("Invalid credentials!")

    def create_auction(self, title, description, min_bid, start_time, end_time):
        if not self.logged_in_user:
            print("You must be logged in to create an auction.")
            return

        auction_id = len(self.auctions) + 1
        self.auctions[auction_id] = AuctionItem(
            title, description, min_bid, start_time, end_time
        )
        print(f"Auction created successfully with ID {auction_id}!")

    def place_bid(self, auction_id, amount):
        if not self.logged_in_user:
            print("You must be logged in to place a bid.")
            return
        
        if auction_id not in self.auctions:
            print("Auction not found!")
            return

        auction = self.auctions[auction_id]
        now = datetime.datetime.now()
        if now < auction.start_time or now > auction.end_time:
            print("Auction not available!")
            return

        if amount <= auction.highest_bid or amount < auction.min_bid:
            print("Bid too low!")
            return

        auction.highest_bid = amount
        auction.highest_bidder = self.logged_in_user
        print(f"Bid placed successfully! Current highest bid: {amount}")

    def show_auctions(self):
        if not self.auctions:
            print("No auctions available.")
            return
        
        for id, auction in self.auctions.items():
            print(f"ID: {id}")
            print(f"Title: {auction.title}")
            print(f"Description: {auction.description}")
            print(f"Minimum Bid: {auction.min_bid}")
            print(f"Start Time: {auction.start_time}")
            print(f"End Time: {auction.end_time}")
            print(f"Highest Bid: {auction.highest_bid}")
            print(f"Highest Bidder: {auction.highest_bidder}")
            print()

def main():
    system = AuctionSystem()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Create Auction")
        print("4. Place Bid")
        print("5. Show Auctions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login_user(username, password)
        elif choice == '3':
            title = input("Enter auction title: ")
            description = input("Enter auction description: ")
            min_bid = float(input("Enter minimum bid amount: "))
            start_time = datetime.datetime.strptime(input("Enter start time (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(input("Enter end time (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            system.create_auction(title, description, min_bid, start_time, end_time)
        elif choice == '4':
            auction_id = int(input("Enter auction ID: "))
            amount = float(input("Enter bid amount: "))
            system.place_bid(auction_id, amount)
        elif choice == '5':
            system.show_auctions()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
