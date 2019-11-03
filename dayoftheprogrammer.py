# Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the  day of the year) during a year in the inclusive range from  to .
#
# From  to , Russia's official calendar was the Julian calendar; since  they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in , when the next day after January  was February . This means that in , February  was the  day of the year in Russia.
#
# In both calendar systems, February is the only month with a variable amount of days; it has  days during a leap year, and  days during all other years. In the Julian calendar, leap years are divisible by ; in the Gregorian calendar, leap years are either of the following:
#
# Divisible by .
# Divisible by  and not divisible by .
# Given a year, , find the date of the  day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .
#
# For example, the given .  is divisible by , so it is a leap year. The  day of a leap year after  is September 12, so the answer is .
#
# Function Description
#
# Complete the dayOfProgrammer function in the editor below. It should return a string representing the date of the  day of the year given.
#
# dayOfProgrammer has the following parameter(s):
#
# year: an integer
# Input Format
#
# A single integer denoting year .
#
# Constraints
#
# Output Format
#
# Print the full date of Day of the Programmer during year  in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .
#
# Sample Input 0
#
# 2017
# Sample Output 0
#
# 13.09.2017
# Explanation 0
#
# In the year y=2017, January has 31 days, February has 28 days, March has 31 days, April has 30 days, May has 31 days, June has 30 days, July has 31 days, and August has 31 days. When we sum the total number of days in the first eight months, we get 31+28+31+30+31+30+31+31 = 243. Day of the Programmer is the 256th day, so then calculate 256-243=13 to determine that it falls on day 13 of the 9th  month (September). We then print the full date in the specified format, which is 13.09.2017.


def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year


year = 2007
print(solve(year))
