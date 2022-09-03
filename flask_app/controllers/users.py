from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.dojo import Dojo
@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", all_users = users)
@app.route("/users/<id>")
def show(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template("show_user.html", user = user)

@app.route("/new")
def user_form():
    dojos = Dojo.get_all()
    dojos_list = []
    for dojo in dojos:
        dojos_list.append([dojo.id, dojo.name])
    print(dojos_list)
    return render_template('new_user.html', dojos = dojos_list)
@app.route("/users/<id>/edit")
def edit_user(id):
    data = {
        "id": id
    }    
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)
@app.route("/users/<id>/destroy")
def delete_user(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/users')

@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo"]
    }
    User.save(data)
    x = data['dojo_id']
    return redirect(f'/dojos/{x}')
@app.route("/update_user", methods=['POST'])
def update_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id": request.form["id"]
    }    
    User.update(data)
    return redirect(f'/users/{data["id"]}')