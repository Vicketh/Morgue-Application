import argparse

parser = argparse.ArgumentParser(description="Morgue Management System")

parser.add_argument("--add", metavar=("name", "age", "primary_contact", "cause_of_death", "date_of_arrival"),
                    nargs=4, help="Add a new body to the system")
parser.add_argument("--update", metavar=("name", "age", "primary_contact","cause_of_death", "date_of_arrival"),
                    nargs=4, help="Update an existing body in the system")
parser.add_argument("--delete", metavar="name", help="Delete a body from the system")
parser.add_argument("--search", metavar=("name", "age", "primary_contact", "cause_of_death", "date_of_arrival"),
                    nargs=4, help="Search for bodies in the system")
parser.add_argument("--display", action="store_true", help="Display all bodies in the system")

args = parser.parse_args()

morgue = Morgue()

if args.add:
    name, age, primary_contact, cause_of_death, date_of_arrival = args.add
    body = Body(name, int(age), primary_contact, cause_of_death, date_of_arrival)
    morgue.add_body(body)
    print(f"Added body: {name}")

if args.update:
    name, age, primary_contact, cause_of_death, date_of_arrival = args.update
    if morgue.update_body(name, int(age), primary_contact, cause_of_death, date_of_arrival):
        print(f"Updated body: {name}")
    else:
        print(f"Error: Body not found: {name}")

if args.delete:
    name = args.delete
    if morgue.delete_body(name):
        print(f"Deleted body: {name}")
    else:
        print(f"Error: Body not found: {name}")

if args.search:
    name, age, primary_contact, cause_of_death, date_of_arrival = args.search
    results = morgue.search_bodies(name, int(age), primary_contact, cause_of_death, date_of_arrival)
    if results:
        print("Search results:")
        for body in results:
            print(f"{body.name}, {body.age}, {body.primary_contact}, {body.cause_of_death}, {body.date_of_arrival}")
    else:
        print("No search results.")

if args.display:
    morgue.display_bodies()