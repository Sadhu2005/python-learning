import datetime
x=datetime.datetime.now()
B=x.strftime("%B")

m=x.strftime("%Y")
print("Month:",B)
print(x)
print(m)
print(datetime.datetime(2020,1,22))