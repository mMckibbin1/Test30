import dbHelper
import datetime

class Event:
    def __init__(self, noGuests: object, nameOfContact: object, address: object, contactNo: object, eventRoomNo: object, dateOfEvent: object, dateOfBooking: object,ID,
                 costPerHead: object) -> object:
        self.noGuests = noGuests
        self.nameOfContact = nameOfContact
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.dateOfBooking = dateOfBooking
        self.costPerHead = costPerHead
        self.ID = ID


class Conference(Event):

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 companyName, noOfDays, projectorRequired, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerHead = 20.0

    def Total(self):
        return (self.noGuests * self.costPerHead) * self.noOfDays

# method to take data from form and add additional required data in order to create object to save to database
def createConference(noOfGuest, nameOfContact, address, contactNo, DateofEvent, eventRoomNumber, CompanyName, NoOfDays, projectorRequired):

    dateofBooking = datetime.datetime.now()
    ID=None
    if projectorRequired == True:
        projectorRequired = 1
    else:
        projectorRequired = 0

    newconference = Conference(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, dateofBooking, CompanyName, NoOfDays, projectorRequired, ID)
    return dbHelper.insertConference(newconference)


#########################################################################################################################


class Party(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)
        self.bandName = bandName
        self.costPerHead = 15.0

        self.bandPrice = CalbandPrice(bandName)

    def CalTotal(self):
        return self.noGuests * self.costPerHead

    def Totalvat(self):
        return

# method to take data from form and add additional required data in order to create object to save to database
def createParty(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, BandName):
    ID = None
    BandPrice = 0
    DateofBooking = datetime.datetime.now()
    NewParty = Party(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, DateofBooking,
                     BandName, BandPrice, ID)
    return dbHelper.insertParty(NewParty)



########################################################################################################################
class Wedding(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, noBedroomsReserved, bandPrice, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)

        self.bandName = bandName
        self.costPerHead = 15.0
        self.noBedroomsReserved = noBedroomsReserved
        self.bandPrice = CalbandPrice(bandName)

    def grosstotal(self):
        return float (self.costPerHead * self.noGuests) + self.bandPrice

# method to take data from form and add additional required data in order to create object to save to database
def createwedding(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, BandName, bedRoomsRes):

    ID = None
    bandPrice = 0
    DateofBooking = datetime.datetime.now()

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, DateofBooking,
                         BandName, bedRoomsRes, bandPrice, ID)
    return dbHelper.insertwedding(Newwedding)
########################################################################################################################


def CalbandPrice(bandName):
    if bandName == "Lil\' Febrezey":
        return 100

    elif bandName == "Prawn Mendes":
        return 250

    elif bandName == "AB/CD":
        return 500
    else:
        return 0

