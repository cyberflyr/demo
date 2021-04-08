import os
import json
import time
import uuid
from flask import Blueprint,request, Response, render_template
from some_demos.models import db, PersonalDetails, Education, PreferredInfo, UserInfo, University
upload = Blueprint(
    'upload',
    __name__,
    template_folder='templates',
)


def build_response(status, data=None, msg=None,error_msg=None, content_type='application/Json', http_code=200):
    response = {
        'status': status,
        'data': data,
        'msg': msg,
        'error_msg': error_msg,
    }
    return Response(json.dumps(response), content_type=content_type, status=http_code)


@upload.route('/register', methods=['POST'])
def get_register_info():
    register_data = json.loads(request.form.get('data')) if request.form.get('data') else None
    if not register_data:
        return build_response(status=2, error_msg='Please upload register_form')

    # user_info
    user_name = register_data.get('UserName')
    password = register_data.get('Password')
    email = register_data.get('Email')
    user = UserInfo.query.filter_by(user_name=user_name).filter_by(email=email).first()
    if user:
        return build_response(status=2, error_msg='User already registered.')
    # personal details
    first_name = register_data.get('FirstName')
    last_name = register_data.get('LastName')
    gender = register_data.get('Gender')
    mobile_phone = register_data.get('MobilePhone')
    nationality = register_data.get('Nationality')
    personal_detail_id = str(uuid.uuid1())
    # education
    graduate_from = register_data.get('GraduateFrom')
    graduation_year = int(register_data.get('GraduationYear')) if register_data.get('GraduationYear') else -1
    graduation_major = register_data.get('GraduationMajor')
    degree = register_data.get('Degree')
    GPA = int(register_data.get('GPA')) if register_data.get('GPA') else -1
    IELTS = register_data.get('IELTS') if register_data.get('IELTS') else -1
    # preferred_option
    preferred_city = register_data.get('PreferredCity')
    preferred_major = register_data.get('PreferredMajor')
    preferred_university = register_data.get('PreferredUniversity')
    preferred_course = register_data.get('PreferredCourse')
    preferred_evaluation_from = register_data.get('PreferredEvaluation')

    cv_file = request.files.get('file')
    if cv_file:
        dir = os.path.abspath(
            os.path.dirname(
                os.path.dirname(__file__)))
        time_tag = int(time.time())
        end_with = cv_file.filename.split('.')[-1]
        save_path = dir + '/' + 'static/' + 'cv/' + f'cv_{time_tag}' + '.' + end_with
        cv_file.save(save_path)
    else:
        save_path = None
    personal_detail = PersonalDetails(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        mobile=mobile_phone,
        nationality=nationality,
        user_id=personal_detail_id,
        cv_path=save_path
    )
    db.session.add(personal_detail)
    db.session.commit()

    education = Education(
        graduation=graduate_from,
        year_graduation=graduation_year,
        major_graduation=graduation_major,
        degree_graduation=degree,
        GPA=GPA,
        IELTS_score=IELTS,
        personal_details_id=personal_detail_id
    )
    db.session.add(education)
    db.session.commit()

    preferred_info = PreferredInfo(
        preferred_city=preferred_city,
        preferred_major=preferred_major,
        preferred_university=preferred_university,
        preferred_course=preferred_course,
        preferred_evaluation_from=preferred_evaluation_from,
        personal_details_id=personal_detail_id
    )
    db.session.add(preferred_info)
    db.session.commit()

    user_info = UserInfo(
        user_name=user_name,
        password=password,
        email=email,
        personal_details_id=personal_detail_id
    )
    db.session.add(user_info)
    db.session.commit()

    return render_template("index.html")


@upload.route('/login', methods=['POST'])
def login():
    data = request.get_data()
    if data is None:
        return build_response(status=2, error_msg='Please input username and password.')
    data = json.loads(data)
    user_name = data.get('UserName')
    password = data.get('Password')
    email = data.get('Email')
    user = UserInfo.query.filter_by(user_name=user_name).filter_by(email=email).first()
    if user is None:
        return build_response(status=2, error_msg='User has not registered.')
    if user.password == password :
        return render_template("index.html")
    else:
        return build_response("Wrong password.")


@upload.route('/doSearch', methods=['GEP'])
def do_search():
    university_name = request.args.get('university_nam')
    university = University.query.filter(University.university_name.like(f'%{university_name}%')).first()
    res = {}
    if university:
        res = university.to_dict()
    return build_response(status=1, data=res)