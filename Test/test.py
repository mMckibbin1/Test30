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



class Party(Event):
    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.bandName = bandName
        self.bandPrice = bandPrice
        self.costPerHead = 15.0

        self.Total = self.noGuests * self.costPerHead

    def CalTotal(self):
        return self.noGuests * self.costPerHead

    def Totalvat(self):
        return

class Wedding(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, noBedroomsReserved):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.bandName = bandName
        self.costPerHead = 15.0
        self.noBedroomsReserved = noBedroomsReserved

        total = self.noGuests * self.costPerHead

        if self.bandName == "Lil’ Febrezey":
            self.bandPrice = 100

        elif self.bandName == "Prawn Mendes":
            self.bandPrice = 250

        elif self.bandName == "AB/CD":
            self.bandPrice = 500

    def Total(self):
        return float (self.costPerHead * self.noGuests) + self.bandPrice


def addWedding():
    noOfGuest = input("enter number of guests\n")
    nameOfContact = input("enter Name of Contact\n")
    address = input("enter address\n")
    contactNo = input("enter Contact Number\n")
    eventRoomNumber = input("enter event Room Number\n")
    DatofEvent = input("enter Date of Event\n")
    DatofBooking = input("enter Date of booking\n")
    BandName = input("enter band Name\n")
    bedRoomsRes = input("enter number of bed rooms you would like\n")

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, bedRoomsRes)
    return print(Newwedding.nameOfContact)


def createWedding(noOfGuest,nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking, BandName, bedRoomsRes):

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, bedRoomsRes)
    return print(Newwedding.nameOfContact)




c1 = Conference(10, "bob", "SERC", "123456789", "A", "06/09/19", "03/09/19", "SERC2", 2, "yes")


