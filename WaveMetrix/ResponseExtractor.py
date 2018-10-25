import json

if __name__ == '__main__':
    with open('API_response.json') as json_file:
        result = json.load(json_file)

        for movie in result:
                print (movie['total_raw_views'])
                for data in movie['data']:
                    print ('\t {}'.format(data['raw_views']))