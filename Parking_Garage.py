from Nguyen_Thai_QueueClass import Garage


# Three instances of the Garage Class and passing the max size of each queue
fenway_garage = Garage(5)
garden_garage = Garage(6)
street_parking = Garage(4)

# Clears the queues
fenway_garage.clear()
garden_garage.clear()
street_parking.clear()


# User selection function
def user_input():
    print('Enter A for vehicle arrival into garage.')
    print('OR')
    print('Enter D for vehicle departure out of garage.')
    print('OR')
    print('Enter Q to quit.')
    user_selection = input('Selection: ')
    return user_selection


# Holding variables for how many vehicles leave and total fees collected
fee_counter = 0
total_fees = 0

while True:
    selection = user_input()
    if selection.upper() == 'A':
        # Moves vehicles into the Fenway Parking Garage
        while not fenway_garage.is_full():
            print()
            print('Fenway Garage has room for vehicles.')
            license_plate = input('Enter the vehicle license plate information: ')
            fenway_garage.insert(license_plate)
            print()
            print('Vehicle has been added to Fenway Parking Garage.')
            print()
            if fenway_garage.is_full():
                print('FENWAY PARKING GARAGE FULL!')
                print()
            break

        # Moves vehicles into the Garden Parking Garage
        while not garden_garage.is_full() and fenway_garage.is_full():
            if garden_garage.is_empty():
                selection = user_input()
            print()
            print('Garden Garage has room for vehicles.')
            license_plate = input('Enter the vehicle license plate information: ')
            garden_garage.insert(license_plate)
            print()
            print('Vehicle has been added to Garden Parking Garage.')
            print()
            if garden_garage.is_full():
                print('GARDEN PARKING GARAGE FULL!')
                print()
            break

        # Moves vehicles into Street Parking
        while fenway_garage.is_full() and garden_garage.is_full() and not street_parking.is_full():
            if street_parking.is_empty():
                selection = user_input()
            print()
            print('Street Parking has room for vehicles.')
            license_plate = input('Enter the vehicle license plate information: ')
            street_parking.insert(license_plate)
            print()
            print('Vehicle has been added to Street Parking.')
            print()
            if street_parking.is_full():
                print('STREET PARKING FULL!')
                print()
            break

        # Output message if all parking lots are full
        while fenway_garage.is_full() and garden_garage.is_full() and street_parking.is_full():
            print('FENWAY, GARDEN, and STREET PARKING ARE ALL FULL!')
            print()
            break

    if selection.upper() == 'D':
        # Outputs a message if there are no cars in the queue
        if fenway_garage.is_empty() and garden_garage.is_empty() and street_parking.is_empty():
            print()
            print("OOPS. WE CAN'T FIND YOUR CAR. HEY ITS BEAN TOWN, WHAT'D YOU EXPECT.")
            print()

        # Moves the first vehicle in the queue out of Fenway Parking Garage
        if not fenway_garage.is_empty():
            print()
            print('VEHICLE DEPARTURE NOTICE')
            print('Departing Vehicle:', fenway_garage.delete().upper().__str__())
            print()
            fee_counter += 1

            # Moves vehicles from the Garden into Fenway and Street into Garden if there is room in the queue
            if not garden_garage.is_empty():
                fenway_garage.insert(garden_garage.delete())
            if not street_parking.is_empty():
                garden_garage.insert(street_parking.delete())

    # Output the vehicles left in each parking garage/lot
    if selection.upper() == 'Q':
        print()
        print('Fenway Parking Garage has', fenway_garage.size_of_queue().__str__(), 'vehicles.')
        print('Fenway Garage:')
        while not fenway_garage.is_empty():
            print(fenway_garage.delete())

        print()
        print('Garage Parking Garage has', garden_garage.size_of_queue().__str__(), 'vehicles.')
        print('Garden Garage:')
        while not garden_garage.is_empty():
            print(garden_garage.delete())

        print()
        print('Street Parking has', street_parking.size_of_queue().__str__(), 'vehicles.')
        print('Street Parking:')
        while not street_parking.is_empty():
            print(street_parking.delete())

        # Fee Calculation for Departing Vehicles
        for i in range(1, fee_counter + 1):
            total_fees += i * 5

        # Output either number of vehicles charge and the total fees collected or none if no vehicles have departed
        print()
        if total_fees == 0:
            print('No vehicles have left the facility.')
            print('Total Fees: $', total_fees, sep='')
        else:
            print('Number of vehicles charged:', fee_counter)
            print('Total Fees: $', total_fees, sep='')
        print()
        break
