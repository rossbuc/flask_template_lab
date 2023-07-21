from flask import render_template, redirect, Blueprint, request
from models.event_list import *

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='My Events Planner', events=events)

@events_blueprint.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name_of_event']
    event_description = request.form['description']
    event_date = request.form['date']
    event_number_of_guests = request.form['number_of_guests']
    event_room_location = request.form['room_location']
    event_recurring = request.form.get('recurring')
    new_event = Event(event_date, event_name, event_number_of_guests, event_room_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('index.jinja', title='My Events Planner', events=events)

@events_blueprint.route('/events/delete/<event_name>', methods=['POST'])
def delete(event_name):
    print(event_name)
    delete_event(event_name)
    return redirect('/events')