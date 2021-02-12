'''
Script to generate Covid-19 data -
Cases Data
    Country -
    State
    Date
    Case Type
    Case Count
Death Data
    Date
    Age
Weather Data
    Country
    State
    Date
    Temperature
    Weather
'''

import datetime
from datetime import datetime
from datetime import timedelta
from random import seed
from random import randint

# seed random number generator
seed(1)

start_date = datetime.strptime('01/03/2020', '%d/%m/%Y')
end_date = datetime.now()

country = 'Germany'
state = 'Bayern'

case_type = ['ACTIVE','RECOVERED','DEATH']
weather =  ['SUNNY','CLOUDY','WINDY','SNOW','RAIN']

case_rcrd = ''
age_rcrd = ''
weather_rcrd = ''

while start_date <= end_date:
    new_active_cnt = randint(0, 10000)
    new_rec_cnt = randint(0, 2000)
    new_death_cnt = randint(0, 1000)

    cases_cnt= {'ACTIVE':new_active_cnt,'RECOVERED':new_rec_cnt,'DEATH':new_death_cnt}

    for curr_case_type in case_type:
        new_case_cnt = cases_cnt[curr_case_type]
        case_rcrd = case_rcrd + f'{country},{state},{start_date},{curr_case_type},{new_case_cnt}\n'

    death_case_no = 0

    while death_case_no < new_death_cnt:
        rand_age = randint(1, 100)
        age_rcrd = age_rcrd + f'{country},{state},{start_date},{rand_age}\n'
        death_case_no+=1

    todays_temp = randint(-15,30)
    rand_weather_index = randint(0,4)
    weather_rcrd = weather_rcrd + f'{country},{state},{start_date},{todays_temp},{weather[rand_weather_index]}\n'

    start_date = start_date + timedelta(days=1)

with open('cases_data.csv', mode = 'w') as cases:
        cases.write(case_rcrd)

with open('deaths_data.csv', mode='w') as deaths:
    deaths.write(age_rcrd)

with open('weathers_data.csv', mode='w') as weather:
    weather.write(weather_rcrd)