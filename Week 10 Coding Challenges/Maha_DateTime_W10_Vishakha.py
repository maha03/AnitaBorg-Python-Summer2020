#print the date of all the Sundays of a specified year
import datetime
def Sunday_dates(year):
    first_date = datetime.date(year, 1, 1)
    days_to_firstSunday= 7 - first_date.isoweekday()
    date_of_firstSunday= first_date + datetime.timedelta(days_to_firstSunday)
    date_of_Sunday=date_of_firstSunday
    #count=0
    while date_of_Sunday.year == year:
        print(date_of_Sunday)
        #count+=1
        date_of_Sunday+=datetime.timedelta(7)
    #print(count)
Sunday_dates(int(input("Enter year")))
