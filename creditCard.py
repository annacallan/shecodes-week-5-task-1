#Credit Card



def validate_credit_card_number_check_digit(card_number):
    # card_number=input('Please enter credit card number: ')
    card_number_minus_check = card_number[:-1]
    check_digit_entered = int(card_number[-1])
    length = len(card_number_minus_check)
    card_digit_counter = length
    number_index = -1
    total = 0
    while card_digit_counter > 0:
        digit = int(card_number_minus_check[number_index])

        if number_index %2 == 1:
            val= digit * 2
            if val > 9:
                total += (val - 9)
            else:
                total += val
        elif number_index %2 == 0:
            total += digit
        number_index -= 1
        card_digit_counter -= 1

    total_str =str(total)
    check_digit_calc = 10 - int(total_str[-1])
    if check_digit_calc == 10:
        check_digit = 0
    else:
        check_digit = check_digit_calc
    
    if check_digit == check_digit_entered:
        # print('This is a valid credit card number')
        return ('This is a valid credit card number.')
    else:
        # print('This is not a valid credit card number. Please check the number carefully')
        return ('This is an invalid credit card number.')


# validate_credit_card_number_check_digit()


def calculate_credit_card_number_check_digit(card_number):
    # card_number=input('Please enter credit card number without the last check digit: ')
    length = len(card_number)
    card_digit_counter = length
    number_index = -1
    total = 0
    while card_digit_counter > 0:
        digit = int(card_number[number_index])

        if number_index %2 == 1:
            val= digit * 2
            if val > 9:
                total += (val - 9)
            else:
                total += val
        elif number_index %2 == 0:
            total += digit
        number_index -= 1
        card_digit_counter -= 1

    total_str =str(total)
    # print(total)
    # print(total_str)
    # print(total_str[-1])
    check_digit_calc = 10 - int(total_str[-1])
    if check_digit_calc == 10:
        check_digit = 0
    else:
        check_digit = check_digit_calc
    print('The check digit is %d' % check_digit)  
    return str(check_digit)  
    print (check_digit)



# calculate_credit_card_number_check_digit()

# calculate_credit_card_number_check_digit('542418027979176')
# calculate_credit_card_number_check_digit('601100099301097')


# 5424180279791760 valid
# 5424180279791762 invalid