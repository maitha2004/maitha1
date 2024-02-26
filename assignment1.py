#question 3
class Passenger:
    def __init__(self, firstName, lastName, fromLocation, toLocation):
        self.firstName = firstName
        self.lastName = lastName
        self.fromLocation = fromLocation
        self.toLocation = toLocation

    def get_first_name(self):
        return self.firstName

    def set_first_name(self, firstName):
        self.firstName = firstName

    def get_last_name(self):
        return self.lastName

    def set_last_name(self, lastName):
        self.lastName = lastName

    def get_from_location(self):
        return self.fromLocation

    def set_from_location(self, fromLocation):
        self.fromLocation = fromLocation

    def get_to_location(self):
        return self.toLocation

    def set_to_location(self, toLocation):
        self.toLocation = toLocation


class Flight:
    def __init__(self, airline, number, date, departureTime, arrivalTime):
        self.airline = airline
        self.number = number
        self.date = date
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime

    def get_airline(self):
        return self.airline

    def set_airline(self, airline):
        self.airline = airline

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_departure_time(self):
        return self.departureTime

    def set_departure_time(self, departureTime):
        self.departureTime = departureTime

    def get_arrival_time(self):
        return self.arrivalTime

    def set_arrival_time(self, arrivalTime):
        self.arrivalTime = arrivalTime


class Airport:
    def __init__(self, departureTerminal, arrivalTerminal):
        self.departureTerminal = departureTerminal
        self.arrivalTerminal = arrivalTerminal

    def get_departure_terminal(self):
        return self.departureTerminal

    def set_departure_terminal(self, departureTerminal):
        self.departureTerminal = departureTerminal

    def get_arrival_terminal(self):
        return self.arrivalTerminal

    def set_arrival_terminal(self, arrivalTerminal):
        self.arrivalTerminal = arrivalTerminal


class BoardingPass:
    def __init__(self, seat, gate, boardingTime, electronicTicketNumber):
        self.seat = seat
        self.gate = gate
        self.boardingTime = boardingTime
        self.electronicTicketNumber = electronicTicketNumber

    def get_seat(self):
        return self.seat

    def set_seat(self, seat):
        self.seat = seat

    def get_gate(self):
        return self.gate

    def set_gate(self, gate):
        self.gate = gate

    def get_boarding_time(self):
        return self.boardingTime

    def set_boarding_time(self, boardingTime):
        self.boardingTime = boardingTime

    def get_electronic_ticket_number(self):
        return self.electronicTicketNumber

    def set_electronic_ticket_number(self, electronicTicketNumber):
        self.electronicTicketNumber = electronicTicketNumber

#question 4

# Creating objects with the details from the boarding pass
passenger = Passenger(firstName="James", lastName="Smith", fromLocation="CHICAGO ORD", toLocation="NEW YORK JFK")
flight = Flight(airline="National Airlines", number="NA4321", date="06 DEC 20", departureTime="11:40", arrivalTime="13:30")
airport = Airport(departureTerminal="03", arrivalTerminal="2")
boarding_pass = BoardingPass(seat="09A", gate="03", boardingTime="11:20", electronicTicketNumber=629)

# Function to display boarding pass details
def display_boarding_pass_details():
    print(f"Passenger Name: {passenger.get_first_name()} {passenger.get_last_name()}")
    print(f"From: {passenger.get_from_location()} To: {passenger.get_to_location()}")
    print(f"Airline: {flight.get_airline()} Flight Number: {flight.get_number()}")
    print(f"Date: {flight.get_date()} Departure: {flight.get_departure_time()} Arrival: {flight.get_arrival_time()}")
    print(f"Departure Terminal: {airport.get_departure_terminal()} Arrival Terminal: {airport.get_arrival_terminal()}")
    print(f"Seat: {boarding_pass.get_seat()} Gate: {boarding_pass.get_gate()}")
    print(f"Boarding Time: {boarding_pass.get_boarding_time()} Electronic Ticket Number: {boarding_pass.get_electronic_ticket_number()}")

#  call the function to display the boarding pass details
display_boarding_pass_details()