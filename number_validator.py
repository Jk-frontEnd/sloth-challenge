import time

def isValidPhoneNumber(number: str) -> bool:
    # Format validation
    number_format_valid = check_number_format(number)
    time.sleep(2)
    if number_format_valid:
        format_val = "Success"
    else:
        format_val = "Fail"
    print(f"Format validation: {format_val}.")
    stripe_short()
    
    # Lenght validation
    number_length_valid = check_number_length(number)
    time.sleep(2)
    if number_length_valid:
        lenght_val = "Success"
    else:
        lenght_val = "Fail"
    print(f"Lenght validation: {lenght_val}.")
    stripe_short()
    
    
    # Final validation
    if not (number_length_valid and number_format_valid):
        final_val = "Fail"
        print(f"Number validation resolved in {final_val}.\nCheck the input number's length and format to match the pattern and try again.\nPattern:\n(xxx) xxx-xxxx")
    else:
        final_val = "Success"
        print(f"Number validation resolved in {final_val}.")
    stripe_long()

def check_number_length(number):
    stripped_number = number.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()
    
    if len(stripped_number) > 10:
        time.sleep(2)
        number_length_valid = False
    elif len(stripped_number) < 10:
        time.sleep(2)
        number_length_valid = False
    else:
        time.sleep(2)
        number_length_valid = True
    return number_length_valid

def check_number_format(number):
    # Check format for (xxx) xxx-xxxx
    has_parentheses_at_positions = number[0] == "(" and number[4] == ")" 
    has_spaces_at_position = number[5] == " "
    has_hyphen_at_position = number[9] == "-"

    result = has_parentheses_at_positions and has_spaces_at_position and has_hyphen_at_position
    
    if not result:
        time.sleep(4)
        number_format_valid = False
    else:
        number_format_valid = True
    return number_format_valid

def stripe_long():
    print("----------------------------------------")

def stripe_short():
    print("----")

# valid phone number: (123) 456-7890
# any number between 0 - 9 in appropriate spots -> valid number

# strip number from "()", "-" and spaces count is number len() == 10
# check the places
# first = "("
# fourth = ")"
# eleventh = "-"


# ------------
# MESSAGES
# lenght_val = "Success" / "Fail"
# format_val = "Success" / "Fail"
# Lenght validation: success.
# Format validation: success.
# Number validation resolved in success. 

# Lenght validation: fail.
# Format validation: fail.
# Number validation resolved in Fail.\nCheck the input number's length and format to match the pattern and try again.\nPattern:\n(xxx) xxx-xxxx


isValidPhoneNumber("(123) 456-7890")  # true
isValidPhoneNumber("098) 123 4567")  # false
isValidPhoneNumber("1111)555 2345")  # false
