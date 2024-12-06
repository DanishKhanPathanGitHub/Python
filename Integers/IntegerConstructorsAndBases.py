print(int("1Aa0", base=11))
print(int("1aa0", base=11))
#Python use insensetive character representation for different bases. 
#means a and A, z and Z will have same value
print(int(0o672)) #base8
try:
    print(int("1Ba0", base=11))
except:
    print("""for base 11 it will support character only a and A, 
    we have 26 characters, so total possible bases will be 10+26=36""")
print(int(0xFF)) #base16

#Code for conversion from base 10 to n
def from_bas10(number, base):
    if number < 0:
        raise ValueError("number must be positive")
    if base < 2 or base > 36:
        raise ValueError("base must be of 2 or greater than 2 and less than 36")
    if number == 0:
        return [0]
    
    digits = []

    while number > 0:
        number, mod = divmod(number, base)
        digits.insert(0, mod)
    print(digits)
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("Does not support this number in this base")
    '''
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding
    '''
    return ''.join([digit_map[d] for d in digits])

def base_change_from10(number, base):
    digits_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sign = -1 if number < 0 else 1
    number*=sign

    digits = from_bas10(number,base)
    encoded_number = encode(digits, digits_map)
    return encoded_number if sign == 1 else '-'+encoded_number

print(base_change_from10(5, 2))
