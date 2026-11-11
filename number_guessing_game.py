import random

def reset():    
    while True:
        n = input("Do you wanna reset the highscore?\npress y for yes and n for No: ")
        n = n.strip().casefold()
        if n not in ["y","n"]:
            print("Enter a valid input: ")
            continue
        else:
            if n =='y':
                with open("highscore.txt","w") as f:
                    pass
        return
            

c_ch = random.randint(1,100)

count = 0
while True:

    try:
        u_ch = int(input("Guess a number: "))
        
    except ValueError:
        print("Enter a valid input")
        continue  #I added it later for the program to skip this iteration and continue to the next iteration
    
    if u_ch<=0:
        print("Please enter a positive number between 1-100")
        continue
            
    else:
        count+=1
        if c_ch == u_ch:
            print(f"Bravo! you guessed it right in {count} trials")
            with open('highscore.txt','a+') as f:
                f.seek(0)
                data = f.read()
            if data =='':
                with open("highscore.txt","w") as f:
                    
                    f.write(str(count))
            else:
                data = int(data)
                if count<data:
                    with open("highscore.txt","w") as f:
                        f.write(str(count))
                        
            reset()          
            break
        
        elif c_ch > u_ch: 
            print("Try a higher number")
            
        else:
            print("Try a lower number")
            
       
