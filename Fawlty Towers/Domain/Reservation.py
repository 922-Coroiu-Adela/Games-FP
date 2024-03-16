import Domain.CustomDate as custom_date
import string

class Reservation:
    def __init__(self, id: string, room_number, family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month):
        self._id = id
        self._room_number = room_number
        self._family_name = family_name
        self._number_guests = number_guests
        self._check_in = custom_date.CustomDate(check_in_day, check_in_month)
        self._check_out = custom_date.CustomDate(check_out_day, check_out_month)

    def get_id(self):
        return self._id

    def get_room_number(self):
        return self._room_number

    def get_family_name(self):
        return self._family_name

    def get_number_guests(self):
        return self._number_guests

    def get_check_in(self):
        return self._check_in

    def get_check_out(self):
        return self._check_out

    def set_id(self, id):
        self._id = id

    def set_room_number(self, room_number):
        self._room_number = room_number

    def set_family_name(self, family_name):
        self._family_name = family_name

    def set_number_guests(self, number_guests):
        self._number_guests = number_guests

    def set_check_in(self, check_in):
        self._check_in = check_in

    def set_check_out(self, check_out):
        self._check_out = check_out

    def to_string(self):
        return ("ID: " + self._id + " | Room number: " + str(self._room_number) + " | Family name: " +
                self._family_name + " | Number of guests: " + str(self._number_guests) + " | Check in: " +
                self._check_in.to_string() + " | Check out: " + self._check_out.to_string())


