import Service.Service as Service
import Domain.CustomDate as CustomDate
class UI:
    def __init__(self):
        self._service = Service.Service()

    def show_reservations(self):
        reservations = self._service.get_reservations()
        for reservation in reservations:
            print(reservation.to_string())

    def run(self):
        while True:
            print("1. Add reservation")
            print("2. Show reservations")
            print("3. Delete reservation")
            print("4. Find available rooms for a time period")
            print("0. Exit")
            option = input("Enter option: ")
            if option == "1":
                try:
                    family_name = input("Enter family name: ")
                    number_guests = int(input("Enter number of guests: "))
                    check_in_day = int(input("Enter check in day: "))
                    check_in_month = int(input("Enter check in month: "))
                    check_out_day = int(input("Enter check out day: "))
                    check_out_month = int(input("Enter check out month: "))
                    self._service.add_reservation(family_name, number_guests, check_in_day, check_in_month, check_out_day, check_out_month)
                except ValueError as ve:
                    print(ve)
            elif option == "2":
                self.show_reservations()
            elif option == "3":
                try:
                    id = input("Enter the id of the reservation you want to delete: ")
                    self._service.delete_reservation(id)
                    print("Reservation deleted")
                except ValueError as ve:
                    print(ve)
            elif option == "4":
                try:
                    check_in_day = int(input("Enter check in day: "))
                    check_in_month = int(input("Enter check in month: "))
                    check_out_day = int(input("Enter check out day: "))
                    check_out_month = int(input("Enter check out month: "))
                    date1 = CustomDate.CustomDate(check_in_day, check_in_month)
                    date2 = CustomDate.CustomDate(check_out_day, check_out_month)
                    room = self._service.available_rooms(date1, date2)
                    if room is None:
                        print("No available rooms")
                    else:
                        print("Available rooms: " + str(room))
                except ValueError as ve:
                    print(ve)
            elif option == "0":
                self._service.save_changes()
                return
            else:
                print("Invalid option")