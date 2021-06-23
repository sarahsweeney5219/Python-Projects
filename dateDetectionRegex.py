#date detection regex
#uses regular expression to detect dates in the DD/MM/YYYY format (numbers must be in min-max range)
#then tests to see if it is a valid date (based on number of days in each month)

import re, calendar

#creating the DD/MM/YYYY regex
dateRegex = re.compile('(3[01]|[12][0-9]|0?[1-9])\/(0?[1-9]|1[012])\/([12][0-9][0-9][0-9])')

#asking user to input text
print('Please enter either a single date, a series of dates, or a body of text with dates contained in it.')
text = input()

matches = []
for groups in dateRegex.findall(text):
    date = '/'.join([groups[0], groups[1], groups[2]])
    matches.append(date)

print(matches)

if len(matches) > 0:
    print('These are the DD/MM/YYYY formatted dates in your input:')
    for match in matches:
        print(match)
    print('We will now proceed to see if they are valid days (according to the number of days in a month')
    validDates = []
    for match in matches:
        if match[3:5] in ['05', '06', '09', '11']:
            if int(match[0:2]) <= 30:
                validDates.append(match)
        elif match[3:5] == '02':
            #check to see if leap year
            if calendar.isleap(int(match[6:10])) == True:
                if int(match[0:2]) <= 29:
                    validDates.append(match)
            else:
                if int(match[0:2]) <= 28:
                    validDates.append(match)
        else:
            if int(match[0:2]) <= 31:
                validDates.append(match)
    print("Of your inputted dates, the following are valid:")
    for validDate in validDates:
        print(validDate)
else:
    print('There were no dates in your input.')


