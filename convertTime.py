error_message_hours = "Hours input fail."
error_message_mins = "Minutes input fail."

def convertTime(time: str) -> str:
    if "pm" in time:
        time_exclusive = time.replace("pm", "").strip()
        if ":" in time_exclusive:
            hours, mins = time_exclusive.split(":")

            if int(hours) > 13:
                return error_message_hours
            
            if int(mins) >= 60:
                return error_message_mins
            
        hours = int(hours) + 12

        final_time = str(hours) + ":" + mins

        return final_time
    elif "am" in time:
        time_exclusive = time.replace("am", "").strip()
        if ":" in time_exclusive:
            hours, mins = time_exclusive.split(":")

            if int(hours) > 13:
                return error_message_hours
            
            if int(mins) >= 60:
                return error_message_mins

        final_time = hours + ":" + mins

        return final_time
    else:
        if ":" in time:
            hours, mins = time.split(":")
            
            if int(hours) > 24 or int(hours) < 0:
                return error_message_hours
            
            if int(mins) >= 60:
                return error_message_mins
            
            if int(hours) >= 12:
                suffix = "pm"
            else:
                suffix = "am"
            
            if int(hours) > 12:
                hours = int(hours) - 12
            elif int(hours) == 0:
                hours = 12
            
            final_time = str(hours) + ":" + mins + " " + suffix
            
            return final_time




result = convertTime("5:20 pm")
print("test one: ", result)

result = convertTime("5:20 am")
print("test two: ", result)

result = convertTime("5:60 am")
print("test three: ", result)

result = convertTime("17:20")
print("test four: ", result)

result = convertTime("7:40")
print("test five: ", result)

result = convertTime("26:00")
print("test five: ", result)