from classes.Database import Database

def get():
    db = Database()
    
    query = db.getAllUsers()
    return query