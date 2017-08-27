import fnmatch
import sys
import os

this_directory = os.path.dirname(os.path.realpath(__file__))
cpp_files = []
for root, dirnames, filenames in os.walk(os.path.join(this_directory, 'test')):
    for filename in fnmatch.filter(filenames, '*.cpp'):
        cpp_files.append(os.path.join(root, filename))

cpp_set = set(cpp_files)
arg_set = set(sys.argv[1:])
all_tests_built = cpp_set == arg_set

if all_tests_built:
    exit(0)
else:
    print("Missing Tests:")
    for test in cpp_set - arg_set:
        print(test)
    exit(1)
