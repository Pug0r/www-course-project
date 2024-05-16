from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


def create_table():
    headers = ('h1', 'h2', 'h3')
    data = (('uno', 'dos', 'tres'), ('raz', 'dwa', 'trzy'))
    pass


headers = ('Imie', 'Nazwisko', 'Przedmiot')
data = (('Krzysztof', 'Kutt', 'Linux'), ('Barbara', 'Lewandowska', 'AM2'))


@main.route('/')
def index():
    return render_template('index.html', headers=headers, data=data)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)