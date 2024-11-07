class Monster:
    def __init__(self,name,heath,attack,defense):
        self.__name = name
        self.__health = heath
        self.__attack = attack
        self.__defense = defense


    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_health(self,health):
        self.__health = health
    def get_health(self):
        return self.__health
    def set_attack(self,attack):
        self.__attack = attack
    def get_attack(self):
        return self.__attack
    def set_defense(self,defense):
        self.__defense = defense
    def get_defense(self):
        return self.__defense
    
    def __str__(self):
        return f"{self.get_name()} is a Monster"
    
class FireMonster(Monster):
    def __init__(self):
        Monster.__init__('firebug',10,9,4)
