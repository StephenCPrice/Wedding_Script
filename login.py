from __future__ import print_function # In python 2.7
import sys
from user_model import User
from flask import redirect, flash
from bcrypt import checkpw
from flask_login import login_user, current_user, logout_user

def authenticate_user(email, password):
    
    user = User.query.filter_by(email=email).first()
    password = password.encode('utf-8')

    if user is None:
        flash('No user with that email')
        return redirect('/login')

    elif checkpw(password, user.password):
        login_user(user, remember=True)
        flash('it worked!')
        return redirect('/home')

    else:
        flash('Incorrect password')
        return redirect('/login')
