from blog import db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(10),unique=True)
    password = db.Column(db.String(30))
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __repr__(self,username,password):
        return '<User %r>' % self.username