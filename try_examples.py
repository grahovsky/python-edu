import sys

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')
except:
    print('Some other error occurred.')

try:
    1/0
except:
    err = sys.exc_info()
    print(err)

try:
    2/0
except Exception as err:
    print(type(err))
    print(err)
