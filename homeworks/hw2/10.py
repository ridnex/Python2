day = int(input())
month = str(input())
list_month = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sign = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']
num_month = list_month.index(month)

if (num_month==0 and day >=20)or(num_month==1 and day<=18):
    print(sign[0])
elif num_month==1 or (num_month==2 and day<=20):
    print(sign[1])
elif num_month==2 or (num_month==3 and day<=19):
    print(sign[2])
elif num_month==3 or (num_month==4 and day<=20):
    print(sign[3])
elif num_month==4 or (num_month==5 and day<=20):
    print(sign[4])
elif num_month==5 or (num_month==6 and day<=22):
    print(sign[5])
elif num_month==6 or (num_month==7 and day<=22):
    print(sign[6])
elif num_month==7 or (num_month==8 and day<=22):
    print(sign[7])
elif num_month==8 or (num_month==9 and day<=22):
    print(sign[8])
elif num_month==9 or (num_month==10 and day<=21):
    print(sign[9])
elif num_month==10 or (num_month==11 and day<=21):
    print(sign[10])
else:
    print(sign[11])
