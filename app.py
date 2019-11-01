from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.security import check_password_hash, generate_password_hash


from User import User

app = Flask(__name__)

# roles -> different privilege
user1 = User(username="admin", password=generate_password_hash("123", method='sha256'), role="1")
user2 = User(username="court", password=generate_password_hash("123", method='sha256'), role="2")
user3 = User(username="delegate", password=generate_password_hash("123", method='sha256'), role="3")
user4 = User(username="voter", password=generate_password_hash("123", method='sha256'), role="4")
users = [user1, user2, user3, user4]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    for user in users:
        # authentication
        if username == user.username and check_password_hash(user.password, password):
            return render_template('nav.html', messages={'username': username})
    # audit log "login successful"
    return redirect(url_for('index'))  # no matched account

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # can only create voter account in website
    role = '4'
    # encryption
    for user in users:
        # check if user exist
        if username == user.username:
            print("user already exist")
            return render_template('signup.html')

    # add new user in memory
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'), role=role)
    users.append(new_user)
    return render_template('nav.html', messages={'username': username})

@app.route('/track', methods=['POST'])
def track():
    # track user's behaviour
    username = request.form.get('username')
    action = request.form.get('action')

