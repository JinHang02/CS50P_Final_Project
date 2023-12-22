from project import get_input_interface,get_login_data,information_interface,summon_interface

def test_get_input_interface():
    assert get_input_interface("1") == "1"
    assert get_input_interface("2") == "2"
    assert get_input_interface("3") == "3"

def test_get_login_data():
    assert get_login_data("Kelly","halo12989","project.csv") == 0
    assert get_login_data("Ben","heisl222","project.csv") == 2

def test_information_interface():
    list1 =[{'Name': 'Kelly','Password': 'halo12989','Contact Number': '+60127867832','Email Address': 'kelly@gmail.com','State': 'Perak'},
            {'Name': 'Jin', 'Password': 'benny101', 'Contact Number': '+60178946728', 'Email Address': 'jin@hotmail.com', 'State': 'Penang'},
            {'Name': 'Ben', 'Password': 'heisl222', 'Contact Number': '+60126789234', 'Email Address': 'ben@gmail.com', 'State': 'Selangor'}]
    assert information_interface(1) == list1

def test_summon_interface():
    list2 = [{'Name': 'Kelly', 'Password': 'halo12989', 'Location': 'Penang', 'Amount': 'RM300', 'Description': 'Speeding'},
             {'Name': 'Ben', 'Password': 'heisl222', 'Location': 'Ipoh,Perak', 'Amount': 'RM200', 'Description': 'Illegal Parking'},
             {'Name': 'Jin', 'Password': 'benny101', 'Location': 'Penang', 'Amount': 'RM500', 'Description': 'Red Light Running'}]
    assert summon_interface(0) == list2
