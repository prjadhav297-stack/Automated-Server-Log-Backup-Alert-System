import mysql.connector, sys, configparser

config = configparser.ConfigParser()
config.read('config.ini')

db = mysql.connector.connect(
    host=config['MYSQL']['host'],
    user=config['MYSQL']['user'],
    password=config['MYSQL']['password'],
    database=config['MYSQL']['database']
)
cursor = db.cursor()

file_name = sys.argv[1]
status = sys.argv[2]

query = "INSERT INTO backups (file_name, status) VALUES (%s, %s)"
cursor.execute(query, (file_name, status))
db.commit()

cursor.close()
db.close()
print("DB_INSERT_SUCCESS")

