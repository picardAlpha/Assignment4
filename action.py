from persistence import *

import sys


def main(args: list[str]):
    inputfilename: str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(", ")
            # TODO: apply the action (and insert to the table) if possible
            # TODO: check if the action can be performed, meaning there is enough quantity etc
            # splittedline[0] = productID
            # splittedline[1] = number of unit sold/acquired
            # splittedline[2] = employeeID
            # splittedline[3] = date
            product = repo.products.find(id=splittedline[0])[0]
            if product.quantity + splittedline[1] < 0 or splittedline[1] == 0:
                continue
            else

            # print("The product we are trying to change is" + repo.products.find(int(splittedline[0])) + " its quantity is : ")


if __name__ == '__main__':
    main(sys.argv)
