from re import search
from turtle import clear
from csv import writer
import os
import sys
import csv


menu_options = {
    1: 'File Search',
    2: 'Search Zip File',
    3: 'Web Scraping',
    4: 'Generate Report',
    5: 'Exit',
}

with open('file_output.csv', 'a+', encoding='utf8', newline='') as f:
        thewriter = writer(f)  
        header = ['Exposure Keyword', 'Line No.', 'Full Line', 'Filename', 'No. Keywords']           
        thewriter.writerow(header)
        f.close()

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
    global keyword_file_ttl
    keyword_file_ttl = 0
    keyword_ttl = 0
    print('*** Search for multiple strings in a file and get lines containing string along with line numbers ***')
    # search for given strings in the file 'C:\Users\rebec\OneDrive\Desktop\test.txt.txt"
    # try:
    #         file_loc = input ("Enter file search location : ")
    # except:
    #      print('Wrong input. Please enter a file location....')
    # Check what choice was entered and act accordingly 
    
    search_array = ['authentication', 'password', 'token', '@ait.com']
    

    matched_lines = search_multiple_strings_in_file(file, search_array)
      
   
    keyword_ttl = keyword_ttl + len(matched_lines)

    #print('Total  instances of keywords observed :', keyword_ttl)
    # open a file (file_output.csv) and write a header
   
    with open('file_output.csv', 'a+', encoding='utf8', newline='') as f:
        thewriter = writer(f)            
       
        exposure_keyword = ''
        line_num = ''
        full_line = ''

        for elem in matched_lines:
            exposure_keyword = elem[0]
            line_num = str(elem[1])
            full_line = elem[2]
            # keyword_ttl = 0
            # keyword_ttl += len(matched_lines)
            keyword_file_ttl = keyword_ttl + 1

            print('Exposure keyword *',elem[0],'* has been identified on line', elem[1], '- Full line = ', elem[2])      
            info_out = [exposure_keyword, line_num, full_line, file, 1]            
            thewriter.writerow(info_out)
            info_out_ttl = [" ", " ", " ", "File Keyword Total", keyword_ttl]

    with open('file_output.csv', 'a+', encoding='utf8', newline='') as f:
        thewriter = writer(f)            
        thewriter.writerow(info_out_ttl)
            

    if __name__ == '__file_search__':
        file_search()

    print('Please be aware of the following:')
    print('1: If there are references to passwords/tokens - confirm if they are active and rotate them if so')
    print('2: if there are references to authentication, verify if is potentially a legitimate authentication form (token or key)')
    print('3: if there is references to personal information - inform the relevant Privacy office / team contacts')    
    

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    print('Search File')
    if os.path.exists('file_output.csv'):
        os.remove('file_output.csv')
    if os.path.exists('report.html'):
       os.remove('report.html')

    print('File Search Example file: test.txt')

    try:
        file_to_search = input ("Enter File to search: ")
    except:
         print('Wrong input. Please Website url....')
        # Check what choice was entered and act accordingly
    file_search(file_to_search)
    
def option2():
    print('Search Zip File')
    
    # importing required modules
    from zipfile import ZipFile
    import os 
    from os.path import isfile, join
    from os import listdir
    from pprint import pprint

    if os.path.exists('file_output.csv'):
        os.remove('file_output.csv')
    if os.path.exists('report.html'):
       os.remove('report.html')

    print('Zip Search Example file: test_zip.zip')
    try:
        
        zip_file_to_search = ''
        zip_file_to_search = input ("Enter Zip File to search: ")    
        if zip_file_to_search.lower().endswith('.zip'):         
            # specifying the zip file name
            file_name = zip_file_to_search
            ext_file_name = ""
        #zip_folder_path = 'C:\projects\data_breach\zip'
                   
    except:
        print('Wrong input. Please enter a zip file....')
        option2()
        #sys.exit
        # Check what choice was entered and act accordingly
   
    
    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
    
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall('C:\_Projects\PII_Search_Utility')
        print('Done!')

        print(os.listdir('C:\_Projects\PII_Search_Utility\zip'))

        zip_files = [f for f in listdir('C:\_Projects\PII_Search_Utility\zip') if isfile(join('C:\_Projects\PII_Search_Utility\zip', f))]
        
        for ext_file_name in zip_files:
            print('* Checking File: ' + ext_file_name)
            file_search(ext_file_name)




def option3():
    print('Scrape Website/HTML File')
     
    from bs4 import BeautifulSoup
    import requests
    from csv import writer
    import re
    
    if os.path.exists('file_output.csv'):
        os.remove('file_output.csv')
    if os.path.exists('report.html'):
       os.remove('report.html')

    print('Web Scrape Example file: test.html')
    try:
        url = input ("Enter website Search URL: ")
    except:
        print('Wrong input. Please Website url....')
    # Check what choice was entered and act accordingly
     
     
    
   
    with open(url) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        # soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('p')
        fp.close()
    
    with open('file_output.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Web Scrape - Exposed Keyword']
        thewriter.writerow(header)

        str_matches = [s for s in lists if s.__contains__("password") or ("authentication") or ("token") or ("@ait.com")]
        for str_match in str_matches:

            #clean = re.compile('<.*?>')
            #str_match = re.sub(clean, '', str_match)
            thewriter.writerow(str_match)

def option4():
    # import libraries
    import urllib
    import urllib.request
    import pandas as pd
    import subprocess
    import os

    file = pd.read_csv("file_output.csv")
    file.to_html("filedump.html")

    #input file
    f_in = open("filedump.html", "rt")
    #output file to write the result to
    f_out = open("report.html", "wt")

    f_out.seek(0) #get to the first position
    f_out.write('<head><link rel="stylesheet" href="styles.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><p class="heading">Summary Report of PII data</p>')


    #for each line in the input file
    for line in f_in:
	    #read replace the string and write to output file
	    f_out.write(line.replace('dataframe', 'GenericTable'))
    #close input and output files
    f_in.close()
    f_out.close()

    os.remove("filedump.html")
    url = "C:\_Projects\PII_Search_Utility/report.html"
    # or a file on your computer
    # url = "/Users/yourusername/Desktop/index.html
    try: # Windows Browser
        os.startfile(url)
    except: 
        print('Wrong url input. Please enter Website url....')
        
def option5():
    print('Exiting search application')
    #os.copy()
    if os.path.exists('file_output.csv'):
        os.remove('file_output.csv')
    if os.path.exists('report.html'):
       os.remove('report.html')
    sys.exit(0)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Input error. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            #print('Generating Report')
            option4()
        elif option == 5:
            #print('Exiting Search Application')
            option5()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')