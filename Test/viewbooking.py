try:
    import Tkinter
    import ttk
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk
    from tkinter import *

isHidden = False


def hideme(lblNoofGuests):
    global isHidden
    if not isHidden:
        lblNoofGuests.grid_remove()
        isHidden = True
    else:
        lblNoofGuests.grid()
        isHidden = False


eventlist = [['wedding', 'Holly'], ['party', 'Tom'], ['conference', 'Bob'], ['']]


class frmViewBooking(Tkinter.Frame):

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

        for event in eventlist:
            self.insert_data(event)

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Booking view")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        def selectItem(a):

            listofevents = []

            try:
                curItem = self.tree.focus()

                for value in self.tree.item(curItem)['values']:
                    listofevents.append(value)

                    type = listofevents[0]
                    return DetailsLabelChange(self, type)
            except:
                print('Select a row!!!!')

        def removeAllLabels(self):
            self.lblNoofGuests.grid_remove()
            self.lblDisNoofGuests.grid_remove()
            self.lblAddress.grid_remove()
            self.lblDisAddress.grid_remove()
            self.lblDateofBooking.grid_remove()
            self.lblDisDateofBooking.grid_remove()
            self.lblCostPerHead.grid_remove()
            self.lblDisCostPerHead.grid_remove()
            self.lblBandName.grid_remove()
            self.lblDisBandName.grid_remove()
            self.lblBandPrice.grid_remove()
            self.lblDisBandPrice.grid_remove()
            self.lblCompanyName.grid_remove()
            self.lblDisCompanyName.grid_remove()
            self.lblNumberofDays.grid_remove()
            self.lblDisNumberofDays.grid_remove()
            self.lblProjectorRequired.grid_remove()
            self.lblDisProjectorRequired.grid_remove()
            self.lblNoOfBedsReserved.grid_remove()
            self.lblDisNoOfBedsReserved.grid_remove()

        def addBaseLables(self):
            self.lblNoofGuests.grid()
            self.lblDisNoofGuests.grid()
            self.lblAddress.grid()
            self.lblDisAddress.grid()
            self.lblDateofBooking.grid()
            self.lblDisDateofBooking.grid()
            self.lblCostPerHead.grid()
            self.lblDisCostPerHead.grid()

        def addWeddingLabels(self):
            addBaseLables(self)
            self.lblBandName.grid()
            self.lblDisBandName.grid()
            self.lblBandPrice.grid()
            self.lblDisBandPrice.grid()
            self.lblNoOfBedsReserved.grid()
            self.lblDisNoOfBedsReserved.grid()

        def addPartyLabels(self):
            addBaseLables(self)
            self.lblBandName.grid()
            self.lblDisBandName.grid()
            self.lblBandPrice.grid()
            self.lblDisBandPrice.grid()

        def addConferenceLables(self):
            addBaseLables(self)
            self.lblCompanyName.grid()
            self.lblDisCompanyName.grid()
            self.lblNumberofDays.grid()
            self.lblDisNumberofDays.grid()
            self.lblProjectorRequired.grid()
            self.lblDisProjectorRequired.grid()

        def DetailsLabelChange(self, eventType):

            if eventType == 'wedding':
                removeAllLabels(self)
                addWeddingLabels(self)

            elif eventType == 'party':
                removeAllLabels(self)
                addPartyLabels(self)

            elif eventType == 'conference':
                removeAllLabels(self)
                addConferenceLables(self)

            else:
                removeAllLabels(self)

        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('Event Type', 'Contact Name', 'Contact Number', 'Event Date',
                                          'Room Number', 'Total Cost'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Event Type')
        self.tree.heading('#2', text='Contact Name')
        self.tree.heading('#3', text='Contact Number')
        self.tree.heading('#4', text='Event Date')
        self.tree.heading('#5', text='Room Number')
        self.tree.heading('#6', text='Total Cost')
        self.tree.bind('<ButtonRelease-1>', selectItem)
        self.tree.column('#0', width=100)  # column width auto size
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=100)
        self.tree.column('#6', width=100)
        self.tree.grid(row=0, columnspan=7, sticky=W)
        self.treeview = self.tree

        #  Total income section below the tree view.
        ttk.Label(self.parent, text="Total Income", font=("arial", 10, "bold")).grid(row=1, column=6, sticky=Tkinter.E,
                                                                                     padx=100)
        ttk.Label(self.parent, text="£PlaceHolder", font=("arial", 10, "bold")).grid(row=1, column=6, sticky=Tkinter.E)

        # Search for dates
        ttk.Label(self.parent, text="Search by date", font=("arial", 10, "bold")).grid(row=2, column=0, sticky=W)
        self.EntStartDate = ttk.Entry(self.parent, font=("arial", 10))
        self.EntStartDate.grid(row=3, column=0, sticky="ew")#, columnspan=1)
        ttk.Label(self.parent, text="To", font=("arial", 10, "bold")).grid(row=3, column=1)
        self.EntEndDate = ttk.Entry(self.parent, font=("arial", 10))
        self.EntEndDate.grid(row=3, column=2, sticky="ew")#, columnspan=1)

        # check boxes
        self.CbxWedding = Checkbutton(self.parent, text='Weddings', font=("arial", 10))
        self.CbxWedding.grid(row=3, column=8)
        self.CbxParties = Checkbutton(self.parent, text='Parties', font=("arial", 10))
        self.CbxParties.grid(row=3, column=9)
        self.CbxConference = Checkbutton(self.parent, text='Conference', font=("arial", 10))
        self.CbxConference.grid(row=3, column=10)

        # button
        btnSearchDate = Button(self.parent, text="Search", command=lambda: hideme(self.lblNoofGuests))
        btnSearchDate.grid(row=3, column=13)

        #  widgets for more details box
        self.labelframe = LabelFrame(self.parent, text="Additional Information", width=305, height=167)
        self.labelframe.grid(row=0, column=10, columnspan=3)

        # columns
        self.labelframe.grid_columnconfigure(1, minsize=200)
        self.labelframe.grid_columnconfigure(2, minsize=100)

        # rows
        self.labelframe.grid_rowconfigure(1, minsize=20)
        self.labelframe.grid_rowconfigure(2, minsize=20)
        self.labelframe.grid_rowconfigure(3, minsize=20)
        self.labelframe.grid_rowconfigure(4, minsize=20)
        self.labelframe.grid_rowconfigure(5, minsize=20)
        self.labelframe.grid_rowconfigure(6, minsize=20)
        self.labelframe.grid_rowconfigure(7, minsize=20)

        # labels for no of guests in additional details label frame
        self.lblNoofGuests = Label(self.labelframe, text="No of Guests: ")
        self.lblNoofGuests.grid(row=1, column=1)
        self.lblDisNoofGuests = Label(self.labelframe, text='10')
        self.lblDisNoofGuests.grid(row=1, column=2)

        # labels for Address in additional details label frame
        self.lblAddress = Label(self.labelframe, text="Address: ")
        self.lblAddress.grid(row=2, column=1)
        self.lblDisAddress = Label(self.labelframe, text='SERC')
        self.lblDisAddress.grid(row=2, column=2)

        # labels for Date of Booking in additional details label frame
        self.lblDateofBooking = Label(self.labelframe, text="Date of Booking: ")
        self.lblDateofBooking.grid(row=3, column=1)
        self.lblDisDateofBooking = Label(self.labelframe, text='10/10/2010')
        self.lblDisDateofBooking.grid(row=3, column=2)

        # labels for Cost Per Head in additional details label frame
        self.lblCostPerHead = Label(self.labelframe, text="Cost Per Head: ")
        self.lblCostPerHead.grid(row=4, column=1)
        self.lblDisCostPerHead = Label(self.labelframe, text='30')
        self.lblDisCostPerHead.grid(row=4, column=2)

        # labels for Band Name in additional details label frame
        self.lblBandName = Label(self.labelframe, text="Band Name: ")
        self.lblBandName.grid(row=5, column=1)
        self.lblDisBandName = Label(self.labelframe, text='Prawn Mendes')
        self.lblDisBandName.grid(row=5, column=2)

        # labels for Band Price in additional details label frame
        self.lblBandPrice = Label(self.labelframe, text="Band Price: ")
        self.lblBandPrice.grid(row=6, column=1)
        self.lblDisBandPrice = Label(self.labelframe, text='£250')
        self.lblDisBandPrice.grid(row=6, column=2)

        # labels for number of bedrooms reserved in additional details label frame
        self.lblNoOfBedsReserved = Label(self.labelframe, text="No. of Bedrooms Reserved: ")
        self.lblNoOfBedsReserved.grid(row=7, column=1)
        self.lblDisNoOfBedsReserved = Label(self.labelframe, text='5')
        self.lblDisNoOfBedsReserved.grid(row=7, column=2)

        # labels for Company Name reserved in additional details label frame
        self.lblCompanyName = Label(self.labelframe, text="Company Name ")
        self.lblCompanyName.grid(row=5, column=1)
        self.lblDisCompanyName = Label(self.labelframe, text='SERC')
        self.lblDisCompanyName.grid(row=5, column=2)

        # labels for Number of Days reserved in additional details label frame
        self.lblNumberofDays = Label(self.labelframe, text="Number of Days: ")
        self.lblNumberofDays.grid(row=6, column=1)
        self.lblDisNumberofDays = Label(self.labelframe, text='5')
        self.lblDisNumberofDays.grid(row=6, column=2)

        # labels for projector required reserved in additional details label frame
        self.lblProjectorRequired = Label(self.labelframe, text="Projector Required: ")
        self.lblProjectorRequired.grid(row=7, column=1)
        self.lblDisProjectorRequired = Label(self.labelframe, text='Yes')
        self.lblDisProjectorRequired.grid(row=7, column=2)

        self.labelframe.grid_rowconfigure(0, weight=1)
        self.labelframe.grid_rowconfigure(3, weight=1)
        self.labelframe.grid_columnconfigure(0, weight=1)
        self.labelframe.grid_columnconfigure(3, weight=1)

        #  widgets for more price breakdown
        self.Totallabelframe = LabelFrame(self.parent, text="Price Breakdown", width=200, height=100)
        self.Totallabelframe.grid(row=1, column=10, columnspan=3)

        # columns
        self.Totallabelframe.grid_columnconfigure(1, minsize=75)
        self.Totallabelframe.grid_columnconfigure(2, minsize=75)
        self.Totallabelframe.grid_columnconfigure(3, minsize=75)
        self.Totallabelframe.grid_columnconfigure(4, minsize=75)

        # rows
        self.Totallabelframe.grid_rowconfigure(1, minsize=20)
        self.Totallabelframe.grid_rowconfigure(2, minsize=20)
        self.Totallabelframe.grid_rowconfigure(3, minsize=20)
        self.Totallabelframe.grid_rowconfigure(4, minsize=20)

        # label for guest price
        self.lblGuestPrice = Label(self.Totallabelframe, text="Guests: ")
        self.lblGuestPrice.grid(row=1, column=1)
        self.lblDisGuestPrice = Label(self.Totallabelframe, text='£')
        self.lblDisGuestPrice.grid(row=1, column=2)

        # Label for band price
        self.lblBandCost = Label(self.Totallabelframe, text="Band: ")
        self.lblBandCost.grid(row=1, column=3)
        self.lblDisBandCost = Label(self.Totallabelframe, text="£")
        self.lblDisBandCost.grid(row=1, column=4)

        # Label for sub total
        self.lblSubTotal = Label(self.Totallabelframe, text="Sub Total: ")
        self.lblSubTotal.grid(row=2, column=1)
        self.lblDisSubTotal = Label(self.Totallabelframe, text="£")
        self.lblDisSubTotal.grid(row=2, column=2)

        # Label for VAT
        self.lblVat = Label(self.Totallabelframe, text="VAT: ")
        self.lblVat.grid(row=3, column=1)
        self.lblDisVat = Label(self.Totallabelframe, text="£")
        self.lblDisVat.grid(row=3, column=2)

        # Label for total
        self.lblTotal = Label(self.Totallabelframe, text="Total: ")
        self.lblTotal.grid(row=4, column=1)
        self.lblDisTotal = Label(self.Totallabelframe, text="£")
        self.lblDisTotal.grid(row=4, column=2)

        self.Totallabelframe.grid_rowconfigure(0, weight=1)
        self.Totallabelframe.grid_rowconfigure(3, weight=1)
        self.Totallabelframe.grid_columnconfigure(0, weight=1)
        self.Totallabelframe.grid_columnconfigure(3, weight=1)
        # Initialize the counter
        self.i = 0

        DetailsLabelChange(self, '')

    # adding data
    def insert_data(self, data):
        """
        Insertion method.
        """
        self.treeview.insert('', 'end', text="Item_" + str(self.i),
                             values=(data))
        # Increment counter
        self.i = self.i + 1


def main():
    root = Tkinter.Tk()
    d = frmViewBooking(root)
    root.mainloop()


if __name__ == "__main__":
    main()
