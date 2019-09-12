import dbHelper
import datetime

class Event:
    def __init__(self, noGuests: object, nameOfContact: object, address: object, contactNo: object, eventRoomNo: object, dateOfEvent: object, dateOfBooking: object,
                 costPerHead: object) -> object:
        self.noGuests = noGuests
        self.nameOfContact = nameOfContact
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.dateOfBooking = dateOfBooking
        self.costPerHead = costPerHead


class Conference(Event):

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 companyName, noOfDays, projectorRequired):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerHead = 20.0

    def Total(self):
        return (self.noGuests * self.costPerHead) * self.noOfDays

def createConference(noOfGuest, nameOfContact, address, contactNo,  DatofEvent, eventRoomNumber, CompanyName, NoOfDays, projectorRequired):
    datofBooking = datetime.datetime.now()

    if projectorRequired == True:
        projectorRequired = 1
    else:
        projectorRequired = 0

    newconference = Conference(int(noOfGuest),nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, datofBooking, CompanyName, NoOfDays, projectorRequired)
    return dbHelper.insertConference(newconference)


#########################################################################################################################


class Party(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.bandName = bandName
        self.costPerHead = 15.0

        self.bandPrice = CalbandPrice(bandName)

    def CalTotal(self):
        return self.noGuests * self.costPerHead

    def Totalvat(self):
        return

def createParty(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, BandName):

    BandPrice = 0
    DatofBooking = datetime.datetime.now()
    NewParty = Party(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, BandPrice)
    return dbHelper.insertParty(NewParty)



########################################################################################################################
class Wedding(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, noBedroomsReserved, bandPrice):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)

        self.bandName = bandName
        self.costPerHead = 15.0
        self.noBedroomsReserved = noBedroomsReserved
        self.bandPrice = CalbandPrice(bandName)

    def grosstotal(self):
        return float (self.costPerHead * self.noGuests) + self.bandPrice

def createwedding(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, BandName,bedRoomsRes):

    bandPrice = 0
    DatofBooking = datetime.datetime.now()

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, bedRoomsRes, bandPrice)
    return dbHelper.insertwedding(Newwedding)
########################################################################################################################


def CalbandPrice(bandName):
    if bandName == "Lil’ Febrezey":
        return 100

    elif bandName == "Prawn Mendes":
        return 250

    elif bandName == "AB/CD":
        return 500
    else:
        return 0

