class Player:
    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name


class BasketballPlayer(Player):
    valid_positions = ['Guard','Forward','Center']
    def __init__(self,name,position):
        Player.__init__(self,name)
        self.__position = position

    def set_position(self,position):
        self.__position = position
    def get_position(self): 
        return self.__position
    
    def __str__(self):
        return f"{self.get_name()} is playing as a {self.get_position()}"
    

players = []

for i in range(5):
    name = input("Enter player's name: ")
    position = input(f"what is he/she playing? ")
    if position not in BasketballPlayer.valid_positions:
        print("Invalid position for a basketball player")
        position = ''
    players.append(BasketballPlayer(name,position))


for player in players:
    print(player)


