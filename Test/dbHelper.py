from tkinter import *
from tkinter import simpledialog
import sqlite3
import test


##set up sqlite
def connect():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    ##Create a table if none exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weddingTable(Guests REAL, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, BandPrice INTEGER, Bedrooms REAL)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS partyTable(Guests REAL, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, BandPrice INTEGER)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS conferenceTable(Guests REAL, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, CompanyName TEXT, Days REAL, ProjectRequired INTEGER)")
    db.commit()
    cursor.close()
    db.close()



# def show():
#  connt = sqlite3.connect('events.db')
#  cursor = connt.cursor()
#  cursor.execute('SELECT * FROM eventTable')
#  for row in cursor.fetchall():
#   print(row)

def read_from_db():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM weddingTable')
    list = []
    for row in cursor.fetchall():
        wedding = test.Wedding(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9])

        list.append(wedding)

    cursor.close()
    db.close()

    return list

    # cpt = 0  # Counter representing the ID of your code.
    # for row in cursor:
    #     # I suppose the first column of your table is ID
    #     tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3]))
    #     cpt += 1  # increment the ID


def insertwedding(wedding):
    conn = sqlite3.connect('events.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO weddingTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, bandPrice, Bedrooms ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
            (wedding.noGuests, wedding.nameOfContact, wedding.address, wedding.contactNo, wedding.eventRoomNo,
             wedding.dateOfEvent, wedding.dateOfBooking,
             wedding.bandName, wedding.bandPrice, wedding.noBedroomsReserved))
        conn.commit()
        cursor.close()



def insertParty(party):
    conn = sqlite3.connect('events.db')
    with conn:
        cursor = conn.cursor()
        conn.execute(
            'INSERT INTO partyTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, BandPrice) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)',
            (party.noGuests, party.nameOfContact, party.address, party.contactNo, party.eventRoomNo,
             party.dateOfEvent, party.dateOfBooking,
             party.bandName,party.bandPrice))

def insertConference(conference):
    conn = sqlite3.connect('events.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO conferenceTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, CompanyName, Days, ProjectRequired) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
        (
            conference.noGuests, conference.nameOfContact, conference.address, conference.contactNo, conference.eventRoomNo, conference.dateOfEvent, conference.dateOfBooking,
            conference.companyName, conference.noOfDays, conference.projectorRequired
        ))
        conn.commit()
        cursor.close()