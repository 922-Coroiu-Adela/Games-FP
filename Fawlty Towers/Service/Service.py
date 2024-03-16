import Repository.Repository as Repository
import Domain.CustomDate as CustomDate
import Domain.Reservation as Reservation
import random


class Service:
    def __init__(self):
        self._repository = Repository.Repository()

    def add_reservation(self, family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month):
        '''
        Adds a reservation to the repository
        :param family_name: the name of the family
        :param number_guests:   the number of guests
        :param check_in_day: the day of the check in
        :param check_in_month: the month of the check in
        :param check_out_day:  the day of the check out
        :param check_out_month: the month of the check out
        :return:
        '''
        if family_name == "":
            raise ValueError("Family name cannot be empty")
        if number_guests < 1:
            raise ValueError("Number of guests must be at least 1")
        if number_guests > 4:
            raise ValueError("Number of guests cannot exceed 4")
        if check_in_month < 1 or check_in_month > 12:
            raise ValueError("Invalid check in month")
        if check_out_month < 1 or check_out_month > 12:
            raise ValueError("Invalid check out month")
        if check_in_day < 1 or check_in_day > 31:
            raise ValueError("Invalid check in day")
        if check_out_day < 1 or check_out_day > 31:
            raise ValueError("Invalid check out day")
        check_in = CustomDate.CustomDate(check_in_day, check_in_month)
        check_out = CustomDate.CustomDate(check_out_day, check_out_month)
        if check_in >= check_out:
            raise ValueError("Invalid check in/out dates")
        room_number = self.find_available_room(check_in, check_out, number_guests)
        if room_number is None:
            raise ValueError("No available rooms")
        id = self.generate_random_id()
        reservation = Reservation.Reservation(id, room_number, family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month)
        self._repository.add_reservation(reservation)

    def generate_random_id(self):
        '''Generates a random id for a reservation'''
        # the id has 4 digits
        id =  str(random.randint(1000, 9999))
        # we check if the id is already used
        reservations = self._repository.get_reservations()
        for reservation in reservations:
            if reservation.get_id() == id:
                return self.generate_random_id()
        return id

    def save_changes(self):
        '''Saves the changes made to the repository'''
        self._repository.save_changes()

    def find_available_room(self, check_in, check_out, number_guests):
        '''
        Finds an available room for the given period and number of guests
        :param check_in: the check in date
        :param check_out: the check out date
        :param number_guests: the number of guests
        :return:
        '''
        reservations = self._repository.get_reservations()
        rooms = self._repository.get_rooms()
        # we keep only the rooms that have the required number of beds
        rooms = [room for room in rooms if room[1] >= number_guests]
        # we keep only the rooms that are not reserved in the given period
        for reservation in reservations:
            if self.valid_date(check_in, check_out, reservation.get_check_in(), reservation.get_check_out()):
                return reservation.get_room_number()
        return None

    def delete_reservation(self, id):
        '''Deletes a reservation from the repository'''
        if id == "":
            raise ValueError("ID cannot be empty")
        if id not in [reservation.get_id() for reservation in self._repository.get_reservations()]:
            raise ValueError("Invalid ID")
        self._repository.delete_reservation(id)


    def valid_date(self, check_in, check_out, reservation_check_in, reservation_check_out):
        '''
        Checks if the given period is valid
        :param check_in: the check in date
        :param check_out: the check out date
        :param reservation_check_in: the check in date of the reservation
        :param reservation_check_out: the check out date of the reservation
        :return: the result of the check
        '''
        if check_in.month == reservation_check_in.month:
            if check_in.day >= reservation_check_in.day:
                return False
        if check_out.month == reservation_check_in.month:
            if check_out.day >= reservation_check_in.day:
                return False
        if check_out.month == reservation_check_out.month:
            if check_out.day >= reservation_check_out.day:
                return False
        if reservation_check_in.month < check_in.month < reservation_check_out.month:
            return False
        if check_in.month < reservation_check_in.month < check_out.month:
            return False
        if reservation_check_in.month < check_out.month < reservation_check_out.month:
            return False
        if check_in.month < reservation_check_out.month < check_out.month:
            return False
        return True

    def available_rooms(self, check_in, check_out):
        rooms = self._repository.get_rooms()
        reservations = self._repository.get_reservations()
        available_rooms = []
        for room in rooms:
            available_rooms.append(room[0])
        for reservation in reservations:
            if not self.valid_date(check_in, check_out, reservation.get_check_in(), reservation.get_check_out()):
                if reservation.get_room_number() in available_rooms:
                    available_rooms.remove(reservation.get_room_number())
        return available_rooms

    def get_reservations(self):
        return self._repository.get_reservations()