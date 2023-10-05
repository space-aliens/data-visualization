import plotly.express as px

from dice import Dice

def main():
    """Main Function of Program."""
    number_of_time_rolled = 1_000

    # Create Two D8
    d8_1 = Dice()
    d8_2 = Dice()

    # Data of dice rolled 1_000 Times
    rolled_data = []

    # Two D8 rolled Thousand Times.
    for i in range(number_of_time_rolled):
        value = d8_1.roll_dice() + d8_2.roll_dice()
        rolled_data.append(value)


    max_value = d8_1.number_of_sides + d8_2.number_of_sides

    # Dice values
    dice_values = list(range(2, max_value + 1))
    
    # How many time each value comes in rolled_data
    dice_values_data = []

    for value in dice_values:
        number_of_times = rolled_data.count(value)
        dice_values_data.append(number_of_times)


    labels = {'x':"Dice Values", 'y':"Dice Values Data"}
    fig = px.bar(x=dice_values,y=dice_values_data, title="Bar of Two D8 Rolled 1_000 Times", labels=labels )

    # Equal spaceing between bars
    fig.update_layout(xaxis_dtick=1)

    # print(rolled_data)    
    fig.show()



if __name__ == "__main__":
    main()   