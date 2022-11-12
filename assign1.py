#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2021
Program: assign1.py (replace student_id with your Seneca User name)
Author: "Student Name"
The python code in this file (assign1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 
'''

import sys

def usage():
    "TODO enter docstring"
    pass # TODO: delete this line, replace with valid code.

def days_in_mon(month):
    "TODO enter docstring"
    # return days
    pass # TODO: delete this line, replace with valid code.

def valid_date(date):
    "TODO enter docstring"
    # return True or False 
    pass # TODO: delete this line, replace with valid code.

def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."

    lyear = year % 4 #
    if lyear == 0:
       feb_max = 29 # this is a leap year
    else:
        feb_max = 28 # this is not a leap year
    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year
    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year
    return feb_max

def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        feb_max = (leap_year(year))

        tmp_day = day + 1 # next day

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "pasted from 'after' and changed + to -, > to <"
    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        feb_max = (leap_year(year))

        tmp_day = day - 1 # next day

        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if tmp_day < mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month - 1
        else:
            to_day = tmp_day
            tmp_month = month - 0

        if tmp_month < 12:
            to_month = 1
            year = year - 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def dbda(start_date, num_days):
    # create a loop
    end_date = start_date
    while num_days != 0:
    # call before() or after() as appropriate
        if num_days > 0:
            end_date = after(end_date)
            num_days -= 1
            #print(num_days) #testing only
            #print(end_date) #testing only
    # return end_date
    return end_date

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    call = (dbda(sys.argv[1], int(sys.argv[2])))
    # output the result
    print(call)
