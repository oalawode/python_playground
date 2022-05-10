"""
This code accepts two different years and returns 
an output of the number and a list of leap years between those years.

"""

# Prompt user to enter the two different years
start_year = int(input('Enter start year and press enter: '))
end_year = int(input('Enter end year and press enter: '))

# Initialise empty list
leap_year_list = []


for year in range(start_year, end_year):
    if year % 2 == 0:
        if year % 4 == 0:
            if (year % 100 != 0) & (year % 400 != 0):
                leap_year_list.append(year)


# Using list comprehension, the below code does the same as that above. But for readability purpose, the above code is preferred.
# leap_year_list = [ year for year in range(start_year, end_year) if year % 2 == 0: if year % 4 == 0: if (year % 100 != 0) & (year % 400 != 0)]

# Print the number of leap years between the years
print(f'There are {len(leap_year_list)} leap years between {start_year} and {end_year}')  

# Print a list of the leap years
print(*leap_year_list, sep=", ")
