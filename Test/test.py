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






c1 = Conference(10, "bob", "SERC", "123456789", "A", "06/09/19", "03/09/19", "SERC2", 2, "yes")


