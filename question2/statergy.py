from host import Host
from user import User
from property import Property
from booking import Booking
class Statergy:
    def user_selector(self):
        try:
            a = input("How' there user/host:")
            name = input("Enter name: ")
            contact = input("Enter contact: ")
            if a == "user":
                user = User(name,contact)
                action = input("Enter the action u wanna perfrom book/cancel: ")
                if action == "book":
                    id = input("Enter id: ")
                    checkin = input("Enter Check in: ")
                    checkout= input("Enter Check out: ")
                    user.booking(id,Booking(checkin,checkout))
                elif action == "cancel":
                    id = input("Enter id: ")
                    checkin = input("Enter Check in: ")
                    checkout= input("Enter Check out: ")
                    user.cancel_booking(id,Booking(checkin,checkout))
        

            elif a == "host":
                host = Host(name,contact)
                action = input("Enter the action u wanna perfrom book/cancel: ")
                if action == "post":
                    propertyid = input("id")
                    name1 = input("name")
                    location = input("loc")
                    discription = input("Disc")
                    price_per_night = input("ppn")
                    status = input("status")
                    host.post_room(Property(propertyid,name1,location,discription,price_per_night, status))
                elif action == "cancel":
                    propertyid = input("id")
                    name1 = input("name")
                    location = input("loc")
                    discription = input("Disc")
                    price_per_night = input("ppn")
                    status = input("status")
                    host.remove_room(Property(propertyid,name1,location,discription,price_per_night, status))
        except:
            print("Error occured")