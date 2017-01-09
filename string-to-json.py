import json

'''
    Again, scrapy outputs a jl file, (I could directly output to a json file but ヾ(`ヘ´)ﾉﾞ  )
    got the string, and convert it into a list of json objs
'''
f = open('./static/results.jl', 'r')
lista = []

for line in f.readlines():
    lista.append(json.loads(line))