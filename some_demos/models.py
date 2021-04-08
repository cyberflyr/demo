from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PersonalDetails(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    gender = db.Column(db.Boolean)
    mobile = db.Column(db.String(64))
    nationality = db.Column(db.String(64))
    user_id = db.Column(db.String(256))
    cv_path = db.Column(db.String(1024))

    def __init__(self, first_name, last_name, gender, mobile, nationality, user_id, cv_path):
        self.first_name = first_name,
        self.last_name = last_name,
        self.gender = gender,
        self.mobile = mobile,
        self.nationality = nationality,
        self.user_id = user_id
        self.cv_path = cv_path


class Education(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    graduation = db.Column(db.String(256))
    year_graduation = db.Column(db.Integer())
    major_graduation = db.Column(db.String(256))
    degree_graduation = db.Column(db.String(256))
    GPA = db.Column(db.Integer())
    IELTS_score = db.Column(db.Integer())
    personal_details_id = user_id = db.Column(db.String(256))

    def __init__(self, graduation, year_graduation, major_graduation, degree_graduation, GPA, IELTS_score, personal_details_id):
        self.graduation = graduation,
        self.year_graduation = year_graduation,
        self.major_graduation = major_graduation,
        self.degree_graduation = degree_graduation,
        self.GPA = GPA,
        self.IELTS_score = IELTS_score,
        self.personal_details_id = personal_details_id


class PreferredInfo(db.Model()):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    preferred_city = db.Column(db.String(256))
    preferred_major = db.Column(db.String(256))
    preferred_university = db.Column(db.String(256))
    preferred_course = db.Column(db.String(256))
    preferred_evaluation_from = db.Column(db.String(256))
    personal_details_id = user_id = db.Column(db.String(256))

    def __init__(self, preferred_city, preferred_major, preferred_university, preferred_course,
                 preferred_evaluation_from, personal_details_id):
        self.preferred_city = preferred_city,
        self.preferred_major = preferred_major,
        self.preferred_university = preferred_university,
        self.preferred_course = preferred_course,
        self.preferred_evaluation_from = preferred_evaluation_from,
        self.personal_details_id = personal_details_id


class UserInfo(db.Model()):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    user_name = db.Column(db.String(256))
    password = db.Column(db.String(256))
    email = db.Column(db.String(256))
    personal_details_id = user_id = db.Column(db.String(256))

    def __init__(self, user_name, password, email, personal_details_id):
        self.user_name = user_name,
        self.password = password,
        self.email = email,
        self.personal_details_id = personal_details_id


class University(db.Model()):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, unique=True)
    university_name = db.Column(db.String(256))
    university_city = db.Column(db.String(256))
    university_short_info = db.Column(db.TEXT)
    university_city_level = db.Column(db.Integer())

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}