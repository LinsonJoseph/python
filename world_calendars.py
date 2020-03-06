malayalam_months = ['Chingam', 'Kanni', 'Thulam', 'Vrishchikam', 'Dhanu', 'Makaram', 'Kumbham', 'Meenam', 'Meṭam', 'Eṭavam', 'Mithunam', 'Karkaṭakam']
tamil_months = ['Avani', 'Purattasi', 'Aippasi', 'Karthingal', 'Margazhi', 'Tahi', 'Maasi', 'Panguni', 'Chithirai', 'Vaikasi', 'Aani', 'Aadi']
gregorian_calendar = ['August-September', 'September–October', 'October–November', 'November–December', 'December–January', 'January–February', 'February–March', 'March–April', 'April–May', 'May–June', 'June–July', 'July–August']
north_sentinel_months = ['Jori', 'Kippa', 'Kasu', 'Morzia', 'Hamoosh', 'Chonnatu', 'Biksi', 'Vadurel', 'Ongatatu', 'Jobhipi', 'Onadai', 'Zebuchi', 'Yucheruyulyule', 'Odharil']
south_sentinel_months = ['Bisalluti', 'Chunwentu', 'Khamoi', 'Boshiga']

mm = 0
while(mm < len(malayalam_months)):
    print(malayalam_months[mm])
    mm += 1

l=[]
for i in range(len(tamil_months)):
    #print(tamil_months[i] + ' ' +gregorian_calendar[i])
    l.append(len(gregorian_calendar[i]))
print(max(l))
print(l)



for i in gregorian_calendar, tamil_months, malayalam_months, north_sentinel_months, south_sentinel_months:
    print(i)
#    print("\n\n", slice(gregorian_calendar), slice(tamil_months))
