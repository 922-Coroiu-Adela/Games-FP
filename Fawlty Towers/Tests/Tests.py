import Service.Service as Service
import Domain.CustomDate as CustomDate

# function to test the add_reservation function
def test_add_reservation():
    service = Service.Service()
    service.add_reservation("Test_name", 2, 1, 1, 2, 1)
    assert service.get_reservations()[-1].get_family_name() == "Test_name"
    assert service.get_reservations()[-1].get_number_guests() == 2

def test_valid_date():
    service = Service.Service()
    custom_date1 = CustomDate.CustomDate(1, 1)
    custom_date2 = CustomDate.CustomDate(4, 1)
    custom_date3 = CustomDate.CustomDate(2, 1)
    custom_date4 = CustomDate.CustomDate(3, 1)
    assert service.valid_date(custom_date1, custom_date2, custom_date3, custom_date4) == False
    custom_date5 = CustomDate.CustomDate(5, 1)
    custom_date6 = CustomDate.CustomDate(6, 1)
    assert service.valid_date(custom_date1, custom_date2, custom_date5, custom_date6) == True
    custom_date7 = CustomDate.CustomDate(1, 2)
    custom_date8 = CustomDate.CustomDate(3, 5)
    custom_date9 = CustomDate.CustomDate(2, 4)
    custom_date10 = CustomDate.CustomDate(2, 7)
    assert service.valid_date(custom_date7, custom_date8, custom_date9, custom_date10) == False
    custom_date11 = CustomDate.CustomDate(1, 2)
    custom_date12 = CustomDate.CustomDate(3, 5)
    custom_date13 = CustomDate.CustomDate(3, 6)
    custom_date14 = CustomDate.CustomDate(3, 7)
    assert service.valid_date(custom_date11, custom_date12, custom_date13, custom_date14) == True

def test_delete_reservation():
    service = Service.Service()
    service.add_reservation("Test_name", 2, 1, 1, 2, 1)
    id = service.get_reservations()[-1].get_id()
    service.delete_reservation(id)
    assert id not in [reservation.get_id() for reservation in service.get_reservations()]

def test_functionalities():
    test_add_reservation()
    test_valid_date()
    test_delete_reservation()
    print("All tests passed")