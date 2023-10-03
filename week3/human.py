class Human:
    ## attributes / properties
    number_of_legs = 0
    number_of_hands = 0
    energy = 0
    eyes = 0
    mouth = 0
    jumping_ability = False
    number_of_ears = 0 
    nostril = 0  
    name = "" 

    def clap(self):
        available_hands = self.number_of_hands
        return available_hands

# constructor
    def __init__(self, name, eyes, number_of_legs, number_of_hands, number_of_ears, mouth):
        self.name = name
        self.eyes = eyes
        self.number_of_legs = number_of_legs
        self.number_of_hands = number_of_hands
        self.number_of_ears = number_of_ears
        self.mouth = mouth
      

stanley = Human("stanley", 2, 2, 2, 2, 1)
dice = Human("dice", 1, 1, 0, 0,1)
print(f"{stanley.name} is my name and I have {stanley.clap()} hands")
print(f"{dice.name} is {stanley.clap()}")
