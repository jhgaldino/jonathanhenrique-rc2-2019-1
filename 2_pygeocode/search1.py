from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False)

    print('\tEndereço buscado : ', address)
    print('Resultado 1 :')
    print('\t\tCEP : ',location[0][0].split(",")[7])
    print('\t\t(Latitude,Longetude)','(',location[0].latitude,',',location[0].longitude,')')

    print('Resultado 2 :')
    print('\t\tCEP : ', location[1][0].split(",")[7])
    print('\t\tLatitude e Longetude','(',location[1].latitude, ',', location[1].longitude,')')

