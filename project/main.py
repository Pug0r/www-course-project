import sqlalchemy
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from project.models import Course, Lecturer, Opinion
from sqlalchemy import func
from project import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    headers = (
        'Imie', 'Nazwisko', 'Przedmiot', 'Średnia', 'Nastawienie wobec studenta', 'Umiejętność przekazywania wiedzy',
        'Własna inicjatywa, przekazywanie dodatkowych treści', 'Przygotowanie merytoryczne do przedmiotu',
        'Dostosowanie wymagań względem poziomu nauczania')
    results = (db.session.query(
        Lecturer.name,
        Lecturer.surname,
        Course.name,
        func.round(((func.avg(Opinion.nastawienie) +
                     func.avg(Opinion.przekazywanie_wiedzy) +
                     func.avg(Opinion.inicjatywa) +
                     func.avg(Opinion.przygotowanie) +
                     func.avg(Opinion.dostosowanie_wymagan)) / 5), 2),
        func.round(func.avg(Opinion.nastawienie), 2),
        func.round(func.avg(Opinion.przekazywanie_wiedzy), 2),
        func.round(func.avg(Opinion.inicjatywa), 2),
        func.round(func.avg(Opinion.przygotowanie), 2),
        func.round(func.avg(Opinion.dostosowanie_wymagan), 2)
    ).join(
        Course,
        Lecturer.id == Course.lecturer_id
    ).join(
        Opinion,
        Opinion.course_id == Course.id
    ).group_by(
        Lecturer.name,
        Lecturer.surname,
        Course.name
    ).order_by(
        sqlalchemy.desc(func.round((func.avg(Opinion.nastawienie) +
                                   func.avg(Opinion.przekazywanie_wiedzy) +
                                   func.avg(Opinion.inicjatywa) +
                                   func.avg(Opinion.przygotowanie) +
                                   func.avg(Opinion.dostosowanie_wymagan)) / 5, 2))
    ).all())
    return render_template('index.html', headers=headers, data=results)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)
