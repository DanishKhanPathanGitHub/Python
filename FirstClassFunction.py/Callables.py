#Every function/method and class object is callable 
print('print callable', callable(print))
print('int callable', callable(int))
print('int object callable', callable(10))
print('str callable', callable(str))
print('str object callable', callable('danish'))
print('str method callable', callable(str.upper))
print('List callable ',callable(list))
print('List object callable', callable([1,2,3]))

