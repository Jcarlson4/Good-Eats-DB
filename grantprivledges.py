import mysql.connector
from mysql.connector import errorcode

#Connection to the MYSQL Database.
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'goodeatsdb'
)
print('Connection Successfully made')

#Set up cursor for database manipulation.
mycursor = db.cursor()

print('Granting privledges to joseph...')
mycursor.execute("Grant ALL on goodeatsdb TO joseph@localhost")
mycursor.execute('GRANT CREATE,ALTER,DROP ON goodeatsdb.* TO joseph@localhost')
mycursor.execute('GRANT SELECT, INSERT,UPDATE,DELETE ON goodeatsdb.* TO joseph@localhost')
print('Privledges granted... ')
