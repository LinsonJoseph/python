malayalam_months = ('Chingam', 'Kanni', 'Thulam', 'Vrishchikam', 'Dhanu', 'Makaram', 'Kumbham', 'Meenam', 'Meṭam', 'Eṭavam', 'Mithunam', 'Karkaṭakam')
tamil_months = ('Avani', 'Purattasi', 'Aippasi', 'Karthingal', 'Margazhi', 'Tahi', 'Maasi', 'Panguni', 'Chithirai', 'Vaikasi', 'Aani', 'Aadi')
gregorian_calendar = ('August-September', 'September–October', 'October–November', 'November–December', 'December–January', 'January–February', 'February–March', 'March–April', 'April–May', 'May–June', 'June–July', 'July–August')
north_sentinel_months = ('Jori', 'Kippa', 'Kasu', 'Morzia', 'Hamoosh', 'Chonnatu', 'Biksi', 'Vadurel', 'Ongatatu', 'Jobhipi', 'Onadai', 'Zebuchi', 'Yucheruyulyule', 'Odharil')
south_sentinel_months = ('Bisalluti', 'Chunwentu', 'Khamoi', 'Boshiga')

#Print malayalam_months
print("The Malayalam months are")
mm = 0
while(mm < len(malayalam_months)):
    print(malayalam_months[mm], end = ' ')
    mm += 1

print('\n')
#Print the name and lenght of the longest month name
print("Length of Imaginary names for calendar months of the North Sentenial Island inhabitants are")
l=[]
for i in range(len(north_sentinel_months)):
    l.append(len(north_sentinel_months[i]))
print(l)
print("Max among them is: ", max(l))

print()
#Compare Tamil months with Gregorian calendar months
print('A comparison for Tamil and Gregorian Calendar months')
for i in range(len(tamil_months)):
    print(f'{tamil_months[i]:<12} - {gregorian_calendar[i]}')

print()
#Print world month names in order
print('Small World month names in order')    
for i in gregorian_calendar, tamil_months, malayalam_months, north_sentinel_months, south_sentinel_months:
    print(i,'\n')
