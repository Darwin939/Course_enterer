from app import app , db
from flask import redirect,request,render_template , Response
from flask_login import LoginManager , login_required , login_user ,current_user
from app.models import User

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('mainpage.html')
    return redirect(location="/login/")

@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        user = db.session.query(User).filter(User.username == username).first()
        try:
            login_user(user)
            return redirect("/")
        except:
            new_user = User(username = username,password = password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")
    return render_template('login.html')


@app.route('/change_password/',methods=['POST','GET'])
def change_pwd():
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        user = db.session.query(User).filter(User.username == username).first()
        try:
            user.password = password
            db.session.commit()
            return render_template('succes.html')
        except Exception as e:
            return Response("Такого пользователя нет")
    return render_template('change_password.html')