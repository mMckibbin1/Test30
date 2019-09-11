from tkinter import *
from tkinter import simpledialog
import sqlite3
from Test import test

##set up sqlite
def connect():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    ##Create a table if none exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weddingTable(Guests REAL, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, Bedrooms REAL)")
    db.commit()



# def show():
#  connt = sqlite3.connect('events.db')
#  cursor = connt.cursor()
#  cursor.execute('SELECT * FROM eventTable')
#  for row in cursor.fetchall():
#   print(row)

def read_from_db():
    cursor.execute('SELECT * FROM weddingTable')
    # calls in the data in one big lump
    # data = c.fetchall()
    # print(data)

    # calls in the data row by row
    list= []
    for row in cursor.fetchall():
       wedding = test.Wedding(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])

       list.append(wedding)



    return list


        # cpt = 0  # Counter representing the ID of your code.
        # for row in cursor:
        #     # I suppose the first column of your table is ID
        #     tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3]))
        #     cpt += 1  # increment the ID


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
        cursor.execute('INSERT INTO weddingTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, Bedrooms) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (wedding.noGuests, wedding.nameOfContact, wedding.address, wedding.contactNo, wedding.eventRoomNo,
                        wedding.dateOfEvent, wedding.dateOfBooking,
                        wedding.bandName, wedding.noBedroomsReserved))
        db.close()


def insertParty(party):
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
        cursor.execute('INSERT INTO partyTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band) VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
                       (party.noGuests, party.nameOfContact, party.address, party.contactNo, party.eventRoomNo,
                        party.dateOfEvent, party.dateOfBooking,
                        party.bandName))
        db.close()


