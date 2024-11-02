def nums_to_eng(num: int) -> str:
    if num < 0 or num > 999:
        return
    
    less_than_20_ls = [
        "zero", 
        "one", 
        "two", 
        "three", 
        "four", 
        "five", 
        "six", 
        "seven", 
        "eight", 
        "nine", 
        "ten",
        "eleven", 
        "twelve", 
        "thirteen", 
        "fourteen", 
        "fifteen", 
        "sixteen", 
        "seventeen", 
        "eighteen", 
        "nineteen"
    ]
    
    tens_ls = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"
    ]

    if num < 20:
        return less_than_20_ls[num]
    
    elif num < 100:
        tens_index = num // 10 - 2 
        ones_index = num % 10
        if ones_index == 0:
            return tens_ls[tens_index]
        else:
            return tens_ls[tens_index] + " " + less_than_20_ls[ones_index]
    
    else:
        hundreds_place = num // 100
        remainder = num % 100
        if remainder == 0:
            return less_than_20_ls[hundreds_place] + " hundred"
        else:
            return less_than_20_ls[hundreds_place] + " hundred " + nums_to_eng(remainder)
