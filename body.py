class Body:
    def __init__(self, name, age, id, primary_contact, cause_of_death, date_of_arrival):
        self.name = name
        self.age = age
        self.id = id
        self.primary_contact = primary_contact
        self.cause_of_death = cause_of_death
        self.date_of_arrival = date_of_arrival

class Morgue:
    def __init__(self):
        self.bodies = []
        
    def add_body(self, body):
        self.bodies.append(body)
        
    def update_body(self, name, age, id, primary_contact, cause_of_death, date_of_arrival):
        for body in self.bodies:
            if body.name == name:
                body.age = age
                body.id = id
                body.primary_contact = primary_contact
                body.cause_of_death = cause_of_death
                body.date_of_arrival = date_of_arrival
                return True
        return False
    
    def delete_body(self, name):
        for body in self.bodies:
            if body.name == name:
                self.bodies.remove(body)
                return True
        return False
    
    def search_bodies(self, name=None, age=None, id=None, primary_contact=None, cause_of_death=None, date_of_arrival=None):
        results = []
        for body in self.bodies:
            if name is not None and body.name == name:
                results.append(body)
            elif age is not None and body.age == age:
                results.append(body)
            elif id is not None and body.id == id:
                results.append(body)
            elif primary_contact is not None and body.primary_contact == primary_contact:
                results.append(body)
            elif cause_of_death is not None and body.cause_of_death == cause_of_death:
                results.append(body)
            elif date_of_arrival is not None and body.date_of_arrival == date_of_arrival:
                results.append(body)
        return results
    
    def display_bodies(self):
        for body in self.bodies:
            print(f"{body.name}, {body.age}, {body.id}, {body.primary_contact}, {body.cause_of_death}, {body.date_of_arrival}")
