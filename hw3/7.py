from distutils.filelist import findall
import re
a = str(input())
pattern = r'[1-9]{1,2}'
x = re.findall(pattern, a)
day = x[0]
y = re.findall(r'[0-9]{4}$', a)
year = y[0][-2:]

month = ['JAN', 'FEB', "MAR", 'APR', "MAY", "JUN", "JUL", 'AUG', 'SEP', "OCT", 'NOV', "DEC"]
mon = a[:3].upper()
for i in range(12):
    if month[i]==mon:
        m = int(i+1)
        print(f'{m}\{day}\{year}')

