from re import search
from turtle import clear
from easygui import *
import sys

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results
    
def file_search(file):
    from csv import writer

    print('*** Search for multiple strings in a file and get lines containing string along with line numbers ***')
    # search for given strings in the file 'C:\Users\rebec\OneDrive\Desktop\test.txt.txt"
    # try:
    #         file_loc = input ("Enter file search location : ")
    # except:
    #      print('Wrong input. Please enter a file location....')
        # Check what choice was entered and act accordingly
    matched_lines = search_multiple_strings_in_file(file, ['authentication', 'password', 'token', '@ait.com'])

   

    keyword_ttl = len(matched_lines)

    print('Total  instances of keywords observed :', keyword_ttl)
    # open a file (file_output.csv) and write a header
    with open('file_output.csv', 'a', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Exposure Keyword', 'Line No.', 'Full Line', 'Keyword Instance Total']
        thewriter.writerow(header)

        for elem in matched_lines:
            exposure_keyword = elem[0]
            line_num = elem[1]
            full_line = elem[2]
        

            out1 = print('Exposure keyword *',elem[0],'* has been identified on line', elem[1], '- Full line = ', elem[2])      
            info_out = [exposure_keyword, line_num, full_line, keyword_ttl]            
            thewriter.writerow(info_out)
            codebox(out1)
           
            

    if __name__ == '__file_search__':
        file_search()

    print('Please be aware of the following:')
    print('1: If there are references to passwords/tokens - confirm if they are active and rotate them if so')
    print('2: if there are references to authentication, verify if is potentially a legitimate authentication form (token or key)')
    print('3: if there is references to personal information - inform the relevant Privacy office / team contacts')    
    

msg = "What is your favorite Subject"
title = "Choose your favourite"
choices=['File Search','Search Zip File','Web Scraping','Exit']
choice=buttonbox(msg, title,choices)
if choice=='File Search':
    msgbox("File Search")
    # try:
    #     file_to_search = input ("File to search: ")
    # except:
    #      print('Wrong input. Please Website url....')
        # Check what choice was entered and act accordingly
    file_to_search = enterbox("Enter File to search")    
    file_search(file_to_search)

elif choice=='Chemistry':
    msgbox("I like Chemistry")
elif choice=='Maths':
    msgbox("Math is fun")
elif choice=='Other':
    msgbox("Ohh thats sad! Your favourite subject is not in the list")
elif choice=='Exit':    
    msgbox("Sorry to see you go")
    sys.exit(0)
