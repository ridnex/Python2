month = int(input("month: "))
day = int(input('day: '))
list_month = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_str = list_month[month-1]
season_num = list_month.index(month_str)
if season_num<2 or season_num==11:
    season = 'Winter'
elif season_num<5:
    season = 'Spring'
elif season_num<8:
    season = 'Summer'
else:
    season = "Autumn"
print(month_str + ' , ' + str(day) + '. ' + 'Season is '+season )

