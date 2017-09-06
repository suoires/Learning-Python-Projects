ccn = input("Enter your credit card here:")


def credit_validator(ccn):
    splitted_ccn = list(map(int, ccn))
    first_15 = splitted_ccn[0:]
    first_15_x2 = first_15
    first_15_x2[::2] = [i*2 for i in first_15[::2]]
    first_15_x2_replace= [sum(map(int, str(x))) if x>=10 else x for x in first_15_x2]
    total = sum(first_15_x2_replace)
    if total %10 == 0:
        print ("This credit card is valid!")
    else:
        print ("This credit card is NOT valid!")
    return total
        

print (credit_validator(ccn))

def creditcard_identifier(ccn):
    ccn = list(map(int, ccn))
    print (ccn[0])
    if ccn[0] == 1 or ccn[0] ==2:
        print("Airlines Credit Card")
    elif ccn[0] == 3:
        print("Travel Credit Card")
    elif ccn[0] == 4 or ccn[0] ==5:
        print("Banking and Financial Credit Card")
    elif ccn[0] == 6:
        print("Merchandising Credit Card")
    elif ccn[0] == 7:
        print("Petroleum Credit Card")
    elif ccn[0] == 8:
        print("Health Care/Telecommunications Credit Card")
    elif ccn[0] == 9:
        print("National Assignment Credit Card")
    else: 
        print("Weird Card")

creditcard_identifier(ccn)

def account_num_identifier(ccn):
    ccn = list(map(int, ccn))
    print("Your account number is: {}".format(ccn[6:]))

account_num_identifier(ccn)
