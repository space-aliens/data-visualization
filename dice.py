from random import randint

class Dice:
    """Create a Dice instance."""
    def __init__(self, number_of_sides = 8):
        """Initilize Dice instance variables."""
        self.number_of_sides = number_of_sides
    
    def roll_dice(self):
        """Roll the dice and return a number or value."""
        value = randint(1, self.number_of_sides)
        return value
