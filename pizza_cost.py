#!usr/bin/env/python3
# Made by Jaydin Madore
# Made on 2022-10-02
# this program ask for the diameter of a pizza. it uses the diameter to calculate the total #cost of the pizza with tax and displays it to the user.
import constants 


def main():
    # input
    diameter = float(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("the total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
