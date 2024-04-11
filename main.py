import random

# Define constants
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = [str(i) for i in range(1, 14)]
NUM_COLUMNS = 7

# Initialize the deck
def initialize_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            card = rank + " of " + suit
            deck.append(card)
    random.shuffle(deck)
    return deck

# Deal cards to tableau
def deal_cards(deck):
    tableau = [[] for _ in range(NUM_COLUMNS)]
    for i in range(NUM_COLUMNS):
        for j in range(i + 1):
            card = deck.pop()
            if j == i:
                tableau[i].append(card)
            else:
                tableau[i].append("Face Down")
    return tableau

# Display the current state of the game
def display_game(deck, tableau, foundation):
    print("Main Deck:")
    print(f"Remaining cards: {len(deck)}")
    print("\nTableau:")
    for i, column in enumerate(tableau):
        print(f"Column {i + 1}: ", end="")
        for card in column:
            print(card, end=", ")
        print()
    print("\nFoundation:")
    for suit, cards in foundation.items():
        print(f"{suit}: ", end="")
        for card in cards:
            print(card, end=", ")
        print()

# Move cards from source to destination (considering multiple cards)
def move_cards(source, destination, num_cards):
    valid_move = True
    if len(source) < num_cards:
        valid_move = False
    if valid_move:
        for _ in range(num_cards):
            card = source.pop()
            destination.append(card)
    else:
        print("There are not enough cards in the source column.")

# Check if the game is won
def is_won(foundation):
    return all(len(cards) == 13 for cards in foundation.values())

# Draw a card from the main deck
def draw_card(deck):
    if deck:
        return deck.pop()
    else:
        print("Main deck is empty.")
        return None

# Play the Solitaire game
def play_solitaire():
    deck = initialize_deck()
    tableau = deal_cards(deck)
    foundation = {suit: [] for suit in SUITS}

    while True:
        display_game(deck, tableau, foundation)
        print("\n1. Move cards from tableau to tableau")
        print("2. Move card from tableau to foundation")
        print("3. Draw a card from the main deck and decide whether to add to tableau or not")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            source_col = int(input("Enter source column number (1-7): ")) - 1
            if source_col < 0 or source_col >= NUM_COLUMNS:
                print("Invalid column number. Try again.")
                continue
            source_pile = tableau[source_col]
            if not source_pile or source_pile[-1] == "Face Down":
                print("Column is empty or the card is face down. Try again.")
                continue
            dest_col = int(input("Enter destination column number (1-7): ")) - 1
            if dest_col < 0 or dest_col >= NUM_COLUMNS:
                print("Invalid column number. Try again.")
                continue
            dest_pile = tableau[dest_col]
            num_cards = int(input("Enter the number of cards to move: "))
            # Check for valid number of cards to move
            if num_cards <= 0 or (source_pile[-num_cards] == "Face Down" and num_cards > 1):
                print("Invalid number of cards to move. You cannot move face-down cards alone.")
                continue 
            move_cards(source_pile, dest_pile, num_cards)
        elif choice == "2":
            # (Rest of code for moving to foundation remains the same)
            # ...
            pass
        elif choice == "3":
            drawn_card = draw_card(deck)
            if drawn_card:
                print(f"Drawn card: {drawn_card}")
                decision = input("Do you want to add this card to the tableau? (y/n): ")
                if decision.lower() == "y":
                    dest_col = int(input("Enter destination column number (1-7): ")) - 1
                    if dest_col < 0 or dest_col >= NUM_COLUMNS:
                        print("Invalid column number. Try again.")
                        continue
                    dest_pile = tableau[dest_col]
                    dest_pile.append(drawn_card)

# Start the game
play_solitaire()
