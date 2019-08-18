#gtin13


def calculate_gtin13_barcode_check_digit(barcode):
    # barcode=input('Please enter a 12 digit gt13 barcode:' )
    # if len(barcode) !=12:
    #     print ('Incorrect length. Please enter a 12 digit gt13 barcode to calculate check digit' )
    # elif len(barcode) ==12:

        digit_counter = 1
        total = 0

        for char in barcode:
            digit =int(char)
            
            if digit_counter %2 ==1:
                total += digit
            elif digit_counter %2 ==0:
                    total += (digit *3)
        
            digit_counter +=1

        print (total)
        mod =total % 10
        print(mod)
        if mod ==0:
            check_digit =0
        else:
            check_digit = 10 - mod    
        # print('check digit is ' + str(check_digit))
        return str(check_digit)

# calculate_gtin13_barcode_check_digit()   

def validate_gtin13_barcode_check_digit(barcode):
    # barcode=input('Please enter a 13 digit gt13 barcode, including check digit:' )
    # if len(barcode) !=13:
    #     print ('Incorrect length. Please enter a 13 digit gt13 barcode to validate check digit' )
    # elif len(barcode) ==13:
        digit_counter = 0
        total = 0
        while digit_counter < 12:
            digit = int(barcode[digit_counter])

            if digit_counter %2 == 0:
                total += digit
            elif digit_counter %2 == 1:
                total += (digit *3)

            digit_counter += 1

        print (total)
        mod =total % 10
        print(mod)
        if mod ==0:
            check_digit = 0
        else:
            check_digit = 10 - mod
                
        last_digit= int(barcode[-1])
        if check_digit == last_digit:
            # print('This is a valid gtin13 barcode with correct check digit')
            return ('This is a valid gtin13 barcode.')
        else:
            # print('This is not a valid gtin13 barcode. Please check barcode carefully')
            return ('This is an invalid gtin13 barcode.')

# validate_gtin13_barcode_check_digit()