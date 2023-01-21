import persistence
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
            # splittedline[1] = number of products sold/acquired
            # splittedline[2] = employeeID
            # splittedline[3] = date
            product = repo.products.find(id=splittedline[0])[0]
            if int(product.quantity) + int(splittedline[1]) < 0 or splittedline[1] == 0:
                continue
            else:

                product.quantity = int(product.quantity) + int(splittedline[1])
                repo.updateProductsQuantity(product.id, product.quantity)
                new_activity = persistence.Activitie(product_id=product.id, quantity=splittedline[1],
                                                     activator_id=splittedline[2],
                                                     date=splittedline[3])
                repo.activities.insert(new_activity)

            # print("The product we are trying to change is" + repo.products.find(int(splittedline[0])) + " its quantity is : ")


if __name__ == '__main__':
    main(sys.argv)
