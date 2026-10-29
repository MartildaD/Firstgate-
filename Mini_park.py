print("\n--- Parking Status ---")
my_list = [0] * 20
print(f"Slots: {my_list}") 

mini_park = range(1, 21)    
print(f"Available: {list(mini_park)}")
print("----------------------\n")



def park():
    print("""
Welcome to Mini Parking Slot 

 
1. Enter parking space
2. choose a slot
3. Check Available slot
4. Exit
""")
    choice = int(input('Select an option: '))


    match choice:
        case 1: 
            print("1. Enter parking space")
        case 2: 
            print("2. choose a slot: ")
        case 3:
             print(f"Available: {list(mini_park)}")
             print("Enter slot number")
        case 4: 
            print("4. Exit")
            print("Thank u for testing!!, GoodBye!😛️")




park() 
    
       

