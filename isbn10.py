#ISBN10


def calculate_isbn10_barcode_check_digit(barcode):
    # barcode=input('Please enter the first 9 digits of an isbn10 barcode:' )
    # if len(barcode) !=9:
    #     print ('Incorrect length. Please enter the first 9 digits of an isbn10 barcode to calculate check digit' )
    # elif len(barcode) ==9:

        digit_counter = 0
        weight = 10
        total = 0

        for char in barcode:
            digit =int(char)
            val = digit * weight
            total +=val
        
            digit_counter += 1
            weight -= 1

        mod =total % 11
        check_digit = 11 - mod
        if check_digit == 10:
            # print('check digit is X to represent 10')
            return('X')
        else:
            # print('check digit is ' + str(check_digit))
            return str(check_digit)

# calculate_isbn10_barcode_check_digit()


def validate_isbn10_barcode_check_digit(barcode):
    # barcode=input('Please enter a 10 digit isbn10 barcode:' )
    # if len(barcode) !=10:
    #     print ('Incorrect length. Please enter a 10 digit isbn10 barcode to validate the check digit' )
    # elif len(barcode) ==10:
    check_digit_entered = barcode[-1]
        # print(check_digit_entered)

    if check_digit_entered == 'X' or check_digit_entered == 'x':
        check_digit = 10
    else:
        check_digit = int(check_digit_entered)

    digit_counter = 0
    weight = 10
    total = 0

    for char in barcode[0:9]:
        digit =int(char)
        val = digit * weight
        total +=val
                
        digit_counter += 1
        weight -= 1

    mod =total % 11
    check_digit_calc = 11 - mod
    # print(check_digit, check_digit_calc, check_digit_entered)
    if check_digit == check_digit_calc:
        # print('This is a valid ISBN10 barcode')
        return ('This is a valid isbn10 barcode.')
    else:
        # print('This does not appear to be a valid barcode. Please check it carefully')
        return ('This is an invalid isbn10 barcode.')
        

# validate_isbn10_barcode_check_digit()

