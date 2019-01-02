import pictorem as pct
import lib
import log
import datetime
from sys import argv
import time
import random


def main():
    current_year = datetime.datetime.today().year
    user_id = lib.work_on_args(argv)

    info = lib.user_get(user_id)
    time.sleep(0.3)
    friends = lib.friends_get(user_id)['items']

    name = info['first_name'] + ' ' + info['last_name']
    link = 'https://vk.com/' + info['domain']

    cities = []
    ages = []
    sexes = []
    last_names = []

    for friend in friends:
        try:
            cities.append(friend['city']['title'])

        except:
            pass

        try:
            bdate = friend['bdate']
            bdate_splited = bdate.split('.')

            if len(bdate_splited) == 3:
                byear = int(bdate_splited[2])

                if (current_year - byear) < 70:
                    ages.append(str(current_year - byear))

        except:
            pass

        try:
            sex = friend['sex']

            if sex == 1:
                sex = 'Female'
                sexes.append(sex)

            elif sex == 2:
                sex = 'Male'
                sexes.append(sex)


        except:
            pass

        last_names.append(friend['last_name'])

    max = lib.get_max_count_of_same_elements(cities)
    possible_city = lib.get_possible(cities, max)

    max = lib.get_max_count_of_same_elements(ages)
    possible_age = lib.get_possible(ages, max)

    max = lib.get_max_count_of_same_elements(sexes)
    possible_sex = lib.get_possible(sexes, max)

    max = lib.get_max_count_of_same_elements(last_names)
    possible_last_name = lib.get_possible(last_names, max)

    tab = '     '

    title = tab + 'Report for ' + name + ' (' + link + ')'

    frame_color = random.choice(['red', 'green', 'yellow', 'blue', 'light_blue', 'purple'])
    frame = lib.get_frame(tab, title, frame_color)

    print()
    print(title)
    print()
    print(frame)
    print()
    print(tab + pct.green.bold('Possible last name: ') + possible_last_name)
    print(tab + pct.green.bold('Possible age: ') + possible_age)
    print(tab + pct.green.bold('Possible city: ') + possible_city)
    print(tab + pct.green.bold('Possible sex: ') + possible_sex)
    print()
    print(frame)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print()
        log.info('Interrupted by user')
        exit(0)
