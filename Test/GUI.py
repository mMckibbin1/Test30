from tkinter import *
from tkinter import simpledialog
import test
from Test import dbHelper

#Main menu of applaction used to access all other forms
class mainMenu:
    def __init__(self):
        #creates form, removes maximise button on form, adds form title and adds background colour
        mainMenu = Tk()
        mainMenu.resizable(0,0)
        mainMenu.title("Main Menu")
        mainMenu.config(background="powder blue")

        #adding UI elements to the form
        Label(mainMenu, text="Please select what you would like1 to do...",font=("arial",15,"bold"), bg="powder blue")\
            .grid(row=0, pady=(25, 0), padx=(10,10))

        btnbookWedding = Button(mainMenu, text="Add wedding Booking", width=23, bg="medium aquamarine",
                                command=bookwedding)

        btnbookParty = Button(mainMenu, text="Add Party Booking", width=23, bg="medium aquamarine",  command=bookParty)
        btnbookConference = Button(mainMenu, text="Add Conference Booking", width=23, bg="medium aquamarine")
        btnviewbookings = Button(mainMenu, text="View, edit and delete Bookings", width=23, bg="medium aquamarine")

        btnbookWedding.grid(row=1, column=0, pady=(25, 5))
        btnbookParty.grid(row=2, column=0, pady=(25, 5) )
        btnbookConference.grid(row=3, column=0, pady=(25, 5))
        btnviewbookings.grid(row=4, column=0, pady=(25, 25))

        mainMenu.mainloop()


################################################################################################################


