def print_summary(day): #function definition for printing the produce summary
    print(f"Day {day}") #prints the day number
    the_file = open(f"um-deliveries-day-{day}.txt") #opens the file for the appropriate day
    for line in the_file: #loops through the file line by line
        line = line.rstrip() #removes unnecessary space from the right
        words = line.split('|') #splits the string on instances of |

        melon = words[0] #assigns the first word to the variable melon 
        count = words[1] #assigns the second word to the variable count
        amount = words[2] #assigns the third word to the variable amount

        print(f"Delivered {count} {melon}s for total of ${amount}") #prints a line of the report
    the_file.close() #closes the file

print_summary(1) #function call for day 1
print_summary(2) #function call for day 2
print_summary(3) #function call for day 3