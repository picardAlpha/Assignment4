class employee(object):
    # TODO: implement
    def __init__(self, id, name, salary, branche):
        self.id = id
        self.name = name
        self.salary = salary
        self.branch = branche



class supplier(object):
    # TODO: implement
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

    pass


class product(object):
    # TODO: implement
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity
    pass


class branche(object):
    # TODO: implement
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class activitie(object):
    # TODO: implement
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

