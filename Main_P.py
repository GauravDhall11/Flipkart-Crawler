from Samsung import *
from Poco import *
from Apple import *
from Vivo import *
from Mi import *
list=['Samsung','Poco','Apple','Vivo','Mi']
print(list)
val=input("Enter Comapny name:")
print("You Entered",val)
if val == 'Samsung':
    display_text()
elif val == 'Poco':
    display_text2()
elif val == 'Apple':
    display_text3()
elif val == 'Vivo':
    display_text4()
elif val == 'Mi':
    display_text5()

