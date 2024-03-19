# ! ---------> looping


# looping can be implimented using
# for loop
# while loop


# ----> for loop
# ?for loop is used for iteartion , if we know the number of time the the loop have to run
# ?
# it is used  To Iterate the Iterables eg(string,list,tuple,etc...)

# todo ----> sytax for loop


# for syntax in c
# for(i-0:i<10:i++){
#     print("hello");
#}

# | for sytax in python
# for userdefined -variable in range(start,end,step):defealut step value is 1
# statement
# statement
# statement
# ? Eg:1
# To print the value from 1 to 10 using for loop

for i in range(0,10):#(n, n-1)
    print(i)
    print("hello")
 # ? Eg:3
 # to decrement the value

 # for val in range(10, 0, -1):
     # print(val)
 # for val in range(10, 0, -2):
     # print(val)

 # for val in range(10, 0, 1):
 #   print(val) # no output


# ? Eg:4
# ! print the output of 7th multification table form 21 to 43
for val in range(1, 10+1,):
   # print('7','x',val,'=',val*7) --> method:1
    
    # ----> method:2
    # ans="7 x{} = {}"
    # print(ans.format(val,val*7))

    # --> method:3
    print(f"7 x{val}={val*7}")

    # ?Eg:5
    # break --> used to teerminate the loop

    for val in range(1, 10):
        if val ==6:
            break
        print(val)
            

    # ?Eg:6
    # break --> used to teerminate the loop

    for val in range(1, 10):
        if val ==6:
            break
        print(val)
    
   # ?Eg:7
   # for val in range(1, 10):
   # if val ==6:
   #    print(val)
   #     break

   # ! continue
   # Eg:1
    for val in range(1, 30):
      #  if val ==6 or val ==8 or val ==21:
      #      continue
     #   print(val)


        # ! pratices problems
        # ? print the even number between 20 to 40
    # for val in range(20, 41):

         # if val %2==0:
         # print(val)


          #!--------> while loop
         # ? while is used when we do not know the number  of times the loop have to run
         # ?  to iterate the non itrable element while is loop is used


         # todo  syntax



         # initialisation
         # while condition:
         #   statement
         #   incre or decre

         # eg:1
         # to iterate  number from 1 to 10


         # 1 = 0
         # while 1<11:
         #   print(i)
         # i=i+1 #I+=1

         # for loop pratisee
         # write a program to disply sum of odd numbers and even
         # numbers that fall between
         # 12 and 37 (including both number)
         

        
         # eg:1
         # to iterate  number from 1 to 10


         # 1 = 0
         # while 1<11:
         #   print(i)
         # i=i+1 #I+=1 




         
                
        



        
        

 
    
    

