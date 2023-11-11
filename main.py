import random
response="y"
while response == "y":
    no=random.randint(1,3)
    if no==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no==2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
    if no==3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
    
    
    response=input("Press y to roll dice and n to exit:")


