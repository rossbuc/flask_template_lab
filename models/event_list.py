from models.event import *
import datetime

event1 = Event(datetime.date(2023, 9, 20), "Python Workshop", 6133, "Hall A", "Intro to Python coding skills")
event2 = Event(datetime.date(2023, 12, 23), "Java Jamboree", 42, "Hall C", "Hangout for Java enthusiasts")

events = [event1, event2]

def add_new_event(event):
    events.append(event)