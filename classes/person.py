class Person:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return "Person('{}','{}','{}','{}')".format(self.first_name, self.last_name,self.email,self.phone_number)

    def __str__(self):
        return "Person: {},{},{},{}".format(self.first_name, self.last_name,self.email,self.phone_number)

