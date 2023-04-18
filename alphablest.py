if __name__ == '__main__': 

    # Declare the variables
    x=chr;
    h=input("Enter the alphabet:") 
    # Display the alphabets 
    print("The Alphabets from A to Z are: ")

    for x in range(ord('A'), ord('Z') + 1):

        if(chr(x) == h):
            print(chr(x), end=" ");
            break
        else:
            print(chr(x), end=" ");
   
