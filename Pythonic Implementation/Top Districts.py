import operator 
import csv
import matplotlib.pyplot as plt
raw=[]
data = open('UIDAI.csv', 'r')
next(data)
for line in data:
    raw.append(line.strip().split(','))
mvkmale={}
mvkfemale={}
mvk={}
for row in raw:
    k=row[3]
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
top10={k: sorted_d[k] for k in list(sorted_d)[:10]}
#print(top10)
for key ,value in sorted_d.items():
    states.append(key)
    Aadhaars.append(value)
for row in raw:
    k=row[3]
    v=row[8]
    g=row[6]
    
    if g=="M":
        if v!='':
            v=int(float(v))
        else:
            v=0
        if k in mvkmale:
            mvkmale[k]+=v
        else:
            mvkmale[k]=v
    elif g=="F":
        if v!='':
            v=int(float(v))
        else:
            v=0
        if k in mvkfemale:
            mvkfemale[k]+=v
        else:
            mvkfemale[k]=v

sorted_male = dict( sorted(mvkmale.items(), key=lambda x: x[1], reverse=True))
sorted_female = dict( sorted(mvkfemale.items(), key=lambda x: x[1], reverse=True))
Dist=[]
male=[]
female=[]
for item in top10:
    Dist.append(item)
    male.append(sorted_male[item])
    female.append(sorted_female[item])
    
for i in range(0,10):
    print(Dist[i],male[i],female[i])
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size   
plt.plot(Dist,male,"b",label="male")
plt.plot(Dist,female,"r",label="female")
plt.xticks(rotation=90)
plt.xlabel("Districts")
plt.ylabel("Number of Aadhaar Generated")
plt.legend()
plt.show()