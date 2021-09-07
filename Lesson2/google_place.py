import csv
import googlemaps


def main():
    gmaps = googlemaps.Client(key='Your Key')
    query = '甜點'
    location = (25.0300378,121.5262015)
    radius = 2500
    place_type = 'food'
    gmap_places = gmaps.places(query=query, location=location, radius=radius, type=place_type)

    with open('Lesson2/shop.csv', 'w', newline='') as csvfile: 
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['店家', '評價'])
        for result in gmap_places['results']:
            writer.writerow([result['name'], result['rating']])

if __name__ == '__main__':
    main()