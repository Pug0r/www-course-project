import sqlalchemy
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Course, Lecturer, Opinion
from sqlalchemy import func
from app import db

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
    headers = (
        'Imie', 'Nazwisko', 'Przedmiot', 'Nastawienie wobec studenta', 'Umiejętność przekazywania wiedzy',
        'Własna inicjatywa, przekazywanie dodatkowych treści', 'Przygotowanie merytoryczne do przedmiotu',
        'Dostosowanie wymagań względem poziomu nauczania')
    user_opinions = (db.session.query(
        Lecturer.name,
        Lecturer.surname,
        Course.name,
        Opinion.nastawienie,
        Opinion.przekazywanie_wiedzy,
        Opinion.inicjatywa,
        Opinion.przygotowanie,
        Opinion.dostosowanie_wymagan
    ).join(
        Course,
        Course.id == Opinion.course_id
    ).join(
        Lecturer,
        Lecturer.id == Course.lecturer_id
    ).where(Opinion.user_id == current_user.id).all())
    user_opinions_id = list(map(lambda x: int(x[0]), db.session.query(Opinion.course_id).where(Opinion.user_id == current_user.id).all()))
    lecturers_to_opinion = (db.session.query(Lecturer.name, Lecturer.surname)
                            .join(Course, Lecturer.id == Course.lecturer_id)
                            .filter(~Course.id.in_(user_opinions_id)).all())
    return render_template('profile.html', username=current_user.username,
                           opinions=user_opinions, headers=headers, add_opinion_on=lecturers_to_opinion)


@main.route('/get_lecturer_courses', methods=['POST'])
@login_required  # delete if doesn't work
def get_lecturer_courses():
    name, surname = request.form['selected_lecturer'].split()
    data = (db.session.query(Course.name).join(Lecturer, Lecturer.id == Course.id)
            .where(Lecturer.name == name, Lecturer.surname == surname).all())
    data = [tuple(row) for row in data]  # returned by db aren't json serializable
    return jsonify(data)



@main.route('/submit_opinion', methods=['POST'])
@login_required
def add_new_opinion():
    # Verification is done on html side
    # TODO: add some feedback to user
    lecturer_name, lecturer_surname = request.form['lecturer'].split()
    course_id = (db.session.query(Course.id).join(Lecturer, Course.lecturer_id == Lecturer.id)
                 .where(Lecturer.name == lecturer_name, Lecturer.surname == lecturer_surname, Course.name == request.form['course'])).scalar()
    print(course_id)
    opinion = Opinion(user_id=current_user.id,
                      course_id=course_id,
                      nastawienie=int(request.form['nastawienieRadio']),
                      przekazywanie_wiedzy=int(request.form['przekazywanieRadio']),
                      inicjatywa=int(request.form['inicjatywaRadio']),
                      przygotowanie=int(request.form['przygotowanieRadio']),
                      dostosowanie_wymagan=int(request.form['dostosowanieRadio']),
                      comment=request.form['comment'])  # you shouldve been passing IDs around:)) think for the future!!
    db.session.add(opinion)
    db.session.commit()
    return redirect(url_for('main.profile'))


@main.route('/get_comments', methods=['GET'])
@login_required
def get_comments():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('limit', 5))
    comments = ((db.session.query(Opinion.nastawienie,
                                  Opinion.przekazywanie_wiedzy,
                                  Opinion.inicjatywa,
                                  Opinion.przygotowanie,
                                  Opinion.dostosowanie_wymagan,
                                  Opinion.comment,
                                  Course.name,
                                  Lecturer.name,
                                  Lecturer.surname,
                                  User.username)
                 .join(Course, Opinion.course_id == Course.id)
                 .join(Lecturer, Course.lecturer_id == Lecturer.id))
                .join(User, Opinion.id == User.id).offset((page-1)*per_page).limit(page*per_page).all())
    comments = [{'nastawienie': com[0],
                 'przekazywanie': com[1],
                 'inicjatywa': com[2],
                 'przygotowanie': com[3],
                 'dostosowanie': com[4],
                 'comment': com[5],
                 'course_name': com[6],
                 'lecturer_name': ' '.join(com[7:9]),
                 'username': com[9]} for com in comments]
    return jsonify(comments)


@main.route('/comments')
@login_required
def display_comments():
    return render_template('comments.html')
