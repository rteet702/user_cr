from flask import render_template
from flask_app import app


@app.route('/users')
def r_users():
    return render_template('users.html')