from distutils.log import error
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user, UserMixin
from .models import Meeting, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get("title")
        topic = request.form.get("topic")
        datetime = request.form.get("datetime")
        attendee = request.form.get("attendee")
        raised = request.form.get("raised")
        actions = request.form.get("actions")
        actionsby = request.form.get("actionsby")
        information = request.form.get("information")
        completion = request.form.get("completion")
 


        if len(title) < 1:
            flash('Please enter a meeting title.', category='error')
        elif len(topic) < 1:
            flash('Please enter a meeting topic.', category='error')
        elif len(datetime) < 1:
            flash('Please enter a date time.', category='error')
        elif len(attendee) < 1:
            flash('Please enter an attendee', category='error')
        elif len(raised) < 1:
            flash('Please enter the correct information', category='error')
        elif len(actions) < 1:
            flash('Please enter the correct information', category='error')
        elif len(actionsby) < 1:
            flash('Please enter the correct information', category='error')
        elif len(information) < 1:
            flash('Please enter the correct information', category='error')
        elif len(completion) < 1:
            flash('Please enter the correct information', category='error')
        

        else:
            new_Meeting = Meeting(title=title, topic=topic, datetime=datetime, attendee=attendee, raised=raised, actions=actions, actionsby=actionsby, information=information, completion=completion, user_id=current_user.id,)
            db.session.add(new_Meeting)
            db.session.commit()
            flash('Meeting added!', category='success')

    return render_template("home.html", user=current_user)



@views.route('/deleteMeeting/<int:id>', methods=['POST'])
@login_required
def deleteMeeting(id):
    meeting = Meeting.query.get(id)
    db.session.delete(meeting)
    db.session.commit()
    flash("Meeting deleted.", category = "error")
    return render_template("minutes.html", user = current_user)