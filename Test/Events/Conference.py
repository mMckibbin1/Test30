import datetime
import Events.BaseEvent
from Database import dbHelper


class Conference(Events.BaseEvent.BaseEventobj):

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