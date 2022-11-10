import pandas as pd 
import matplotlib as mp
import matplotlib.pyplot as plt
import openpyxl
data = pd.read_csv('ds_salaries.csv')

def print_full_data(data):
    print(data)
#--------------------------------------------------describe-------------------------------------------------------------------

def print_describe(data):
    print(data.describe())

def number_rows(data):
    return(len(data))
#----------------------------------------------columns-----------------------------------------------------------------------

def number_columns(data):
    return len(data.columns)
#-------------------------------------------------shape--------------------------------------------------------------------

def row_column(data):
    return data.shape
#---------------------------------------------to_string------------------------------------------------------------------------

def print_col(column, data):
    var = data[f'{column}'].to_string(index=False)
    return var

def info_by_country(country , data):
    rslt = data[data['employee_residence'] == country]
    return rslt
#----------------------------------------------sort_values-----------------------------------------------------------------------

def big_salary_in_country(country, data):
    selected_country = data[data['employee_residence'] == country]
    sorted = selected_country.sort_values(by=['salary'],ascending=False)

    salary = sorted['salary']

    return salary.head(1)
#-------------------------------------------where--------------------------------------------------------------------------

def more_salary_to_the_best(data, country):
    selected_country = data[data['employee_residence'] == country]
    sorted = selected_country.sort_values(by=['salary'],ascending=False)

    salary = sorted['salary']
    m = salary>100000
    salary.where(m, 2*salary)
    return salary


def salary_in_currency(currency, data):
    selected_country = data[data['salary_currency'] == currency]
    sorted = selected_country.sort_values(by=['salary'],ascending=False)

    salary = sorted[['salary', 'salary_currency']]

    return salary
#-----------------------------------------------------selecting with condintion---------------------------------------------------------------

def number_workers_ofline(data):
    ofline = data[data['remote_ratio']==100]
    number  = len(ofline)
    return number

def number_workers_combo(data):
    combo = data[data['remote_ratio']==50]
    number  = len(combo)
    return number

def number_workers_online(data):
    online = data[data['remote_ratio'] == 0]
    number  = len(online)
    # return f"{number} employees works online "
    return number

def workers_level_country_job(level, job_title,country ):
    selected_country = data[data['employee_residence'] == country ]
    selected_level = selected_country[selected_country['experience_level']==level]
    selected_job = selected_level[selected_level['job_title'] == job_title]
    return selected_job
#---------------------------------------------------value_counts------------------------------------------------------------------

def count_by_salary(data):
    item = data["salary"].value_counts()
    return item
#--------------------------------------------------------to excel-------------------------------------------------------------

def make_excel(data):
    data.to_excel("output.xlsx")  
#--------------------------------------------------------min-------------------------------------------------------------

def min_salary_in_country(country, data):
    selected_country = data[data['employee_residence'] == country]
    item = selected_country["salary"].min()
    return item

#---------------------------------------------------------pie chart----------------------------------------------
labels = 'Ofline_worker', 'Online_worker', 'Combo_worker'
sizes = [number_workers_ofline(data), number_workers_online(data), number_workers_combo(data)]
explode = (0, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()
#---------------------------------------------------------------------------------------------------------------------

# print(number_rows(data))
# print(number_columns(data))
# print(row_column(data))
# print(print_col('employee_residence', data))
# print(info_by_country('CA', data))
# print(big_salary_in_country('CA' ,data))
# print(salary_in_currency('EUR', data))
# print(number_workers_online(data))
# print(workers_level_country_job('SE', 'Data Scientist', 'US'))
# print(count_by_salary(data))
#print(min_salary_in_country('US', data))
# print(more_salary_to_the_best(data, 'US'))
#print(number_workers_ofline(data))
make_excel(data)