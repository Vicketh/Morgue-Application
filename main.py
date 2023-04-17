from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///morgue.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False) 
    primary_contact  = db.column(db.String(55), nullabble=False)
    cause_of_death = db.Column(db.String(100), nullable=False)
    date_of_arrival = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    bodies = Body.query.all()
    return render_template('index.html', bodies=bodies)

@app.route('/add', methods=['GET', 'POST'])
def add_body():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        primary_contact = request.form['primary_contact']
        cause_of_death = request.form['cause_of_death']
        date_of_arrival = request.form['date_of_arrival']
        new_body = Body(name=name, age=age, primary_contact=primary_contact, cause_of_death=cause_of_death, date_of_arrival=date_of_arrival)
        db.session.add(new_body)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_body(id):
    body = Body.query.get_or_404(id)
    if request.method == 'POST':
        body.name = request.form['name']
        body.age = request.form['age']
        body.primary_contact = request.form['primary_contact']
        body.cause_of_death = request.form['cause_of_death']
        body.date_of_arrival = request.form['date_of_arrival']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', body=body)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_body(id):
    body = Body.query.get_or_404(id)
    db.session.delete(body)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)