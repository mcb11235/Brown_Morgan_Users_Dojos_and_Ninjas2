from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.user import User
@app.route("/dojos")
def dojos():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)
@app.route("/dojos/<id>")
def show_dojo(id):
    data = {
        "id":id
    }
    try:
        dojo = Dojo.get_one(data)
    except:
        print("No Users Found For This Dojo")
    else:
        user = dojo.users
        return render_template("show_dojo.html", dojo = dojo, users=user)
@app.route("/create_dojo", methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    x = Dojo.save(data)
    return redirect('/dojos')
