# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'tests')))

from test_sample import test_true

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test_true()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
