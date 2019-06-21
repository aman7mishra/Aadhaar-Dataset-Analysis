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
    k=row[1]
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
EnrollAgency=[]
Aadhaars=[]
for key ,value in sorted_d.items():
    EnrollAgency.append(key)
    Aadhaars.append(value)
print(len(EnrollAgency))
for i in range(0,20):                    #printing first 20
    print(EnrollAgency[i], Aadhaars[i])
fig_size[0] = 55
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
plt.plot(EnrollAgency,Aadhaars,"r")
plt.xticks(rotation=90)
plt.xlabel("Enrollment Agency")
plt.ylabel("Number of Aadhaar Generated")
plt.savefig('EnrollAgency_vs_Aadhaar.png')
plt.show()