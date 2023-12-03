import pickle
l=[10,20,30,40]
file=open("writedata.txt","wb")
pickle.dump(l,file)

file.close()
text=open("writedata.txt","rb")
t=pickle.load(text)
print(t)