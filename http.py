import requests as rq
address=input("enter the address without http: \n")

add="http://" + address

r=rq.get(add)
headers=strlist = ' '.join(r.headers)

print(str(r.status_code)+  "\n"+headers+"\n"+"this is response!\n"+r.text)