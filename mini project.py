# Input the first date
date1 = input("Enter date1 in format of dd/mm/year: ")
x = date1[0] + date1[1]  # Extract day
y = int(x)  # Convert day to integer
z = date1[3] + date1[4]  # Extract month
month1 = int(z)  # Convert month to integer
k = date1[6:len(date1)]  # Extract year
year1 = int(k)  # Convert year to integer

# Input the second date
date2 = input("Enter date2 in format of dd/mm/year: ")
a = date2[0] + date2[1]  # Extract day
b = int(a)  # Convert day to integer
c = date2[3] + date2[4]  # Extract month
month2 = int(c)  # Convert month to integer
d = date2[6:len(date2)]  # Extract year
year2 = int(d)  # Convert year to integer

# Function to check and print leap years
def leapyear(year1, year2):
    print("Leap-years: ")
    for i in range(year1, year2 + 1):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i, end=", ")
    print("\n")

# Function to check and print non-leap years
def nonleapyear(year1, year2):
    print("Non-leap years: ")
    for j in range(year1, year2 + 1):
        if not ((j % 4 == 0 and j % 100 != 0) or (j % 400 == 0)):
            print(j, end=", ")
    print("\n")

# Call the functions to display results
leapyear(year1, year2)
nonleapyear(year1, year2)
