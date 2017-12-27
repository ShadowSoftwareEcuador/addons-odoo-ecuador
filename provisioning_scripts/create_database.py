import erppeek

server = 'http://localhost:8069'
database = 'shadow'
admin_password = 'admin'
user_password = 'odoo'
lang = 'es_EC'

client = erppeek.Client(server=server)

if not database in client.db.list():
    print("The database does not exist yet, creating one!")
    client.create_database(admin_password, database, demo=False, lang=lang, user_password=user_password)
    print("The database was created...!")
else:
    print("The database " + database + " already exists.")
