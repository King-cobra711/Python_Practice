import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)
    
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.origional_value * 1.25
        else:
            self.value = self.origional_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
        one_in_a_mil = [i for i in range(1000001)]
        what_are_the_chances = random.choice(one_in_a_mil)

        if what_are_the_chances == 7:
            print("The coin landed on its side!!!")
        else:
            if self.heads == True:
                print("Heads")
            else:
                print("Tails")
        
    def __del__(self):
        print("Coin spent!")

    def __str__(self):
        if self.origional_value >= 1.00:
            return "${} Coin".format(int(self.origional_value))
        else:
            return "{} cent Coin".format(int(self.origional_value * 100))

class Two_dollar(Coin):

    def __init__(self):
        data = {"origional_value": 2.00, "clean_colour": "Gold", "rusty_colour": "Greenish", "num_edges": 1, "diameter": 20.50, "thickness": 2.80, "mass": 6.60}

        super().__init__(**data)

class One_dollar(Coin):

    def __init__(self):
        data = {"origional_value": 1.00, "clean_colour": "Gold", "rusty_colour": "Greenish", "num_edges": 1, "diameter": 25, "thickness": 2.80, "mass": 9}

        super().__init__(**data)

class Five_cent(Coin):

    def __init__(self):
        data = {"origional_value": 0.05, "clean_colour": "Silver", "rusty_colour": "Greenish", "num_edges": 1, "diameter": 19.41, "thickness": 1.30, "mass": 2.83}

        super().__init__(**data)

class Ten_cent(Coin):

    def __init__(self):
        data = {"origional_value": 0.10, "clean_colour": "Silver", "rusty_colour": "Greenish", "num_edges": 1, "diameter": 23.60, "thickness": 2, "mass": 5.65}

        super().__init__(**data)

class Twenty_cent(Coin):

    def __init__(self):
        data = {"origional_value": 0.20, "clean_colour": "Silver", "rusty_colour": "Greenish", "num_edges": 1, "diameter": 21.75, "thickness": 2.14, "mass": 4}

        super().__init__(**data)

class Fifty_cent(Coin):

    def __init__(self):
        data = {"origional_value": 0.50, "clean_colour": "Silver", "rusty_colour": "Greenish", "num_edges": 12, "diameter": 31.65, "thickness": 2.38, "mass": 15.55}

        super().__init__(**data)

coins = [Two_dollar(), One_dollar(), Fifty_cent(), Twenty_cent(), Ten_cent(), Five_cent()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.mass, coin.num_edges]

    string = "{} - Colour: {}, Value: {}, Diameter: {}, Thickness: {}, Mass: {}, Number of edges: {}".format(*arguments)

    print(string)
