from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# connecting to database
app.config[app.config ['SQLALCHEMY_DATABASE_URI']='postgresql://DB_USER:80561@localhost/demoDB']
db = SQLAlchemy(app)

#Defien db model
class Data (db.Model):
    _tablename_= "data"
    id=db.Column(db.Integer, primaary_key= True)
    email = db.Column(db.String(120), unique = "True")
    username = db.Column(db.String(120))

    def_init_(self,email,username):
    self.email = email
    self.username = username


@app.route("/")

def hello():
    return render_template("checkbox.html")

#get information from your form checkout.html, when the submit button is click
@app.route('/', methods=['POST'])
def thankyou():
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        print(request.form)
    return render_template('thankyou.html')

#last step: commit
data = Data(email,username)
db.session.add(data)
db.session.commit() #execute

if __name__ == "__main__":
    app.debug=True
    app.run()
