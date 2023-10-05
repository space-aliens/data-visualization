import plotly.express as px

from dice import Dice


def create_rolled_data(**dices):
    rolled_data = []
    # Rolled all three D6 1_000 Times
    for i in range(1_000):
        dice_value = 0

        # Loop Throught the dices.
        for value in dices.values():
            dice_value += value.roll_dice()
        rolled_data.append(dice_value)

    return rolled_data    

def main():
    """Main Function of Program."""    

    # Create Three D6
    d6_1 = Dice(number_of_sides=6)
    d6_2 = Dice(number_of_sides=6)
    d6_3 = Dice(number_of_sides=6)

    rolled_data = create_rolled_data(d1=d6_1, d2=d6_2, d3=d6_3)

    max_value = d6_1.number_of_sides + d6_2.number_of_sides + d6_3.number_of_sides

    dice_values = range(3, max_value + 1)

    # Number of time values comes in rolled_data.
    dice_values_data = [rolled_data.count(value) for value in dice_values]


    labels = {'x':"Dice Values", 'y':"Dice Values Data"}

    fig = px.bar(x=dice_values, y=dice_values_data, title="Bar of Three D6 Rolled 1_000 Times", labels=labels)
    fig.update_layout(xaxis_dtick=1)
    fig.show()

if __name__ == "__main__":
    main()