import dbHelper


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


#########################################################################################################################


class Party(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.bandName = bandName
        self.bandPrice = bandPrice
        self.costPerHead = 15.0

        self.Total = self.noGuests * self.costPerHead

        if self.bandName == "Lil’ Febrezey":
            self.bandPrice = 100

        elif self.bandName == "Prawn Mendes":
            self.bandPrice = 250

        elif self.bandName == "AB/CD":
            self.bandPrice = 500

    def CalTotal(self):
        return self.noGuests * self.costPerHead

    def Totalvat(self):
        return

def createParty(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking, BandName):
    if BandName == "Lil’ Febrezey":
        BandPrice = 100

    elif BandName == "Prawn Mendes":
        BandPrice = 250

    elif BandName == "AB/CD":
        BandPrice = 500

    NewParty = Party(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName,BandPrice)
    return dbHelper.insertParty(NewParty)



########################################################################################################


class Wedding(Event):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice, noBedroomsReserved):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                         costPerHead=0)
        self.bandName = bandName
        self.costPerHead = 15.0
        self.noBedroomsReserved = noBedroomsReserved



        if self.bandName == "Lil’ Febrezey":
            self.bandPrice = 100

        elif self.bandName == "Prawn Mendes":
            self.bandPrice = 250

        elif self.bandName == "AB/CD":
            self.bandPrice = 500

    def grosstotal(self):
        return float (self.costPerHead * self.noGuests) + self.bandPrice

def createwedding(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking, BandName, bedRoomsRes):

    TotalCost = int()

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, bedRoomsRes)
    return dbHelper.insertwedding(Newwedding)



def bandPrice(bandName):
    if bandName == "Lil’ Febrezey":
        return 100

    elif bandName == "Prawn Mendes":
        return 250

    elif bandName == "AB/CD":
        return 500

