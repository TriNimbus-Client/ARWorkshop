#!/usr/bin/env python

import random
from faker import Faker

fake = Faker('en_CA')
for n in range(1000000):
    print(str(n)+","+fake.name()+","+fake.province()+","+fake.company()+","+str(random.randint(18,90)))
    #print(str(n)+","+fake.job())
