import mysql
from mysql.connector import errorcode
import mysql.connector


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

# READ Statements: Foods safe for cats.
print('Safe for cats')
mycursor.execute('SELECT food_name FROM food WHERE good_food = 1 and pet_type = "cat"')
print(mycursor.fetchall())

print('Safe for dogs')
mycursor.execute('SELECT food_name FROM food WHERE good_food = 1 and pet_type = "dog"')
print(mycursor.fetchall())

# UPDATE statements:
#print('Correcting query...')
#mycursor.execute('UPDATE food SET bad_food = 1 WHERE food_name = "chocolate"')
#mycursor.execute ('UPDATE food SET good_food = 0 WHERE food_name = "chocolate"')
#db.commit()
#print('Query Updated')

# DELETE Statement.
#print('Deleting row...')
#mycursor.execute('DELETE FROM food WHERE pet_type = "fish" ')
#db.commit()
#print('Row deleted.')

# INSERT Statement:
#print('Inserting into database...')
#mycursor.execute('INSERT INTO food (good_food,bad_food,food_name,pet_type) VALUES (%s,%s,%s,%s)',(1,0,"popcorn","dog"))
#db.commit()
#print('Insertion made.')