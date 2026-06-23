SUITS: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Ace",
]


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank: str = rank
        self.suit: str = suit
        self.rank_index: int = RANKS.index(rank)
        self.suit_index: int = SUITS.index(suit)

    def __eq__(self, other: object) -> bool:
        return (type(self) == type(other)
                and self.rank == other.rank
                and self.suit == other.suit
        ) 

    def __lt__(self, other: "Card") -> bool:
        if (self.rank_index < other.rank_index 
            or (self.rank_index == other.rank_index
                and self.suit_index < other.suit_index)):
            return True
        
        return False

       


    def __gt__(self, other: "Card") -> bool:
        if (self.rank_index > other.rank_index 
            or (self.rank_index == other.rank_index
                and self.suit_index > other.suit_index)):
            return True
        
        return False

    # don't touch below this line

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
