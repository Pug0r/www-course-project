from project import db
from sqlalchemy import text
from werkzeug.security import generate_password_hash

queries_to_call_on = {
    'user': {
        'query': "INSERT INTO user (username, email, password_hash) VALUES (:username, :email, :password);",
        'params': [
            {'username': 'Aleksander Pugowski', 'email': 'alekp16@gmail.com', 'password': generate_password_hash('123')},
            {'username': 'admin', 'email': 'admin@gmail.com', 'password': generate_password_hash('123')},
            {'username': 'user123', 'password': generate_password_hash('ex'), 'email': 'uniquemail1@gmail.com'},
            {'username': 'user456', 'password': generate_password_hash('ex'), 'email': 'uniquemail2@gmail.com'},
            {'username': 'user789', 'password': generate_password_hash('ex'), 'email': 'uniquemail3@gmail.com'},
            {'username': 'user101112', 'password': generate_password_hash('ex'), 'email': 'uniquemail4@gmail.com'},
            {'username': 'user131415', 'password': generate_password_hash('ex'), 'email': 'uniquemail5@gmail.com'},
            {'username': 'user161718', 'password': generate_password_hash('ex'), 'email': 'uniquemail6@gmail.com'},
            {'username': 'user192021', 'password': generate_password_hash('ex'), 'email': 'uniquemail7@gmail.com'},
            {'username': 'user222324', 'password': generate_password_hash('ex'), 'email': 'uniquemail8@gmail.com'},
            {'username': 'user252627', 'password': generate_password_hash('ex'), 'email': 'uniquemail9@gmail.com'},
            {'username': 'user282930', 'password': generate_password_hash('ex'), 'email': 'uniquemail10@gmail.com'}
        ]},
    'lecturer': {
        'query': "INSERT INTO lecturer (name, surname) VALUES (:name, :surname);",
        'params': [
            {'name': 'Krzysztof', 'surname': 'Kutt'},
            {'name': 'John', 'surname': 'Doe'},
            {'name': 'Alice', 'surname': 'Smith'},
            {'name': 'Bob', 'surname': 'Johnson'},
            {'name': 'Emma', 'surname': 'Brown'},
            {'name': 'Michael', 'surname': 'Wilson'},
            {'name': 'Emily', 'surname': 'Jones'},
            {'name': 'William', 'surname': 'Davis'},
            {'name': 'Sophia', 'surname': 'Miller'},
            {'name': 'James', 'surname': 'Taylor'},
            {'name': 'Sophie', 'surname': 'Johnson'},
            {'name': 'David', 'surname': 'Garcia'},
            {'name': 'Olivia', 'surname': 'Martinez'},
            {'name': 'Liam', 'surname': 'Brown'},
            {'name': 'Charlotte', 'surname': 'Anderson'},
            {'name': 'Daniel', 'surname': 'Hernandez'},
            {'name': 'Emma', 'surname': 'Lopez'},
            {'name': 'Lucas', 'surname': 'Gonzalez'},
            {'name': 'Ava', 'surname': 'Wilson'},
            {'name': 'Mia', 'surname': 'Taylor'}
        ]},
    'opinion': {
        'query': "INSERT INTO opinion (user_id, course_id, nastawienie, przekazywanie_wiedzy, inicjatywa, "
                 "przygotowanie, dostosowanie_wymagan, comment) VALUES (:user_id, :course_id, :nastawienie, "
                 ":przekazywanie_wiedzy, :inicjatywa, :przygotowanie, :dostosowanie_wymagan, :comment);",
        'params': [
            {'user_id': 1, 'course_id': 11, 'nastawienie': 3, 'przekazywanie_wiedzy': 4, 'inicjatywa': 2,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 2, 'course_id': 3, 'nastawienie': 2, 'przekazywanie_wiedzy': 3, 'inicjatywa': 4,
             'przygotowanie': 5, 'dostosowanie_wymagan': 1, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 3, 'course_id': 14, 'nastawienie': 4, 'przekazywanie_wiedzy': 5, 'inicjatywa': 1,
             'przygotowanie': 2, 'dostosowanie_wymagan': 3,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 4, 'course_id': 7, 'nastawienie': 5, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 4, 'dostosowanie_wymagan': 1, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 5, 'course_id': 18, 'nastawienie': 1, 'przekazywanie_wiedzy': 3, 'inicjatywa': 4,
             'przygotowanie': 2, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 6, 'course_id': 10, 'nastawienie': 2, 'przekazywanie_wiedzy': 5, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 7, 'course_id': 5, 'nastawienie': 3, 'przekazywanie_wiedzy': 1, 'inicjatywa': 2,
             'przygotowanie': 4, 'dostosowanie_wymagan': 5, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 8, 'course_id': 17, 'nastawienie': 4, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 1, 'dostosowanie_wymagan': 2, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 9, 'course_id': 2, 'nastawienie': 5, 'przekazywanie_wiedzy': 4, 'inicjatywa': 3,
             'przygotowanie': 2, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 10, 'course_id': 15, 'nastawienie': 1, 'przekazywanie_wiedzy': 2, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 1, 'course_id': 8, 'nastawienie': 2, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 4, 'dostosowanie_wymagan': 1, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 2, 'course_id': 19, 'nastawienie': 3, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 2, 'dostosowanie_wymagan': 5,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 3, 'course_id': 4, 'nastawienie': 5, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 5, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 4, 'course_id': 12, 'nastawienie': 5, 'przekazywanie_wiedzy': 3, 'inicjatywa': 4,
             'przygotowanie': 2, 'dostosowanie_wymagan': 1, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 5, 'course_id': 1, 'nastawienie': 1, 'przekazywanie_wiedzy': 4, 'inicjatywa': 5,
             'przygotowanie': 3, 'dostosowanie_wymagan': 2,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 6, 'course_id': 13, 'nastawienie': 2, 'przekazywanie_wiedzy': 1, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 4, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 7, 'course_id': 16, 'nastawienie': 5, 'przekazywanie_wiedzy': 5, 'inicjatywa': 2,
             'przygotowanie': 1, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 8, 'course_id': 9, 'nastawienie': 4, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 9, 'course_id': 20, 'nastawienie': 5, 'przekazywanie_wiedzy': 1, 'inicjatywa': 4,
             'przygotowanie': 2, 'dostosowanie_wymagan': 3, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 10, 'course_id': 6, 'nastawienie': 5, 'przekazywanie_wiedzy': 5, 'inicjatywa': 5,
             'przygotowanie': 2, 'dostosowanie_wymagan': 4, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 1, 'course_id': 2, 'nastawienie': 2, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 5, 'dostosowanie_wymagan': 3,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 2, 'course_id': 7, 'nastawienie': 5, 'przekazywanie_wiedzy': 2, 'inicjatywa': 2,
             'przygotowanie': 5, 'dostosowanie_wymagan': 4, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 3, 'course_id': 12, 'nastawienie': 4, 'przekazywanie_wiedzy': 5, 'inicjatywa': 3,
             'przygotowanie': 1, 'dostosowanie_wymagan': 2, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 4, 'course_id': 14, 'nastawienie': 5, 'przekazywanie_wiedzy': 2, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 5, 'course_id': 20, 'nastawienie': 1, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 2, 'dostosowanie_wymagan': 4, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 6, 'course_id': 5, 'nastawienie': 2, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 7, 'course_id': 11, 'nastawienie': 3, 'przekazywanie_wiedzy': 1, 'inicjatywa': 2,
             'przygotowanie': 4, 'dostosowanie_wymagan': 5,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 8, 'course_id': 17, 'nastawienie': 4, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 1, 'dostosowanie_wymagan': 2, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 9, 'course_id': 1, 'nastawienie': 5, 'przekazywanie_wiedzy': 4, 'inicjatywa': 3,
             'przygotowanie': 2, 'dostosowanie_wymagan': 1, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 10, 'course_id': 8, 'nastawienie': 1, 'przekazywanie_wiedzy': 2, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 1, 'course_id': 18, 'nastawienie': 2, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 4, 'dostosowanie_wymagan': 1, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 2, 'course_id': 9, 'nastawienie': 3, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 2, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 3, 'course_id': 20, 'nastawienie': 4, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 4, 'course_id': 3, 'nastawienie': 5, 'przekazywanie_wiedzy': 3, 'inicjatywa': 4,
             'przygotowanie': 2, 'dostosowanie_wymagan': 1, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 5, 'course_id': 11, 'nastawienie': 1, 'przekazywanie_wiedzy': 4, 'inicjatywa': 5,
             'przygotowanie': 3, 'dostosowanie_wymagan': 2, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 6, 'course_id': 2, 'nastawienie': 2, 'przekazywanie_wiedzy': 1, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 4,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 7, 'course_id': 13, 'nastawienie': 5, 'przekazywanie_wiedzy': 5, 'inicjatywa': 2,
             'przygotowanie': 2, 'dostosowanie_wymagan': 4, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 8, 'course_id': 3, 'nastawienie': 4, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 9, 'course_id': 15, 'nastawienie': 2, 'przekazywanie_wiedzy': 1, 'inicjatywa': 4,
             'przygotowanie': 2, 'dostosowanie_wymagan': 5,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 10, 'course_id': 6, 'nastawienie': 1, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 2, 'dostosowanie_wymagan': 3, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 1, 'course_id': 4, 'nastawienie': 2, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 5, 'dostosowanie_wymagan': 2, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 2, 'course_id': 16, 'nastawienie': 1, 'przekazywanie_wiedzy': 1, 'inicjatywa': 2,
             'przygotowanie': 4, 'dostosowanie_wymagan': 5,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 3, 'course_id': 18, 'nastawienie': 4, 'przekazywanie_wiedzy': 5, 'inicjatywa': 3,
             'przygotowanie': 1, 'dostosowanie_wymagan': 2, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 4, 'course_id': 20, 'nastawienie': 4, 'przekazywanie_wiedzy': 2, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 1, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 5, 'course_id': 7, 'nastawienie': 1, 'przekazywanie_wiedzy': 3, 'inicjatywa': 5,
             'przygotowanie': 2, 'dostosowanie_wymagan': 4,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 6, 'course_id': 19, 'nastawienie': 2, 'przekazywanie_wiedzy': 4, 'inicjatywa': 1,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 7, 'course_id': 1, 'nastawienie': 3, 'przekazywanie_wiedzy': 1, 'inicjatywa': 2,
             'przygotowanie': 4, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'},
            {'user_id': 8, 'course_id': 8, 'nastawienie': 4, 'przekazywanie_wiedzy': 2, 'inicjatywa': 3,
             'przygotowanie': 5, 'dostosowanie_wymagan': 1,
             'comment': 'The lecturer explained the topics very clearly'},
            {'user_id': 9, 'course_id': 10, 'nastawienie': 5, 'przekazywanie_wiedzy': 4, 'inicjatywa': 3,
             'przygotowanie': 2, 'dostosowanie_wymagan': 1, 'comment': 'This lecturer was really inspiring'},
            {'user_id': 10, 'course_id': 12, 'nastawienie': 1, 'przekazywanie_wiedzy': 2, 'inicjatywa': 4,
             'przygotowanie': 3, 'dostosowanie_wymagan': 5, 'comment': 'I enjoyed this course a lot'}
        ]},
    'course': {
        'query': "INSERT INTO course (lecturer_id, name) VALUES (:lecturer_id, :name);",
        'params': [
            {'lecturer_id': 1, 'name': "Introduction to Python Programming"},
            {'lecturer_id': 2, 'name': "Data Structures and Algorithms"},
            {'lecturer_id': 3, 'name': "Database Management Systems"},
            {'lecturer_id': 4, 'name': "Web Development with Flask"},
            {'lecturer_id': 5, 'name': "Machine Learning Fundamentals"},
            {'lecturer_id': 6, 'name': "Computer Networks"},
            {'lecturer_id': 7, 'name': "Operating Systems Principles"},
            {'lecturer_id': 8, 'name': "Software Engineering"},
            {'lecturer_id': 9, 'name': "Artificial Intelligence"},
            {'lecturer_id': 10, 'name': "Cybersecurity Fundamentals"},
            {'lecturer_id': 11, 'name': "Introduction to Python Programming"},
            {'lecturer_id': 12, 'name': "Data Structures and Algorithms"},
            {'lecturer_id': 13, 'name': "Database Management Systems"},
            {'lecturer_id': 14, 'name': "Web Development with Flask"},
            {'lecturer_id': 15, 'name': "Machine Learning Fundamentals"},
            {'lecturer_id': 16, 'name': "Computer Networks"},
            {'lecturer_id': 17, 'name': "Operating Systems Principles"},
            {'lecturer_id': 18, 'name': "Software Engineering"},
            {'lecturer_id': 19, 'name': "Artificial Intelligence"},
            {'lecturer_id': 20, 'name': "Cybersecurity Fundamentals"}
        ]}}


def clear_db():
    with db.get_engine().connect() as conn:
        conn.execute(text("DELETE FROM course"))
        conn.commit()
        conn.execute(text("DELETE FROM lecturer"))
        conn.commit()
        conn.execute(text("DELETE FROM opinion"))
        conn.commit()
        conn.execute(text("DELETE FROM user"))
        conn.commit()


def populate_db():
    with db.get_engine().connect() as conn:
        for table in queries_to_call_on:
            for params in queries_to_call_on[table]['params']:
                conn.execute(text(queries_to_call_on[table]['query']), parameters=params)
        conn.commit()
