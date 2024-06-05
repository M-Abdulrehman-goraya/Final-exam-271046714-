from info import Info
from property import Property
from booking import Booking
class Host(Info):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.host.append(self.name)
    def post_room(self,details):
        self.rooms.append(details)
        print(self.rooms)
    def remove_room(self,details):
        self.rooms.remove(details)