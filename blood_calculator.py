#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:25:02 2023

@author: shaun
"""

def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        print("Program ending")

def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)
    
def HDL_input():
    HDL_value = input("Enter the HDL Result:")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int <= 159:
        answer = "Borderline High"
    elif 160 <= LDL_int <= 189:
        answer = "High"
    elif LDL_int >= 190:
        answer = "Very High"
    return answer

def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return

interface()
