"""
The most common use of context managers is the proper management of resources.
We want to open, read, write, and close files correctly. 
Otherwise, the operating system may eventually throw an error and we may leak resources.

The 'with' statement ensures that the open file descriptor is closed automatically.
It takes the place of the try, except, finally blocks. It also makes the code more readable.

1) I will use a short quote by Napoleon to highlight an example.
2) Say we want to create a Notebook class to function as a context manager. 
It will open a notebook and write to it. For this it needs an __enter__ and
an __exit__ method. With these, the class follows the context manager protocol
and supports the 'with' statement.
"""

# 1
with open('Napoleon_quote.txt', 'w') as quote:
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


# 2
class Notebook:
    def __init__(self, notebook_name):
        self.notebook_name = notebook_name

    def __enter__(self):
        self.notebook = open(self.notebook_name, 'w')
        return self.notebook
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.notebook:
            self.notebook.close()


if __name__ == "__main__":
    
    with Notebook('quote.txt') as quote:
        quote = """
                The battlefield is a scene of constant chaos.
                The winner will be the one who controls that chaos,
                both his own and the enemy's.
                """