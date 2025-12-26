'''
Build a countdown calculator. 
Write some code that can take two dates as input, and then calculate the amount of time between them. 
This will be a great way to familiarize yourself with Python’s datetime module.
'''

from datetime import datetime

def first_date_input():
    while True:
      date1 = input("Enter the first date (YYYY-MM-DD):")
      try:
           dateobj = datetime.strptime(date1, "%Y-%m-%d")
           print(f"The following date is {dateobj.date()}")
           return dateobj
      except ValueError:
          print("There is wrong or invalid date entered!")

def second_date_input():
    while True:
      date2 = input("Enter the second date (YYYY-MM-DD):")
      try:
           dateobj = datetime.strptime(date2, "%Y-%m-%d")
           print(f"The following date is {dateobj.date()}")
           return dateobj
      except ValueError:
          print("There is wrong or invalid date entered!")

def main():

    start = first_date_input()
    end = second_date_input()

    delta = end - start

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    
    print(f"Time between dates: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    
if __name__ == "__main__":
    main()



        