class bookwedding:
    def __init__(self):
        # mainMenu = Tk()
        FrmWeddingBooking = Toplevel()
        FrmWeddingBooking.grab_set
        mainMenu.wait_window()
        FrmWeddingBooking.title("Wedding bookings")
        FrmWeddingBooking.resizable(0, 0)
        FrmWeddingBooking.config(background="powder blue")

        noGuests = IntVar()
        nameOfContact = StringVar()
        address = StringVar()
        contactNo = StringVar()
        eventRoomNo = StringVar()
        dateOfEvent = StringVar()
        dateOfBooking = StringVar()
        bandName = StringVar()
        noBedroomsReserved = IntVar()

        Label(FrmWeddingBooking, text="Please fill in the details for the wedding event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=3)

        Label(FrmWeddingBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,
                                                                                                            pady=(
                                                                                                            25, 0),
                                                                                                            padx=(
                                                                                                            10, 10))
        Label(FrmWeddingBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,
                                                                                                            pady=(
                                                                                                            25, 0),
                                                                                                            padx=(
                                                                                                            10, 10))
        Label(FrmWeddingBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, pady=(25, 0),
                                                                                                    padx=(10, 10))
        Label(FrmWeddingBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,
                                                                                                           pady=(25, 0),
                                                                                                           padx=(
                                                                                                           10, 10))
        Label(FrmWeddingBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,
                                                                                                              pady=(
                                                                                                              25, 0),
                                                                                                              padx=(
                                                                                                              10, 10))
        Label(FrmWeddingBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,
                                                                                                          pady=(25, 0),
                                                                                                          padx=(10, 10))
        Label(FrmWeddingBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=7,
                                                                                                          pady=(25, 0),
                                                                                                          padx=(10, 10))
        Label(FrmWeddingBooking, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=8,
                                                                                                      pady=(25, 0),
                                                                                                      padx=(10, 10))
        Label(FrmWeddingBooking, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="powder blue").grid(
            row=9, pady=(25, 0), padx=(10, 10))

        self.EntnumberOfguest = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=noGuests)
        self.EntnameOfContact = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=nameOfContact)
        self.EntAddress = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=address)
        self.EntContactNumber = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=contactNo)
        self.EntEventRoomNumber = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=eventRoomNo)
        self.EntDateOfEvent = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=dateOfEvent)
        self.EntDateOfBooking = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=dateOfBooking)
        self.EntBandName = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=bandName)
        self.EntBedroomReserved = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=noBedroomsReserved)

        self.EntnumberOfguest.grid(row=1, column=1, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=1, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=1, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=1, pady=(25, 0), padx=(0, 25))
        self.EntEventRoomNumber.grid(row=5, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfEvent.grid(row=6, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfBooking.grid(row=7, column=1, pady=(25, 0), padx=(0, 25))
        self.EntBandName.grid(row=8, column=1, pady=(25, 0), padx=(0, 25))
        self.EntBedroomReserved.grid(row=9, column=1, pady=(25, 0), padx=(0, 25))



        btnCloseForm = Button(FrmWeddingBooking, text="Cancel", command=FrmWeddingBooking.quit)

        btnAddBooking = Button(FrmWeddingBooking, text="Add Booking",
                               command=lambda: [test.createwedding(self.EntnumberOfguest.get(),
                                                                  self.EntnameOfContact.get(),
                                                                  self.EntAddress.get(),
                                                                  self.EntContactNumber.get(),
                                                                  self.EntEventRoomNumber.get(),
                                                                  self.EntDateOfEvent.get(),
                                                                  self.EntDateOfBooking.get(),
                                                                  self.EntBandName.get(),
                                                                  self.EntBedroomReserved.get()), exit])

        btnAddBooking.grid(row=10, column=1, pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=2, pady=(25, 50), padx=(0, 25))
        FrmWeddingBooking.mainloop()

#####################################################################################################################

class bookParty:
    def __init__(self):
        FrmPartyBooking = Tk()
        # FrmPartyBooking = Toplevel()
        # FrmPartyBooking.grab_set
        # mainMenu.wait_window()
        FrmPartyBooking.title("Wedding bookings")
        FrmPartyBooking.resizable(0, 0)
        FrmPartyBooking.config(background="powder blue")

        noGuests = IntVar()
        nameOfContact = StringVar()
        address = StringVar()
        contactNo = StringVar()
        eventRoomNo = StringVar()
        dateOfEvent = StringVar()
        dateOfBooking = StringVar()
        bandName = StringVar()
        bandPrice = IntVar()

        Label(FrmPartyBooking, text="Please fill in the details for the Party event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=3)

        Label(FrmPartyBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,
                                                                                                            pady=(
                                                                                                            25, 0),
                                                                                                            padx=(
                                                                                                            10, 10))
        Label(FrmPartyBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,
                                                                                                            pady=(
                                                                                                            25, 0),
                                                                                                            padx=(
                                                                                                            10, 10))
        Label(FrmPartyBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, pady=(25, 0),
                                                                                                    padx=(10, 10))
        Label(FrmPartyBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,
                                                                                                           pady=(25, 0),
                                                                                                           padx=(
                                                                                                           10, 10))
        Label(FrmPartyBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,
                                                                                                              pady=(
                                                                                                              25, 0),
                                                                                                              padx=(
                                                                                                              10, 10))
        Label(FrmPartyBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,
                                                                                                          pady=(25, 0),
                                                                                                          padx=(10, 10))
        Label(FrmPartyBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=7,
                                                                                                          pady=(25, 0),
                                                                                                          padx=(10, 10))
        Label(FrmPartyBooking, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=8,
                                                                                                      pady=(25, 0),
                                                                                                      padx=(10, 10))


        self.EntnumberOfguest = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=noGuests)
        self.EntnameOfContact = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=nameOfContact)
        self.EntAddress = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=address)
        self.EntContactNumber = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=contactNo)
        self.EntEventRoomNumber = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=eventRoomNo)
        self.EntDateOfEvent = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=dateOfEvent)
        self.EntDateOfBooking = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=dateOfBooking)
        self.EntBandName = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=bandName)


        self.EntnumberOfguest.grid(row=1, column=1, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=1, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=1, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=1, pady=(25, 0), padx=(0, 25))
        self.EntEventRoomNumber.grid(row=5, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfEvent.grid(row=6, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfBooking.grid(row=7, column=1, pady=(25, 0), padx=(0, 25))
        self.EntBandName.grid(row=8, column=1, pady=(25, 0), padx=(0, 25))


        if self.EntBandName == "Lil’ Febrezey":
            self.bandPrice = 100

        elif self.EntBandName == "Prawn Mendes":
            self.bandPrice = 250

        elif self.EntBandName == "AB/CD":
            self.bandPrice = 500

        btnCloseForm = Button(FrmPartyBooking, text="Cancel", command=FrmPartyBooking.quit)

        btnAddBooking = Button(FrmPartyBooking, text="Add Booking",
                               command=lambda: [test.createParty(self.EntnumberOfguest.get(),
                                                                  self.EntnameOfContact.get(),
                                                                  self.EntAddress.get(),
                                                                  self.EntContactNumber.get(),
                                                                  self.EntEventRoomNumber.get(),
                                                                  self.EntDateOfEvent.get(),
                                                                  self.EntDateOfBooking.get(),
                                                                  self.EntBandName.get(),
                                                                  self.bandPrice), exit])

        btnAddBooking.grid(row=10, column=1, pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=2, pady=(25, 50), padx=(0, 25))
        FrmPartyBooking.mainloop()