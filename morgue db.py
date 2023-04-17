import sqlite3




conn = sqlite3.connect('morgue.db')



c = conn.cursor()

# Create the bodies table
c.execute('''CREATE TABLE bodies
             (name text, age integer, primary_contact text, cause_of_death text, date_of_arrival text)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#add new
import sqlite3

conn = sqlite3.connect('morgue.db')

c = conn.cursor()

# Add a new body to the database
name = 'Isagi Yoichi'
age = 35
primary_contact = 'Nagi Seishiro - Brother'
cause_of_death = 'Car accident'
date_of_arrival = '2023-01-01'

c.execute("INSERT INTO bodies VALUES (?, ?, ?, ?)", (name, age, primary_contact, cause_of_death, date_of_arrival))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#UPDATE EXISTING
import sqlite3

conn = sqlite3.connect('morgue.db')

c = conn.cursor()

# Update an existing body in the database
name = 'Isagi Yoichi'
age = 41
primary_contact = 'Shelly Mwihaki - Spouse'
cause_of_death = 'Drowning'
date_of_arrival = '2023-01-05'

c.execute("UPDATE bodies SET age = ?, primary_contact = ?, cause_of_death = ?, date_of_arrival = ? WHERE name = ?", (age, primary_contact, cause_of_death, date_of_arrival, name))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#***DELETE EXISTING****
import sqlite3

conn = sqlite3.connect('morgue.db')

c = conn.cursor()

# Delete an existing body from the database
name = 'Isagi Yoichi'

c.execute("DELETE FROM bodies WHERE name = ?", (name,))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

#***SEARCH FOR BODIES***
import sqlite3

conn = sqlite3.connect('morgue.db')

c = conn.cursor()

# Search for bodies in the database
name = 'Isagi Yoichi'
age = None
primary_contact = None
cause_of_death = None
date_of_arrival = None

query = "SELECT * FROM bodies WHERE "
params = []

if name:
    query += "name = ? AND "
    params.append(name)
if age:
    query += "age = ? AND "
    params.append(age)
if primary_contact:
    query += "primary_contact = ? AND"
    params.append(primary_contact)
if cause_of_death:
    query += "cause_of_death = ? AND "
    params.append(cause_of_death)
if date_of_arrival:
    query += "date_of_arrival = ? AND "
    params.append(date_of_arrival)

if query.endswith("AND "):
    query = query[:-4]

c.execute(query, tuple(params))

results = c.fetchall()

for row in results:
    print(row)

# Close the connection
conn.close()
import sqlite3
from datetime import datetime

# Function to generate a new unique body ID
def generate_id():
    # Connect to the database
    conn = sqlite3.connect("morgue.db")
    c = conn.cursor()
    
    # Get the highest existing body ID
    c.execute("SELECT MAX(body_id) FROM bodies")
    max_id = c.fetchone()[0]
    
    # Generate a new ID by adding 1 to the highest existing ID
    new_id = max_id + 1 if max_id else 1
    
    # Close the database connection and return the new ID
    conn.close()
    return new_id

# Function to add a new body to the database
def add_body(name, age, gender, date_of_death, date_of_admission, diagnosis, status):
    # Generate a new unique body ID
    body_id = generate_id()
    
    # Connect to the database
    conn = sqlite3.connect("morgue.db")
    c = conn.cursor()
    
    # Insert the new body into the database
    c.execute("INSERT INTO bodies (body_id, name, age, primary_contact, cause_of_death, date_of_death status) VALUES (?, ?, ?, ?, ?, ?, ?)", (body_id, name, age, primary_contact, cause_of_death, date_of_death, status))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
    
    # Return the new body ID
    return body_id

# Function to update the status of a body in the database
def update_status(body_id, status):
    # Connect to the database
    conn = sqlite3.connect("morgue.db")
    c = conn.cursor()
    
    # Update the status of the specified body in the database
    c.execute("UPDATE bodies SET status = ? WHERE body_id = ?", (status, body_id))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Function to add a new invoice to the database
def add_invoice(body_id, amount_due):
    # Generate a new unique invoice ID
    invoice_id = generate_id()
    
    # Get the current date and time
    date_issued = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Connect to the database
    conn = sqlite3.connect("morgue.db")
    c = conn.cursor()
    
    # Insert the new invoice into the database
    c.execute("INSERT INTO invoices (invoice_id, body_id, date_issued, amount_due, paid) VALUES (?, ?, ?, ?, ?)", (invoice_id, body_id, date_issued, amount_due, 0))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
    
    # Return the new invoice ID
    return invoice_id

# Function to mark an invoice as paid in the database
def mark_invoice_paid(invoice_id):
    # Connect to the database
    conn = sqlite3.connect("morgue.db")
    c = conn.cursor()
    
    # Update the specified invoice in the database
    c.execute("UPDATE invoices SET paid = ? WHERE invoice_id = ?", (1, invoice_id))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()


#***example***
mark_invoice_paid(1)  # Mark invoice with ID 1 as paid
