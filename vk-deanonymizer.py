from libs import log, pictorem as pct, lib
import datetime
from sys import argv
import time
import random
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='VK Deanonymizer v 1.1')

    required = parser.add_argument_group('required arguments')
    required.add_argument('--user-id', '-u', required=True, help='Target user_id', type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    user_id = args.user_id
    current_year = datetime.datetime.today().year

    info = lib.user_get(user_id)
    time.sleep(1/3)
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

        except Exception:
            pass

        try:
            bdate = friend['bdate']
            bdate_splited = bdate.split('.')

            if len(bdate_splited) == 3:
                byear = int(bdate_splited[2])

                if (current_year - byear) < 70:
                    ages.append(str(current_year - byear))

        except Exception:
            pass

        try:
            sex = friend['sex']

            if sex == 1:
                sex = 'Female'
                sexes.append(sex)

            elif sex == 2:
                sex = 'Male'
                sexes.append(sex)


        except Exception:
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
    print(tab + pct.yellow.bold('Computational information:'))
    print(frame)
    print()

    try:
        print(tab + pct.green.bold('Registration date: ') + lib.get_reg_date(user_id))
    except Exception: pass

    print(tab + pct.green.bold('Possible last name: ') + possible_last_name)
    print(tab + pct.green.bold('Possible age: ') + possible_age)
    print(tab + pct.green.bold('Possible city: ') + possible_city)
    print(tab + pct.green.bold('Possible sex: ') + possible_sex)
    print()
    print(frame)
    print()
    print()
    print(tab + pct.yellow.bold('Public information:'))
    print(frame)
    print()

    print(tab + pct.green.bold('First name: ') + info['first_name'])
    print(tab + pct.green.bold('Last name: ') + info['last_name'])

    try:
        sex = info['sex']

        if sex == 1:
            sex = 'Female'

        elif sex == 2:
            sex = 'Male'

        print(tab + pct.green.bold('Sex: ') + sex)

    except Exception: pass

    try:
        bdate = info['bdate']
        byear = lib.work_on_bdate(bdate)

        if bdate:
            print(tab + pct.green.bold('Age: ') + str(current_year - int(byear)))

    except Exception: pass

    try:
        city = info['city']['title']
        print(tab + pct.green.bold('City: ') + city)

    except Exception: pass

    try:
        country = info['country']['title']
        print(tab + pct.green.bold('Country: ') + country)

    except Exception: pass

    try:
        univer = info['university_name']
        print(tab + pct.green.bold('University: ') + univer)

    except Exception: pass

    try:
        fac = info['faculty_name']
        print(tab + pct.green.bold('Faculty: ') + fac)

    except Exception: pass

    print()
    print(tab + pct.white.bold('You can see more public information at ' + link))

    print()
    print(frame)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print()
        log.info('Interrupted by user')
        exit(0)
