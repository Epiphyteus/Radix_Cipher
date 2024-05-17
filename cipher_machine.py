#title 
def title():
 print(r"""

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗              
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗             
██║     ██║██████╔╝███████║█████╗  ██████╔╝             
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗             
╚██████╗██║██║     ██║  ██║███████╗██║  ██║             
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝             

███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
     """)

#menu options
def menu():
    print(r"""   """)
    print("Welcome to Cipher Machine.") 
    print("You can use this program to work with a variety of simple ciphers and encryptions.")
    print("""Please make a selection by entering one of the following values
    """)
    print("1. Caesar Cipher ")
    print("2. Casear Hacker ")
    print("3. Symbol Converter")
    print("0. Quit")


##code for caesar cipher
def caesar(x):
    print("""Do you want to (e)ncode or (d)ecode a message? 
          """)
    while True:
#loop to allow player to select encryption or decryption 
        i=input(">")
        if i.startswith("e") or i.startswith("E"):
            mode="Encrypt"
            break
        elif i.startswith("d") or i.startswith("D"):
            mode="Decrypt"
            break
        else:
            print("Enter d or e")
    print(f"""
{mode}ing""")
#User key to offset a character in message
    print("""
Enter a secret numerical key.""")
#loop to handle non-integer entry error
    while True:
        try:
            key=int(input("""
>"""))
            break
        except ValueError:
            print("""
That's not a number. Try again.""")
#allow for a key of any integer to be converted automatically to an offset that is allowable
    while key not in range (0, len(x)):
        if key>len(x):
            key=key-len(x)
        elif key<len(x):
            key=len(x)-key
#Get user input message
    print("""
Input your message
          """)
    message=input(">")
#Convert to uppercase to simplify things
    message=message.upper()
#Establish empty string for translated message
    conv=""
    index=0
#loop to tranverse message
    while index<len(message):
#if symbol is a valid symbol in the established list of symbols (see else for syblols not in SYMBOLS)
        if message[index] in x:
#find the position of that symbol within the list of symbols
            num=x.find(message[index])
#offset that position by the value specified by the user (secret key)
            if mode=="Encrypt":
                num+=key
            elif mode=="Decrypt":
                num-=key
#if that offset results in a position greater than the amount of positions in the list of symbols
#subtract the lenght of the list of symbols from the position
#effectively wrapping the position in the list around to the beginning once it reaches the end. 
            if num>= len(x):
                num=num-len(x)
#handle the situation where the position of a symbol + the length of the list of symbols exactly equals the length of the list
#and is therefore
            elif num<0:
                num=num+len(x)
#for each time through the for loop, add the newly converted symbol to existing list, forming the converted message.
            conv = conv + x[num]
#if symbol is not in established list of symbols, append the non converted symbol
        else:
            conv=conv+message[index]
        index+=1
#return the converted message to the main calling routine. 
    return(conv)

#code for brute force decryption 
def caesar_hacker(x,y):
    msg=y
    for key in range (len(x)):
        translated=""
        for symbol in msg:
            if symbol in x:        
                num=x.find(symbol)
                num=num-key
                if num<0:
                    num+=len(x)
                translated=translated+x[num]
            else:
                translated+=symbol
        print(f"""
For secret key {key} 
Message was: 
{translated}
---------------------------""")


#functions to convert strings to lists and back
def string_to_list(string):
    list=[]
    s=len(string)
    i=0
    while i<s:
        list.append(string[i])
        i+=1
    return list

def list_to_string(list):
    text="".join(list)
    return text

#create and format 4 sequential lists of symbol types all with lenght 100
def make_sym_lists():
    import string
    h=[]
    d=[]
    b=[]
    a=[]
#walk a list of 1 to 100, one number at a time. for each number, convert it to binary, hex, decimal and add each of those conversions to the correct list. 
    for x in range(1,101,1): 
        y=hex(x)
        z=bin(x)
        h.append(y[2:].zfill(2))
        d.append(str(x))
        b.append(z[2:])
