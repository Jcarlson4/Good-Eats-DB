import csv
from csv import reader
import mysql.connector
from mysql.connector import errorcode

#Connection to the MYSQL Database.
db = mysql.connector.connect(
    host = 'localhost',
    user = 'joseph',
    passwd = '!',
    database = 'goodeatsdb'
)
print('Connection Successfully made')

#Set up cursor for database manipulation.
mycursor = db.cursor()

#Insert all the data from the safe foods csv file into the food table in MYSQL.

with open (r'C:\Users\josep\Documents\School Work Spring 2022\Learning Python\module3new\foodsfordb.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    
    stmt = ('INSERT INTO food'
    '(good_food,bad_food,food_name,pet_type)'
    "VALUES"
    "(%s,%s,%s,%s)")

    for row in csv_reader:
        mycursor.execute(stmt, row)

    print('Inserting...')

    db.commit()

    mycursor.close()

    db.close()

    print('Insertion successful')
