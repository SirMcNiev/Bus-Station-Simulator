from time import sleep
from random import randint
from random import random
from os import chdir

num_of_people_adding = 0
traffic_lights = 5

times_of_simulating = int(input("Enter the number you want the simulation to run:"))

for eachtime in range(times_of_simulating):
    data = []
    should_add = randint(0,2)
    if should_add == 0:
        pass
    else:
        num_of_people_adding = randint(1,7)
        for i in range(num_of_people_adding):
            data.append(0)
        for i in range(traffic_lights):
            chance_of_getting_red = randint(0,2)
            if chance_of_getting_red == 0:
                for j in range(num_of_people_adding):
                    current_value = float(data[j])
                    data.pop(j)
                    data.insert(j,current_value + randint(0,90))
            else:
                pass
        for j in range(num_of_people_adding):
                current_value = float(data[j])
                data.pop(j)
                data.insert(j,round(current_value + 2 * random() * randint(15,90) + 0.7 + (random()  / 3 + 0.6) * randint(200,400),2))
    data.sort()
    print(data)
    chdir("/Users/ASUS/Desktop")
    f = open("__data__.txt","a+",encoding = "utf-8")
    f.write(str(data) + "\n")
    f.close()
    sleep(1.5)
