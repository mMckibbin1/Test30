from test import Event

WeddingsList = []

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


def createWedding(noOfGuest,nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking, BandName, bedRoomsRes):

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DatofEvent, DatofBooking,
                         BandName, bedRoomsRes)

    WeddingsList.append(Newwedding)

    for wedding in WeddingsList:
        print(wedding.nameOfContact)