#using string tools, take each symbol in python's built in list of 100 printable ASCII characters and add it to the correct list. 
    for symbol in string.printable:
        c=symbol 
        a.append(c)
    return (h,b,a,d)

#Binary,Hex,Decimal,ASCII Converter
def symbol_converter():
#call lists from makelists(), assign to local variables
    sym_lists=make_sym_lists()
    hexlist=sym_lists[0]
    binlist=sym_lists[1]
    ASCII_list=sym_lists[2]
    declist=sym_lists[3]
    while True:
        out=[]
        print(fr"""Radix and symbology selection:
        """)
        print("(H)exidecimal")
        print("(D)ecimal")
        print("(B)inary")
        print(fr"""(A)SCII (Plaintext)
        """)
        print(fr"""(Q)uit to Menu
        """)
        print(fr"""Choose desired INPUT radix or symbology from the menu above
        """)
        q=1
    #loop to handle the user setting the conversion mode. Provides option to quit as well. 
        while True:
            msg_in=input(">")
            if msg_in.startswith("h") or msg_in.startswith ("H"):
                msg_in="hexidecimal"
                q==1
                break
            elif msg_in.startswith("D") or msg_in.startswith("d"):
                msg_in="decimal"
                q==1
                break
            elif msg_in.startswith("B") or msg_in.startswith("b"):
                msg_in="binary"
                q==1
                break
            elif msg_in.startswith("A") or msg_in.startswith("a"):        
                msg_in="ascii"
                q==1
                break       
            elif msg_in.startswith("q") or msg_in.startswith("Q"):
                q=0
                break
            else:
                print("Please make a valid selection")
        if q==0:
            break
        print("")
#display in and out selections after making them. 
        print(fr"""INPUT: {msg_in}
        """)
        print("Choose desired OUTPUT radix or symbology from the menu above")
        print("")
        msg_out=input(">")
        print("")

        if msg_out.startswith("H") or msg_out.startswith("h"):
            msg_out="hexidecimal"
        elif msg_out.startswith ("D") or msg_out.startswith("d"):
            msg_out="decimal"
        elif msg_out.startswith ("B") or msg_out.startswith("b"):
            msg_out="binary"
        elif msg_out.startswith ("A") or msg_out.startswith("a"):
            msg_out="ascii"
        print(fr"""OUTPUT: {msg_out}
        """)
        print(fr"""Enter message below. Separate symbol values in hex, binary, and decimal inputs with spaces.
        """)
#Loop to deal with mis entered messages without crashing the program. Later on, if a message's characters are not in the selected input symbols library, the user will be reminded of the input mode and allowed to re-enter the message. 
        while True:
            try:
#no matter the message, it need to become a list to be converted. Plaintext inputs will be split into the smallest divisions possible, Every single character including spaces will be indexed in a list by the same name as the input message. 
#other symbol designations like binary, hex, or decimal will create new list items everytime items are separated by a space. The output for anything being converted to bin, hex, or dec will automatically also be spaced in the same way. 
                msg=input(">")
                if msg_in=="ascii":
                    string_to_list(msg)
                else:
                    msg=msg.split()
