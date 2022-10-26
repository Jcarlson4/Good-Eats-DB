import mysql.connector
from mysql.connector import errorcode

#Connection to the MYSQL Database.
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)
print('Connection Successfully made')

#Set up cursor for database manipulation.
mycursor = db.cursor()

print('Creating database...')
mycursor.execute('CREATE DATABASE goodeatsdb')
print('Database created successfully...')