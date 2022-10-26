import mysql
import csv
import mysql.connector
from mysql.connector import errorcode
from csv import reader

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

drop = ('DROP TABLE IF EXISTS food')
drop2 = ('DROP TABLE IF EXISTS pets')

print('Checking tables... ')
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())

print('Dropping tables...')
mycursor.execute(drop)
mycursor.execute(drop2)
print('Tables have been dropped...')

print('Creating tables...')

# CREATE Statement for Table food.

mycursor.execute('CREATE TABLE food (foodid INT AUTO_INCREMENT PRIMARY KEY, good_food TINYINT, bad_food TINYINT, food_name VARCHAR(45), pet_type VARCHAR(45))')
print('food table has been created...')
print('Table creation is complete.')
