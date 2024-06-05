from info import Info
from booking import Booking
from host import Host
class User(Info):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.user.append(self.user)
    def booking(self,id,details):
        if id in self.rooms:
            self.bookings.append(details)
            print("Ticket Booked")
        else:
            print("Error Occured")
    def cancel_booking(self,details):
        if self.name in self.bookings:
            self.bookings.remove(details)