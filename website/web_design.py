from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from website import app_db
import json
web_design = Blueprint('web_design', __name__)

"""

Add the name of the blueprint as the decorator and include a route which is the URL that will take the user to this application. 
Whatever is inside the defined function called home will run on the main webpage.

"""

@web_design.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            app_db.session.add(new_note)
            app_db.session.commit()
            flash('Note is successfully added', category='success')
    return render_template("home.html", user=current_user)

@web_design.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            app_db.session.delete(note)
            app_db.session.commit()
    return jsonify({})

