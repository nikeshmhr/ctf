# My Approach
# ---------------------
# import sys
# import hashlib

# salt = 'f789bbc328a3d1a3'
# matchPrefix = '0e'

# if len(sys.argv) < 2:
#     print("Usage: ./magic-hash-generator.py path_to_wordlist")
#     exit()

# with open(sys.argv[1]) as infile:
#     for line in infile:
#         try:
#             password = line.split()[0]
#             # print('Trying ' + password)
#             toHash = str(salt + password).encode('utf-8')
#             hashed = hashlib.md5(toHash).hexdigest()
#             if hashed.startswith(matchPrefix):
#                 if hashed[2:].isnumeric():
#                     print(password)
#         except:
#             print(line)

# From write up
from itertools import product
import hashlib # Import the modules
for x in range(0, 10): # Iterate through the lengths
        for combo in product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=x): # For each combination in this alphabet with this length
                result = hashlib.md5(("f789bbc328a3d1a3" + ''.join(combo)).encode('utf-8')).hexdigest() # Generate the result
                if result.startswith("0e") and result[2:].isdigit(): # Check if result matches our requirements
                        print("f789bbc328a3d1a3" + ''.join(combo)) # If it does print out the string
                else:
                        pass #If not pass