from project6_helpers import *
import sys

if __name__=='__main__':
    # print(get_files_path())
    
    try:
        str_to_find=sys.argv[1]
        find_words_in_files(str_to_find)
    except:
        print('No argumet provided in the execution,\nExample:python project6.py "argument"')
    # print("\033[91mThis is red!\033[0m")