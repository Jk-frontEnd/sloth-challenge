def convert_to_s(time):
    error = "-1"

    if ":" in time:
        mins, secs = time.split(":")
    
    if int(secs) >= 60:
        return error
    
    timing = int(mins) * 60 + int(secs)

    return timing
