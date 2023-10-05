import matplotlib.pyplot as plt 
from dice import Dice
from three_d6_visualization import create_rolled_data

def main():
    """Main Function of Programmer."""
    
    # Create a D6
    d6_1 = Dice(number_of_sides=6)
    d6_2 = Dice(number_of_sides=6)

    # Rolled Data
    rolled_data = create_rolled_data(d1=d6_1, d2=d6_2)

    
    max_value = d6_1.number_of_sides + d6_2.number_of_sides

    # Dice Values
    dice_values = [value for value in range(1, max_value+1)]

    # Dice Values Data
    # How many time a value occure in rolled_data.
    frequencey = []
    for value in dice_values:
        number_of_time = rolled_data.count(value)
        frequencey.append(number_of_time)




    plt.style.use('classic')
    fig , ax = plt.subplots(figsize=(8, 7))
    ax.plot(dice_values, frequencey, color = "red", linewidth=3)

    # Set Label and Title
    ax.set_title("Graph of 1000 Time Rolled Dice.", fontsize=12)
    ax.set_xlabel("Dice Values", fontsize=12)
    ax.set_ylabel("Dice Value Data", fontsize=12)

    # Equal Aspect 
    # ax.set_aspect('equal')

    # Scatter Plot
    ax.scatter(x=dice_values, y=frequencey, c=frequencey, cmap=plt.cm.Blues, s=100, edgecolor='none' )

    plt.show()




if __name__ == "__main__":
    main()
