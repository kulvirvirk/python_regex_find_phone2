# 1. Create a regex object with pattern
# 2. use a findall() to find the phone number from string

import re

# 1. Create a regex object with pattern
#create a regex object. 
# So, here phone_regex contains our regex object, it defines the pattern we are trying to macth.
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# 2. use a findall() to find the phone number from string
# now we are calling a findall() method to search for pattern provided by phone_regex object
print(phone_regex.findall('Heloo, these are my two phone number: 999-444-2323 and 333-456-3333'))