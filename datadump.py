#!/usr/bin/python3
import requests
import os
import psycopg2
import sys

def dump_data(city_search, section, category):
    '''data dump from foursquare api'''
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    
    url = 'https://api.foursquare.com/v2/venues/explore?near=' + city_search + '&section=' +  section +'&client_id=' + client_id + '&client_secret=' + client_secret + '&v=20180924'
    r = requests.get(url)
    if r.status_code == 200:
        conn = psycopg2.connect('dbname=testpython user=vagrant password={}'.format(os.environ.get('DJANGO_PASSWORD')))
        cur = conn.cursor()
        data = r.json()
        for item in data.get('response').get('groups')[0].get('items'):
            city = 1
            category = category
            name = item.get('venue').get('name')
            description = item.get('venue').get('categories')[0].get('name')
            lat = float(item.get('venue').get('location').get('lat'))
            lng = float(item.get('venue').get('location').get('lng'))
            zipcode = item.get('venue').get('location').get('postalCode')
            address = item.get('venue').get('location').get('address')
            item_id = item.get('venue').get('id')
            phone = '' 
            photoUrl = {'id': ''}
            #request 2 to get photoURL
            url2 = 'https://api.foursquare.com/v2/venues/' + item_id + '/photos?client_id=' + client_id + '&client_secret=' + client_secret + '&v=20180924'
            r2 = requests.get(url2)
            if r2.status_code == 200:
                data2 = r2.json()
                for photo in data2.get('response').get('photos').get('items'):
                    photoUrl['id'] = photo.get('prefix') + '400x300' + photo.get('suffix')
                    print(photoUrl.get('id'))
            else:
                print('Unable to retrieve photo url => Statu_code {}'.format(r2.status_code))            
            
            '''Category, City, Name, Description, Lat, Long, Zip, Address, Phone, Photourl'''
            try:
                cur.execute(
                'INSERT INTO souvenirapp_place(category, name, description, city_id, address, latitude, longitude, phone, photourl, zipcode) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (category, name, description, city, address, lat, lng, phone, photoUrl.get('id'), zipcode))
                print('Data point added to database => testpython')
            except Exception as e:
                print(e)
            #printing
            '''
            print('Category: {}'.format(category))
            print('Name: {}'.format(name))
            print('Description: {}'.format(description))
            print('Lat: {}'.format(lat))
            print('Long: {}'.format(lng))
            print('Zipcode: {}'.format(zipcode))
            print('Address: {}'.format(address))
            print('Phone: {}'.format('empty'))
            print('PhotoURL: {}'.format(photoUrl))
            print('-----------------')
            print()
            '''
    else:
        print("Unable to retrieve data -> Status Code: {}".format(r.status_code))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) is not 4:
        print('Usage: <executable file> <city> <section: ["food", "shops", "arts", "outdoors" "sights"]> <category: ["Eat", "Play", "Stay"]>')
    else:
        dump_data(sys.argv[1], sys.argv[2], sys.argv[3])
