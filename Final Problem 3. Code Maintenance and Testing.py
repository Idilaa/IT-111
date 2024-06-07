import sqlite3
import csv

conn = sqlite3.connect("test.db")
print("\nDatabase connected.")

##TASK 1: Add one more column to the table. Be sure to adjust all queries to reflect this extra column!

# CREATE A TABLE
conn.execute('''DROP TABLE IF EXISTS CONTACTS''')
conn.execute('''CREATE TABLE IF NOT EXISTS CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL          TEXT);''')
print("Table created.")
conn.close()

##TASK 2: Create an additional test record.

# ADD RECORDS
conn = sqlite3.connect("test.db")
conn.execute("INSERT OR IGNORE INTO CONTACTS (ID,NAME, AGE,ADDRESS, EMAIL) \
      VALUES (10, 'Polly', 32, 'Seattle', 'polly@example.com')");
conn.execute("INSERT or IGNORE INTO CONTACTS (ID,NAME, AGE,ADDRESS, EMAIL) \
     VALUES (11, 'Roger', 28, 'Bainbridge', 'roger@example.com')");
conn.commit()
print("Records created. \n")
conn.close()

# RETRIEVE RECORDS
conn = sqlite3.connect("test.db")
cursor = conn.execute("SELECT * from CONTACTS")
print("RECORDS:")
for row in cursor:
   print ("ID = " + str(row[0]))
   print ("NAME = " + row[1])
   print("AGE = " + str(row[2]))
   print ("ADDRESS = " + str(row[3]))
   print ("EMAIL = " + str(row[4]) + "\n")
conn.close()

##TASK 3: Generalize the query so the user can input a column name.

# USER QUERY FROM CLI
column = input("Enter a column name (ID, NAME, AGE, ADDRESS, or EMAIL): ")
query = input("Enter a query term: ")
conn = sqlite3.connect("test.db")

# Task 4 - Place the query below into a "try: except:" block. The exception should say 'Query not valid'.
try:
    cursor = conn.execute("SELECT * from CONTACTS where " + column + " = '" + query + "'")
    print("\nSELECTED RECORD:")
    for row in cursor:
        print ("ID = " + str(row[0]))
        print ("NAME = " + row[1])
        print("AGE = " + str(row[2]))
        print ("ADDRESS = " + str(row[3]))
        print ("EMAIL = " + str(row[4]) + "\n")
except:
    print("Query not valid.")

conn.close()

# SAVE RECORDS TO A LIST
conn = sqlite3.connect('test.db')
cursor = conn.execute("SELECT * from CONTACTS")
data_list = []
for row in cursor:
   data_list.append(row)
conn.close()
print("RECORDS LIST:")
print(data_list)

# Task 5 - Let the user enter the name of the CSV file for data export.
# Include the selected file name in the final print statement.
file_name = input("Enter the name of the CSV file for data export (e.g., contacts.csv): ")

# SAVE RECORDS TO A CSV FILE
with open(file_name, mode='w') as contact_file:
    contact_writer = csv.writer(contact_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data_list:
        contact_writer.writerow(row)

# Print statement should reflect the user-selected file name.
print("\nCSV EXPORT COMPLETE. Data saved to:", file_name)
