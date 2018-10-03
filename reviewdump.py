#!/usr/bin/python3
import psycopg2
from random import randint
import os

def review_data_dump():
    '''data dump for reviews'''
    conn = psycopg2.connect('dbname=testpython user=vagrant password={}'.format(os.environ.get('DJANGO_PASSWORD')))
    cur = conn.cursor()
   
    reviews = {
        'Eat': ['Best place ever', 'Spectacular food', 'I love this place', 'Would recommned', '5 star place!', 'DELICIOUS!!!'],
        'Play': ['Super fun!', 'Love this place', 'So exciting!', 'Best time ever']
    }
    ratings = [3, 4, 5]
    user_id = [2, 3, 4, 5, 6]
    try:            
        for num in range(67, 157):
            rating = randint(0, len(ratings)-1)
            user = randint(0, len(user_id)-1)

            if num < 97:
                review = randint(0, len(reviews['Eat'])-1)
                cur.execute(
                    'INSERT INTO souvenirapp_review(text, rating, place_id_id, user_id_id) VALUES(%s, %s, %s, %s)', (reviews.get('Eat')[review], ratings[rating], num, user_id[user]))
                print('Data point added to database => testpython')
                
            else:
                review = randint(0, len(reviews['Play'])-1)
                cur.execute(
                    'INSERT INTO souvenirapp_review(text, rating, place_id_id, user_id_id) VALUES(%s, %s, %s, %s)', (reviews.get('Play')[review], ratings[rating], num, user_id[user]))
                print('Data point added to database => testpython')
    except Exception as e:
        print(e)


    conn.commit()
    conn.close()

if __name__ == '__main__':
    review_data_dump()
