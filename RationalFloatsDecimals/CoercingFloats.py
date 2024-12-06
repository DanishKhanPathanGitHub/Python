import math
import fractions

print('trunc of 10.7: ', math.trunc(10.7))
print('floor of 10.7: ', math.floor(10.7))
#trunc will discard all numbers after decimal point
#floor will return max number <= float number
print('trunc of -10.2: ', math.trunc(-10.2))
print('floor of -10.2: ', math.floor(-10.2))
#for negative numbs max num <= number would be not same as pos nums
print('ceil of 10.3: ', math.ceil(10.3))
print('ceil of -10.3: ', math.ceil(-10.3)) 
#ceiling is exactly opposite of floor
#min num >= float num
print('round of -10.7: ', round(-10.7))
print('round of 10.7: ', round(10.7))
print('round of 10.77: ', round(10.77))
#round will do actual rounding, by default round to 10^0 = 1's multiplier
# Another way of saying - to integers, 1,2,3,...77,78....100 etc
# round(num, n), if n=1, it's 10^-1 = 0.1's multiplier
# Another way of saying 1 digit after decimal point, so n=rounding to n num after decimal point
print('round of 10.335 to 2 digit after dceimal: ', round(10.335, ndigits=2))
print('round of 10.325 to 2 digit after dceimal: ', round(10.325, ndigits=2))
#round uses banker rounding algorithm, here see...
# 10.335 -> 10.34 not 10.33 when equal distance
# 10.325 -> 10.32 not 10.33 when equal distance
# in one case it's rounding away zero(10.34)
# in one case it's rounding towards zero(10.32)
#because it preferes the even least digit when there's equal distance
#in banks for fair rounding of interest/money for both customer POV and bank's POV
#it's necessary to allow 50-50 rounding choice - away zero-towards zero
#as only towards zero rounding will round the number less than it's actual value
#as only away zero rounding will round the number more than it's actual value
#fair play would be allowing one rounding in some case and another rounding in other cases
print('round of -10.335 to 2 digit after dceimal: ', round(-10.335, 2))
print('round of -10.325 to 2 digit after dceimal: ', round(-10.325, 2))
