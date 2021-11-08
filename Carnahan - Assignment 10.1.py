##############################################################################
# Author: Jacob Carnahan
# Class : CIS 245-T302
# Date : November 7, 2021
# Description:
#           Assignment 10.1 
##############################################################################
# Standard library imports
import os

# Local imports
from ContactRecord import ContactRecord

# Strings
dir_creation = "Directory doesn't exist, create it?"
file_overwrite = "File already exists, overwrite it?"

# Function defs ---------------------------------------------------------------
def user_consents_to(msg):
    '''
    Displays a message to user and takes/validates yes/no input. Spins until
    valid input is recieved.
    Returns:
        -True if user consents to prompt
        -False if user does not
    '''
    while True:
        response = input(msg + "(y/n) ")
        
        if response == 'Y' or response == 'y':
            return True
        elif response == 'N' or response == 'n':
            return False
        else:
            print("Please answer with y or n.\n")

def prompt_path():
    '''
    Prompts for a path relative to the CWD, checks if it exists, creates it
    if it doesn't.
    
    Chose to restrict directory creation to leaves off of the CWD to avoid 
    permission issues and accidental overwrites of important data.
    
    Returns:
        -The absolute path of the specified directory
    
    Exits:
        -If directory cannot be created
    '''
    abs_path = os.getcwd() # Get the current directory
    
    while True:
        print(f"Current Directory: {abs_path}")
        print("Enter a directory relative to current to save data in (blank to use current):")
        path = input("?>")
        
        if path == "":
            break # User wants to use current dir, nothing to do
        
        # Build up the full path...
        path = path.split(os.path.sep) 
        for element in path:
            abs_path = abs_path + os.path.sep + element
        # Check for existance...
        if os.path.isdir(abs_path):
            break # Dir exists, nothing else to do
        else: # Dir needs to be created...
            print(f"Entered path: {abs_path}\n")
            if user_consents_to(dir_creation):
                try:
                    os.makedirs(abs_path)
                except: # Something went wrong that I don't have time to fix...
                    print("Could not create directory. Exiting.")
                    exit()
                else:
                    break # Dir created successfully
                    
            else:
                print("Must specify a valid directory to save in. Try again.")
                
    return abs_path
        
def prompt_filename(path):
    '''
    Asks for a filename to save data to, checks if it conflicts with a directory
    name, checks if the file already exists, and prompts if the user wishes to
    overwrite the file if it does.
    
    Returns:
        -Absolute pathname of the file the user wishes to use
    '''
    while True:
        filename = input("Enter a filename for save data: ")
        
        if filename == "":
            print("Must specify a file to save to. Try again.")
            continue
        
        # Build an absolute path to the file
        abs_path = path + os.path.sep + filename
        
        # Make sure the name doesn't conflict with a directory name...
        if os.path.isdir(abs_path):
            print("There is a directory with that name already. Try again.")
            continue
            
        # Check if file already exists...
        if os.path.isfile(abs_path):
            if user_consents_to(file_overwrite): #
                break
            else:
                print("Must specify a file to save to. Try again.")
                continue
        
        else: #File doesn't exist, should be able to create it later
            break
            
    return abs_path
    
    
# Main program ----------------------------------------------------------------
# Get path information for later use
print("This program saves data to a specified location. Please follow the prompts.\n")
dir_path = prompt_path()
full_path = prompt_filename(dir_path)

# Create two new ContactRecord objects, one to write and one to read with 
write_record = ContactRecord()
read_record = ContactRecord()

# Build up the data to write out
write_record.inputName("Please enter your full name")
write_record.inputAddress("Please enter your address")
write_record.inputPhoneNumber("Please enter your phone number")
# Write to our file
write_record.writeRecord(full_path)

# Read from our file with separate object
read_record.readRecord(full_path)

print("\n\nYou entered:")    
read_record.printRecord()