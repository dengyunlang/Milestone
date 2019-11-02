# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required
from .models import Candidate, Log
from . import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/profile')
@login_required
def profile():
    candidates = Candidate.query
    print()
    return render_template('profile.html', candidates=candidates)

@main.route('/statistics')
@login_required
def statistics():
    candidates = Candidate.query
    return render_template('profile.html', candidates=candidates)

@main.route('/addcandidate', methods=['POST'])
@login_required
def addcandidate():
    candidateid = request.form.get('candidateid')
    name = request.form.get('name')
    new_candidate = Candidate(candidateid=candidateid, name=name, totalballot=0)
    db.session.add(new_candidate)
    db.session.commit()
    candidates = Candidate.query
    return render_template('profile.html', candidates=candidates)

@main.route('/deletecandidate', methods = ['POST'])
@login_required
def deletecandidate():
    result = Candidate.query.filter(Candidate.id == request.form['id']).first()
    db.session.delete(result)
    db.session.commit()
    candidates = Candidate.query
    return render_template('profile.html', candidates=candidates)

@main.route('/vote', methods = ['POST'])
@login_required
def vote():
    result = Candidate.query.filter(Candidate.id == request.form['id']).first()
    result.totalballot += 1
    db.session.commit()
    candidates = Candidate.query
    return render_template('profile.html', candidates=candidates)
