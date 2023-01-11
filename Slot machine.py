# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:21:21 2023

@author: DELL
"""

# Slot Machine

def deposit():
    while True:
        amount = input("What would you like to deposit?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must ne greater than zero.")
        else:
            print("Please enter a number.")
    return amount

deposit()