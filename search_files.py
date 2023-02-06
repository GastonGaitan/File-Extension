import sys
import os
arguments = sys.argv

help = '''
This program will look for files within a directory depending on the extension given as argument.
python find_files "directory" extension
As a good practice, if the directions contains any folder with spaces, use "" to sorround the direction.
For instance: python search_files "desktop/python" exe
'''

if arguments[1] == "-help" or arguments[1] == '-h':
    print(help)
else:
    try:
        directory = arguments[1]
        extension = arguments[2]
    except IndexError:
        print("There has been an error. Please enter the folder direction and the extension from the files you want to look for.")
    else:
        try:
            files = os.listdir(directory)
        except FileNotFoundError:
            print("The route specified does not exist.")

        file_list = []

        for file in files:
            if file.split('.')[1] == extension:
                file_list.append(file)

        if len(file_list) == 0:
            print(f"No files with the extension {extension} on the director specified.")

        else:
            print(f'Files with the extension {extension} within the folder "{directory}":')
            for file in file_list:
                print(file)





























