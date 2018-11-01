n = 100

for i in range(1,n+1):
    div_by_two = False
    div_by_three = False

    if i%2 == 0:
        div_by_two = True
    if i%3 == 0:
        div_by_three = True
    
    if div_by_two and div_by_three:
        print("pingpong")
    elif div_by_two:
        print("ping")
    elif div_by_three:
        print("pong")
    else:
        print(i)
