#printing dictionary items (keys and values)

week_dict = {'Sunday': 'day1', 'Monday': 'day2', 'Tuesday': 'day3', 'Wednesday': 'day4', 'Thursday': 'day5', 'Friday': 'day6', 'Saturday': 'day7'}

#here in each item weekday is key and day1-day7 are values of the weekday. Let's print them

for key, value in week_dict.items():
    print(f'{key} is {value} of week')

