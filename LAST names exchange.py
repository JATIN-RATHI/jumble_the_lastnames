def split_name(names, n):
    #creating list to store first name and last name
    f_name = []
    l_name = []
    #iteration to traverse every item in list
    for words in names:
        #splitting every item word by word in list
        splitted = words.split(" ")
        #storing splitted item ...1st word in f_name and 2nd word in l_name
        f_name.append(splitted[0])
        l_name.append(splitted[1])
    #calling interchange function and giving f_name ,l_name and number of items in names list i.e, n
    final = interchange(f_name, l_name, n)
    return final

def interchange(f_name, l_name, n):
    import random
    k = 1
    #iteration to jumbled or interchange the last names with each another using random function
    for j in range(n):
        #storing first name + space + random last name from the l_name list  in 'jumbled_name'
        jumbled_name = f_name[j] + " " + l_name[random.randint(0, n-1)]
        print(f"{k} : {jumbled_name}")
        k += 1
    return None

if __name__ == '__main__':
    print("\nWelcome to the program\tcreated by \x1b[6;30;42m'Jatin Rathi'\x1b[0m")
    n = int(input("\nEnter the number of names you want to insert : "))
    #creating names list entered by the user to jumbled them
    names = []
    #iterating to take 'n' input from user
    for i in range(1, n+1):
        #storing names one by one in the name
        name = input(f"Enter {i} name with last name : ").capitalize()
        #stored name in name added to the names list one by one
        names.append(name)
    input("Press Enter/any key to display the Exchanged last names")
    #calling the split_name function to return the jumbled_name function output.
    result = split_name(names, n)
