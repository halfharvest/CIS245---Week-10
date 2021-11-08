##############################################################################
# Author: Jacob Carnahan
# Class : CIS 245-T302
# Date : November 7, 2021
# File : ContactRecord.py
# Description:
#           Assignment 10.1 
##############################################################################

import re

class ContactRecord:
    '''
    Class that holds contact information.
    '''
    def __init__(self, name=None, address=None, phoneNumber=None):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        
    def getName(self):
        return self.name
        
    def getAddress(self):
        return self.address
        
    def getPhoneNumber(self):
        return self.phoneNumber
        
    def inputName(self, msg):
        '''
        Method that prompts for, inputs, and performs weak validation on a name.
        Sets the member variable "name" to input.
        '''
        while True:
            uinput = input(msg + ": ")
            # Check to see if we have at least a first and last name:
            if len(uinput.split()) >= 2:
                break
            else:
                print("Must enter at least first and last name. Try again.\n")
        
        self.name = uinput
    
    def inputAddress(self, msg):
        '''
        Method that prompts for and inputs an address.
        Sets the member variable "address" to input.
        '''
        
        uinput = input(msg + ": ")
        
        self.address = uinput
    
    def inputPhoneNumber(self, msg):
        '''
        Method that prompts for, inputs, and validates a phone number.
        Sets the member variable "phoneNumber" to validated input.
        '''
        rexp = "\d{3}-\d{3}-\d{4}"
        
        while True:
            uinput = input(msg + " (expected format: ###-###-####): ")
            
            if re.search(rexp, uinput):
                break
            else:
                print("Invalid input. Please enter again.\n")
        
        self.phoneNumber = uinput
    
    def writeRecord(self, path, mode='w'):
        '''
        Method to write a complete record to file.
        '''
        if self.name == None or self.address == None or self.phoneNumber == None:
            raise Exception("Missing data.")
        
        try:    
            with open(path, mode) as f:
                f.write(f"{self.name}, {self.address}, {self.phoneNumber}\n")
        except FileNotFoundError:
            print(f"File at {path} does not exist.")
            exit()
        except:
            print("Unspecified exception occured.")
            exit()
        
    
    def readRecord(self, path):
        '''
        Method to read a in record from a file.
        '''
        try:
            with open(path) as f:
                record = f.readline()
        except FileNotFoundError:
            print(f"File at {path} does not exist.")
            exit()
        except: # Implement more as needed/discovered
            print("Unspecified exception occured.")
            exit()
                
        record = record.split(",")
        
        self.name = record[0].strip()
        self.address = record[1].strip()
        self.phoneNumber = record[2].strip()
        
    def printRecord(self):
        '''
        Method to display the contents of a record.
        '''
        out_str = (
            f"Name: {self.name}\n" 
            f"Address: {self.address}\n"
            f"Phone Number: {self.phoneNumber}"
            )
            
        print(out_str)
        
        
        