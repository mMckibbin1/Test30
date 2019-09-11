from tkinter import *
from tkinter import simpledialog
import sqlite3
from Test import test

##set up sqlite
db = sqlite3.connect('events.db')
cursor = db.cursor()
##Create a table if none exists
cursor.execute(
    "CREATE TABLE IF NOT EXISTS eventTable(Guests REAL, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, Bedrooms REAL)")
db.commit()



# def show():
#  connt = sqlite3.connect('events.db')
#  cursor = connt.cursor()
#  cursor.execute('SELECT * FROM eventTable')
#  for row in cursor.fetchall():
#   print(row)

def read_from_db():
    db.execute('SELECT * FROM eventTable')
    # calls in the data in one big lump
    # data = c.fetchall()
    # print(data)

    # calls in the data row by row
    for row in db.fetchall():
        print(row)


def insertwedding(wedding):
    # noGuests1 = wedding.noGuests
    # nameOfContact1 = nameOfContact.get()
    # address1 = address.get()
    # contactNo1 = contactNo.get()
    # eventRoomNo1 = eventRoomNo.get()
    # dateOfEvent1 = dateOfEvent.get()
    # dateOfBooking1 = dateOfBooking.get()
    # bandName1 = bandName.get()
    # noBedroomsReserved1 = noBedroomsReserved.get()

    conn = sqlite3.connect('events.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO eventTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, Bedrooms) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (wedding.noGuests, wedding.nameOfContact, wedding.address, wedding.contactNo, wedding.eventRoomNo,
                        wedding.dateOfEvent, wedding.dateOfBooking,
                        wedding.bandName, wedding.noBedroomsReserved))
        db.close()



