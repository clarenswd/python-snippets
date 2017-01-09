import json
import datetime

'''
After using scrapy, I got a JL file, strings, I needed to create a json file so I used the following function to put the 'json' strings into a file.
'''
def process_string(*params):
    f = open('./static/results.jl', 'r')
    lista = []
    #convert to dict
    for line in f.readlines():
        lista.append(json.loads(line))

    #debug
    for l in lista:
        print(type(l['page_url']))

    jsonfilename = datetime.date.today()
    with open('./static/'+str(jsonfilename)+'-result.json', 'w') as fp:
        json.dump(lista, fp)