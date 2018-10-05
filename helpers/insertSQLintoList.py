from database import db

# Here you pass the table and the dict base where it will insert the database info.
# for example:
# User is a table already created
# users = []
# insertToList(User,users)




def insertSQLintoList(table,list):
    for i in db.session.query(table).all():
            del i.__dict__['_sa_instance_state']
            list.append(i.__dict__)