import Domain.Reservation as Reservation
import Domain.CustomDate as CustomDate


class Repository:
    def __init__(self):
        self._reservations = []
        self._rooms = []
        self.load_reservations()
        self.load_rooms()

    def add_reservation(self, reservation):
        self._reservations.append(reservation)

    def load_reservations(self):
        with open("reservations.txt", "r") as file:
            # Read the file line by line
            # The reservation file has the following format:
            # id, room_number, family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month
            for line in file:
                # Split the line into its components
                components = line.split(",")
                # Create a new reservation
                reservation = Reservation.Reservation(components[0], int(components[1]), components[2], int(components[3]), int(components[4]), int(components[5]), int(components[6]), int(components[7]))
                # Add the reservation to the list
                self.add_reservation(reservation)

    def load_rooms(self):
        with open("rooms.txt", "r") as file:
            # the format is room_number, number_of_beds
            for line in file:
                components = line.split(",")
                self._rooms.append([int(components[0]), int(components[1])])

    def save_changes(self):
        with open("reservations.txt", "w") as file:
            for reservation in self._reservations:
                # Write the reservation to the file
                # The format is id, room_number, family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month
                file.write(reservation.get_id() + "," + str(reservation.get_room_number()) + "," +
                           reservation.get_family_name() + "," + str(reservation.get_number_guests())
                           + "," + str(reservation.get_check_in().day) + "," + str(reservation.get_check_in().month)
                           + "," + str(reservation.get_check_out().day) + "," + str(reservation.get_check_out().month)
                           + "\n")

    def delete_reservation(self, id):
        for i in range(len(self._reservations)):
            if self._reservations[i].get_id() == id:
                del self._reservations[i]
                return

    def get_reservations(self):
        return self._reservations

    def get_rooms(self):
        return self._rooms

