import requests
import csv

def write_csv(filename, data):
    with open(filename, 'a', encoding ='utf-8', newline='') as file:
        csv.DictWriter(file, fieldnames=list(data)).writerow(data)

def main():
    offset = 0

    while True:
        url = 'https://наш.дом.рф/сервисы/api/erz/main/filter'
        params = (
            ('offset', offset),
            ('limit', 100),
            ('sortField', 'devShortNm'),
            ('sortType', 'asc')
        )


        response = requests.get(url, params=params)
        reestr = response.json()

        developers = reestr['data']['developers']

        for developer in developers:
            devId = developer['devId']

            try:
                devShortNm = developer['devShortNm']
            except:
                devShortNm = 'Наименование организации не указано'

            try:
                devNumPhone = developer['devPhoneNum']
            except:
                devNumPhone = 'Номер телефона не указан'

            try:
                devEmail = developer['devEmail']
            except:
                devEmail = 'E-mail не указан'

            try:
                devSite = developer['devSite']
            except:
                devSite = 'Адрес сайта не указан'

            try:
                devLegalAddr = developer['devLegalAddr']
            except:
                devLegalAddr = 'Фактический адрес не указан'


            data = {
                'devId': devId,
                'devShortNm': devShortNm,
                'devNumPhone': devNumPhone,
                'devEmail': devEmail,
                'devSite': devSite,
                'devLegalAddr': devLegalAddr
            }

            write_csv('dom-rf.csv', data)

        if not developers:
            break

        offset += 100


if __name__ == '__main__':
    main()