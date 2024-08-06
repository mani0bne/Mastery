from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'

db = SQLAlchemy(app)

# Give id's
class Admin(db.Model):
    
    loginEmail = db.Column(db.String(100), primary_key = True, nullable = False)
    loginPassword = db.Column(db.String(100), nullable= False)

with app.app_context():
    db.create_all()

# give name in the request.get()
@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":    
        admin_loginEmail = request.form.get('email')
        admin_loginPassword = request.form.get('password')

#Mention the id of the input form here

        admin = Admin(
            loginEmail = admin_loginEmail,
            loginPassword = admin_loginPassword
        )

        db.session.add(admin)
        db.session.commit()
        return redirect('/')
    
    else:
        allTasks = Admin.query.all()
        print(allTasks)
        return render_template('index.html', allTasks=allTasks)

        
    




if __name__ == "__main__":
    app.run(debug=True)