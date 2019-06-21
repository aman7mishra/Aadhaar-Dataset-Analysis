import operator 
import csv
import matplotlib.pyplot as plt
raw=[]
data = open('UIDAI.csv', 'r')
next(data)
for line in data:
    raw.append(line.strip().split(','))
mvk={}
for row in raw:
    k=row[2]
    v=row[8]
    if v!='':
        v=int(float(v))
    else:
        v=0
    if k in mvk:
        mvk[k]+=v
    else:
        mvk[k]=v
sorted_d = dict( sorted(mvk.items(), key=lambda x: x[1], reverse=True))
states=[]
Aadhaars=[]
for key ,value in sorted_d.items():
    states.append(key)
    Aadhaars.append(value)
for i in range(len(states)):
    print(states[i],Aadhaars[i])

plt.plot(states,Aadhaars,marker="o")
plt.xticks(rotation=90)
plt.xlabel("States")
plt.ylabel("Number of Aadhaar Generated")
plt.savefig('States_vs_Aadhaar.png')
plt.show()