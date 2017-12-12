import os
import fnmatch

try:
    input = raw_input
except NameError:
    pass

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

path = input('Enter directory to search: ')
print("Will search " + path + " directory.")

outputFile = input('Enter output file name: ')
outputFile = outputFile + ".txt"
print("File name will be " + outputFile)

with open(outputFile, 'w') as f1:
    for filename in find_files(path, 'strings.xml'):
        print 'Found string source:', filename
        for line in open(filename, 'r'):
            if '<string' in line:
                print(line)
                f1.write(line)
