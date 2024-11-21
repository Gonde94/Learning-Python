"""
The most common use of context managers is the proper management of resources.
We want to open, read, write, and close files correctly. 
Otherwise, the operating system may eventually throw an error and we may leak resources.

The 'with' statement ensures that the open file descriptor is closed automatically.
It takes the place of the try, except, finally blocks. It also makes the code more readable.

We will use a short quote by Napoleon as an example. 
"""

with open('Napoleon_quote.txt') as quote:
    quote.write("""
                The battlefield is a scene of constant chaos.
                The winner will be the one who controls that chaos,
                both his own and the enemy's.
                """)
    
# This is equivalent to:
#quote = open('quote.txt', 'w')
#try:
#    quote.write("""
#                The battlefield is a scene of constant chaos.
#                The winner will be the one who controls that chaos,
#                both his own and the enemy's.
#                """)
#finally:
#    quote.close()