<<<<<<< HEAD
from . import db

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))

=======
from . import db

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))

>>>>>>> c1daa13c026cdd946bd8e6e9a09f8e91c83910e4
