#!/usr/bin/env python3
import requests


def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print('Endereço :', address)
    print('Resultado 1 :')
    print('\t\tCEP : ',reply[0]['display_name'].split(',')[7])
    print('\t\tLatitude e Longetude','(',reply[0]['lat'],',', reply[0]['lon'],')')

    print('Resultado 2 :')
    print('\t\tCEP : ', reply[1]['display_name'].split(',')[7])
    print('\t\tLatitude e Longetude','(',reply[1]['lat'],',', reply[1]['lon'],')')


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')
