import json
x=10
x_jon=json.dumps(x)
#print(x_jon)

y=5.5
y_json=json.dumps(y)

m=True
m_json=json.dumps(m)

sonlar=(12,45,23,67)
sonlar_json=json.dumps(sonlar)
sonlar2=json.loads(sonlar_json)

bemor ={
        "ismi":"Sabohat Qayumova",
        "yosh":24,
        "oila":True,
        "farzandlar":('Azizbek',"E'zoza"),
        "allergiya":None,
        "dorilar":[
            {"nomi":"Analgin","miqdori":0.5},
            {"nomi":"Panodol","miqdori":1.3}
            ]
        }
bemor_json=json.dumps(bemor,indent=4)
# print(bemor_json)
#JSONni faylga saqlash
with open('data/bemor.json','w') as f:
    json.dump(bemor,f)

filename="data/bemor.json"
with open(filename) as f:
    bemor=json.load(f)
# print(type(bemor))
# print(bemor.keys())
# print(bemor["dorilar"][0])
# print(bemor)
