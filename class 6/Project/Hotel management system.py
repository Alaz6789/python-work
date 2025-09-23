class Room:
    def __init__(self, room_number, price, is_booked = "not booked"):
        self.room_number = room_number
        self.price = price
        self.is_booked = is_booked
    def show_info(self):
        print(f"------ \n the room number is {self.room_number} \n the room costs £{self.price} \n the room {self.is_booked} ")
    def book(self):
        if self.is_booked == "not booked":
            self.is_booked = "is booked"
            print("You booked the room")
        elif self.is_booked == "is booked":
            print("already booked")

class DeluxeRoom(Room):
    def __init__(self,room_number, price, is_booked, free_breakfast):
        super().__init__(room_number, price, is_booked)
        self.free_breakfast = free_breakfast
    def show_info(self):
        super().show_info()
        print(f" free breakfast is {self.free_breakfast} \n ------")

class SuiteRoom(Room):
    def __init__(self,room_number, price, is_booked, lounge_access):
        super().__init__(room_number, price, is_booked)
        self.lounge_access = lounge_access
    def show_info(self):
        super().show_info()
        print(f" lounge access is {self.lounge_access} \n ------")

room1 = DeluxeRoom(290, 12, "not booked", "available")
room1.book()
room1.book()
room1.show_info()

room2 = SuiteRoom(312, 16, "is booked", "not available")
room2.book()
room2.book()
room2.show_info()