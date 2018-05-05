lst = ["A","B","C"]

item = {"name:":"Adrian","status":"hungry","favorite food":"McFlurries","bag":["laptop","usb","food"]}
reddit = {"reddit" : {"key" : [1,2,3,4]}}

'''
print(reddit["reddit"]["key"][1])

for keys in item:
    print(keys)
'''

adrian = {
    "name":"Adrian Mercado",
    "age":22,
    "hobbies":["powerlifting","raving","eating ice cream"],
    "wake_up":{"Monday":"9:00 AM","Tuesday":"1:00 PM", "Wednesday":"11:00 AM"}
}

print(adrian["name"])
print(str(len(adrian["hobbies"])) + " hobbies")
for hobby in adrian["hobbies"]:
    print(hobby)
for k,v in adrian["wake_up"].items():
    print(k,v)