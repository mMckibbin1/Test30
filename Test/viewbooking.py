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

eventlist = ['wedding','party']
class frmViewBooking(Tkinter.Frame):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Booking view")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        def selectItem(a):
            curItem = dict(self.tree.focus())
            list = []

            list = curItem.get('values')

            event = list[1]
            print(event)



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
        self.tree.bind('<Button-1>', selectItem)
        self.tree.column('#0', stretch=Tkinter.YES)  # column width auto size
        self.tree.column('#1', stretch=Tkinter.YES)
        self.tree.column('#2', stretch=Tkinter.YES)
        self.tree.column('#3', stretch=Tkinter.YES)
        self.tree.column('#4', stretch=Tkinter.YES)
        self.tree.column('#5', stretch=Tkinter.YES)
        self.tree.column('#6', stretch=Tkinter.YES)
        self.tree.grid(row=0, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        #  Total income section below the tree view.
        ttk.Label(self.parent, text="Total Income", font=("arial", 10, "bold")).grid(row=1, column=2, sticky=Tkinter.W)
        ttk.Label(self.parent, text="£PlaceHolder", font=("arial", 10, "bold")).grid(row=1, column=3, sticky=Tkinter.E)

        # Search for dates
        ttk.Label(self.parent, text="Search by date", font=("arial", 10, "bold")).grid(row=2, column=0, sticky=W)
        self.EntStartDate = ttk.Entry(self.parent, font=("arial", 10), width=50)
        self.EntStartDate.grid(row=3, column=0, sticky=W)
        ttk.Label(self.parent, text="To", font=("arial", 10, "bold")).grid(row=3, column=1)
        self.EntEndDate = ttk.Entry(self.parent, font=("arial", 10), width=50)
        self.EntEndDate.grid(row=3, column=2)

        # check boxes
        self.CbxWedding = Checkbutton(self.parent, text='Weddings', font=("arial", 10))
        self.CbxWedding.grid(row=4, column=0)
        self.CbxParties = Checkbutton(self.parent, text='Parties', font=("arial", 10))
        self.CbxParties.grid(row=4, column=1)
        self.CbxConference = Checkbutton(self.parent, text='Conference', font=("arial", 10))
        self.CbxConference.grid(row=4, column=2)

        # button
        btnSearchDate = Button(self.parent, text="Search", command=lambda: hideme(self.lblNoofGuests))
        btnSearchDate.grid(row=5, column=1)

        #  widgets for more details box
        self.labelframe = LabelFrame(self.parent, text="Additional Information", width=200, height=100)
        self.labelframe.grid(row=0, column=5)

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
        self.lblDisCompanyName = Label(self.labelframe, text='5')
        self.lblDisCompanyName.grid(row=6, column=2)

        # labels for Number of Days reserved in additional details label frame
        self.lblProjectorRequired = Label(self.labelframe, text="Number of Days: ")
        self.lblProjectorRequired.grid(row=7, column=1)
        self.lblDisProjectorRequired = Label(self.labelframe, text='5')
        self.lblDisProjectorRequired.grid(row=7, column=2)

        self.labelframe.grid_rowconfigure(0, weight=1)
        self.labelframe.grid_rowconfigure(3, weight=1)
        self.labelframe.grid_columnconfigure(0, weight=1)
        self.labelframe.grid_columnconfigure(3, weight=1)
        # Initialize the counter
        self.i = 0

    # adding data
    def insert_data(self):
        """
        Insertion method.
        """
        self.treeview.insert('', 'end', text="Item_" + str(self.i),
                             values=(+ " mg",
                                     self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1

def main():
    root = Tkinter.Tk()
    d = frmViewBooking(root)
    root.mainloop()


if __name__ == "__main__":
    main()
