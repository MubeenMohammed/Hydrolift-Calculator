# 1. Please complete the following: 
#   Your First name and Last Name: Mubeen Mohammed
#   Your Student ID: 261072123

# 2. Write your program here: 
G = 9.81

METER_PER_FEET = 0.3

KNOT_PER_METER_SEC = 0.51

def get_color():
    """
    (no input) --> integer
    The function will ask the user to select the color of the vessel
    from the given choices and if the user inputs a wrong number that
    does not correspond to a color it will keep on asking the user a
    valid input until a input given matches any one of the color
    
    """
    print('Select which number corresponds to the color of your vessel')
    print('1-Red')
    print('2-Blue ')
    print('3-White ')
    vessel_color = input("What is the color of your vessel? ")
    
    def invalid_input():
        """
        (no input) --> string
        returns the alternate vessel_color by first printing error for wrong input
        and asks for a alternate input
        """
        print("ERROR: The value you selected does not correspond to a color")
        vessel_color = input("Please choose another number between 1 and 3: ")
        return vessel_color
    
    while not is_valid_text(vessel_color,'1','3') or int(vessel_color) < 1 or int(vessel_color) > 3:
       vessel_color = invalid_input()
       
    return int(vessel_color)

    
def ship_or_boat():
    """
    (no input) --> (string)
    returns if the vessel is a boat or a ship by asking the user weight of vessel in tons
    """
    weight = float(input("Please enter the weight of your vessel in Tons: "))
    if weight > 500:
        return "Ship"
    else:
        return "Boat"
    
    
def feet_to_meter(length):
    """
    (float) --> (float)
    returns the length in meters by taking input argument in length in feet
    and converting it into meters and rounding off the result by 2 decimal numbers
    """
    
    in_meters = round(length*0.3,2)
    return in_meters


def knot_to_meter_sec(speed):
    """
    (float) --> (float)
    returns the speed in meters per sec by taking input argument of speed in knots
    converting it into meter per sec and rounding of the number by 2 decimal points
    """

    in_meter_sec = round(speed*0.51,2)
    return in_meter_sec


def is_positive(number):
    """
    (float) --> (Boolean value)
    returns a boolean value expressing wheter the input value is a
    positive number(True) or not(False)
    """
    if number > 0:
        return True
    else:
        return False
    
    
def compute_froude(length,speed):
    """
    (float,float) --> (float)
    returns froude number by taking two input arguments length and speed
    in feet and knot and then converting it to meter and meter per sec by
    calling pervious functions(feet_to_meter and knot_to_meter_sec) and
    calculating froude number using the formula
    froude_number = speed/(length*G)**(1/2)
    and then returns a float by rounding it off to 2 decimal numbers
    """
    
    speed = knot_to_meter_sec(speed)
    length = feet_to_meter(length)
    froude_number = speed/(length*G)**(1/2)
    return round(froude_number,2)


def display_hydro_lift(length,speed):
    """
    (float,float) --> (no output)
    prints different statement depending upon the computed froude number by
    calling the previous function and taking length, speed as inputs
    """
    
    froude_number = compute_froude(length,speed)
    if froude_number < 0.3:
        print("Negligible hydrodynamic lift compared to Archimedes thrust")
    elif froude_number >= 0.3 and froude_number < 0.7:
        print("Negative hydrodynamic lift")
    else:
        print("Hydrodynamic lift represents 50% of the displacement")
        
        
def is_valid_text(text,ch_min,ch_max):
    """
    (string,string,string) --> (boolean value)
    returns a boolean value by comparing if each character in text
    is between character_max and character_min values
    """
    
    for i in range(0,len(text)):
       if text[i] < ch_min or text[i] > ch_max:
           return False
    return True
    
    
def vessel_program():
    """
    (no input) --> (no output)
    it prints welcome and end messeage at the start and end of the program
    respectively and
    first gets vessel_color by calling get_color function
    display the value of the selected color
    calls the function ship or boat to obtain the nature of the vessel
    ask the user for vessel length in feet 
    Then checks if length is > 0 or not.
        if the length is > 0 then
            it will ask for speed of boat/ship in knot and
            compute vessel's hydrodynamic lift by
            calling display_hydro_lift()
        if the length is < or = 0 then
            it will print that it is impossible to to compute froude
            number for this length
    """
        
    print("**** WELCOME TO THE SHIP SCIENCE PROGRAM! ****")
    vessel_color = get_color()
    print('You selected color number:',vessel_color)
    nature_of_vessel = ship_or_boat()
    if nature_of_vessel == 'Ship':
        vessel_length = float(input('What is the length of the Ship in feet? '))
    else:
        vessel_length = float(input('What is the length of the Boat in feet? '))
    greater_than_0 = is_positive(vessel_length)
    if greater_than_0 == True:
        if nature_of_vessel == 'Ship':
            vessel_velocity = float(input('What is the speed of the Ship in knot? : '))
        else:
            vessel_velocity = float(input('What is the speed of the Boat in knot? : '))
        display_hydro_lift(vessel_length, vessel_velocity)
    else:
        print('It is impossible to compute Froude number since the length is less than or equal to 0')
    print('**** END OF THE PROGRAM. GOODBYE! ****')

vessel_program()

        
    

    
    
    
    
    

    

    
