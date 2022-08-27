from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.users import User


@app.route('/users')
def r_users():
    users = User.get_all()
    return render_template('users.html', users=users)


@app.route('/users/create')
def r_create():
    return render_template('create.html')


@app.route('/users/add_user', methods=['POST'])
def add_user():
    inbound = request.form
    data = {
        'first_name' : inbound['first_name'],
        'last_name' : inbound['last_name'],
        'email' : inbound['email_address'],
    }

    User.create(data)

    return redirect('/users')

@app.route('/users/<id>')
def r_user_info(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)

    return render_template('view_user.html', user=user)

@app.route('/users/<id>/edit')
def r_user_edit(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)

    return render_template('edit_user.html', user=user)