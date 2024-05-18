from app import db
from flask_login import UserMixin
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    is_admin: so.Mapped[bool] = so.mapped_column()

    def __repr__(self):
        return f'<User {self.username}>'


class Lecturer(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(100))
    surname: so.Mapped[str] = so.mapped_column(sa.String(100))

    def __repr__(self):
        return f"<Lecturer {self.name + ' ' + self.surname}>"


class Course(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    lecturer_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Lecturer.id))
    name: so.Mapped[str] = so.mapped_column(sa.String(100))

    def __repr__(self):
        return f'<Course {self.name}>'


class Opinion(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id))
    course_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Course.id))
    nastawienie: so.Mapped[int] = so.mapped_column()
    przekazywanie_wiedzy: so.Mapped[int] = so.mapped_column()
    inicjatywa: so.Mapped[int] = so.mapped_column()
    przygotowanie: so.Mapped[int] = so.mapped_column()
    dostosowanie_wymagan: so.Mapped[int] = so.mapped_column()
    comment: so.Mapped[str] = so.mapped_column(sa.String(1024))

    def __repr__(self):
        return f'<Opinion of {self.user_id} on {self.course_id}>'
