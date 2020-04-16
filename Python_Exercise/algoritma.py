class managment:

    zam=1.8
    counter=0

    def __init__(self,name,lastname,maas,city):
        self.name=name
        self.lastname=lastname
        self.maas=maas
        self.city=city

        managment.counter+=1


    def join(self):
        return self.name + " " + self.lastname

    def zamOrani(self):
        self.maas=self.maas+(self.maas*self.zam)




person1=managment("ugurcan","kok",230,"Aydin")
print (person1.name)
print(person1.join())
#person1.zamOrani()
#print(person1.maas)

print(managment.counter)

person2=managment("kerem","kok",300,"Aydin")

print(managment.counter)
print(person2.maas)


liste=[person1,person2]

max_maas=-1
index=-1

for each in liste:
    if(each.maas>max_maas):
        max_maas=each.maas
        index=each



print(max_maas)
print(index.join())