#conditionals for input, output, what lists to reference and how to do the conversion. Space added here for bin, hex, and dec outputs. lists converted back into strings.
                for x in msg:
                    if msg_in=="hexidecimal" and msg_out=="hexidecimal":
                        x=hexlist.index(x)
                        x=hexlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="decimal" and msg_out=="decimal":
                        x=declist.index(x)
                        x=declist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="binary" and msg_out=="binary":
                        x=binlist.index(x)
                        x=binlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="ascii" and msg_out=="ascii":
                        x=ASCII_list.index(x)
                        x=ASCII_list[x]
                        out.append(x)
                        o=list_to_string(out)
                    if msg_in=="hexidecimal" and msg_out=="decimal":
                        x=hexlist.index(x)
                        x=declist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="hexidecimal" and msg_out=="binary":
                        x=hexlist.index(x)
                        x=binlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="hexidecimal" and msg_out=="ascii":
                        x=hexlist.index(x)
                        x=ASCII_list[x]
                        out.append(x)
                        o=list_to_string(out)
                    if msg_in=="decimal" and msg_out=="hexidecimal":
                        x=declist.index(x)
                        x=hexlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="decimal" and msg_out=="binary":
                        x=declist.index(x)
                        x=binlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="decimal" and msg_out=="ascii":
                        x=declist.index(x)
                        x=ASCII_list[x]
                        out.append(x)
                        o=list_to_string(out)
                    if msg_in=="binary" and msg_out=="hexidecimal":
                        x=binlist.index(x)
                        x=hexlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="binary" and msg_out=="decimal":
                        x=binlist.index(x)
                        x=declist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="binary" and msg_out=="ascii":
                        x=binlist.index(x)
                        x=ASCII_list[x]
                        out.append(x)
                        o=list_to_string(out)
                    if msg_in=="ascii" and msg_out=="hexidecimal":
                        x=ASCII_list.index(x)
                        x=hexlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="ascii" and msg_out=="decimal":
                        x=ASCII_list.index(x)
                        x=declist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                    if msg_in=="ascii" and msg_out=="binary":
                        x=ASCII_list.index(x)
                        x=binlist[x]
                        out.append(f"{x} ")
                        o=list_to_string(out)
                break
            except ValueError:
                print(fr"""
ERROR: Input shoud be {msg_in}. 
Before re-entering message below, 
please check message text to ensure correct symbology and spacing.
                """)
        print(fr"""
Converting from {msg_in} to {msg_out}...

The converted message is:
      """)
#print the converted message
        print (fr"""----------------------
{o}
-----------------------
         """)
#allow the user to do another conversion or quit to the main cipher machine menu. 
print("Returning to menu...")


#main calling routine
re=1
title()
while re!=0:
    menu()
    x=int(input("""
>"""))
    if x==(1):
        print("""Initializing Caesar's Cipher...
                """)
#Establish a list of symbols for encryption
        print("""Do you want to use the default symbols list or create your own?
                
Enter 0 to use the default list or 1 to create your own.
    """)
        while True:
            try:
                choice=int(input(">"))
                if choice==1:
                    print("""
Enter your own symbols as a string with no commas.""")
                    x=input(">")
                    x=x.upper()
                    break
                elif choice==0:
                    x="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                    break
            except ValueError:
                print("""
That's not a valid selection. Try again.
                    """)
        print(fr"""
The symbols that can be encrypted are:
{x}

Symbols not in this list will be included as unencrypted characters.

Encrypted Message:
---------------------             
{caesar(x)}
---------------------      
Returning to menu.""")
        
    elif x==(2):
        print("Initializing Caesar Hacker...")
        print("This function will decrypt a message for all possible keys in a list of symbols.")
        print("""
Do you want to use the default symbols list or create your own?

Enter 0 to use the default list or 1 to create your own.
            """)
        while True:
            try:
                choice=int(input(">"))
                if choice==1:
                    print("""
Enter your own symbols as a string with no commas.""")
                    s=input(">")
                    s=s.upper()
                    break
                elif choice==0:
                    s="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                    break
            except ValueError:
                print("""
That's not a valid selection. Try again.
                    """)
        print(fr"""
The symbols that can be encrypted are:
{s}""")
        print("""
Symbols not in this list will be included as unencrypted characters.

Enter a message to decrypt""")
        msg=input(">")
        msg=msg.upper()
#run caesar_hacker function, pass symbols list and message to decode. 
        caesar_hacker(s,msg)
        print("""
Returning to menu.""")

    elif x==(3):
        symbol_converter()
    elif x==(0):
        print("Quitting...")
        re=0
    else:
        print("Invalid menu selection, try again")

