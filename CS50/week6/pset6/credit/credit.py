
# Prompt User for Credit Card Number
def main():
    while True:
        card_num = int(input("Card Number: "))
        if card_num >= 0:
            break

    if check_v(card_num):
        print_card_brand(card_num)
    else:
        print("INVALID")
        
        

def check_v(ccn):
    return checksum(ccn)
    
    
    
    
    
def checksum(ccn):
    
    sum = 0
    for i in range(len(str(ccn))):
        if(i % 2 == 0):
            sum += ccn % 10
        else:
            digit = 2 * (ccn % 10)
            sum += digit // 10 + digit % 10
        
        ccn //= 10
        
    return sum % 10 == 0

def print_card_brand(ccn):
    
    if (ccn >= 34e13 and ccn < 35e13) or (ccn >= 37e13 and ccn < 38e13):
        print("AMEX")
    elif (ccn >= 51e14 and ccn < 56e14):
        print("MASTERCARD")
    elif (ccn >= 4e12 and ccn < 5e12) or (ccn >= 4e15 and ccn < 5e15):
        print("VISA")
    else:
        print("INVALID")




if __name__ == "__main__":
    main()