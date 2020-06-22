'''
Developer Name - Mannideep Kalangi
Date - 22/06/2020
Description - Game......
'''

def poscheck(a):
    if a>=1 and a<=9:
        if a>=1 and a<=3:
            int(row1[a-1])==a
            return True
        elif a>=4 and a<=6:
            b=a%3
            int(row2[b-1])==a
            return True
        elif a>=7 and a<=9:
            b=a%6
            int(row3[b-1])==a
            return True
        else:
            return False
    else:
        return False

def anscheck(row1,row2,row3):
    if row1[0]==ply1_sgn and row1[1]==ply1_sgn and row1[2]==ply1_sgn:
        return True
    elif row2[0]==ply1_sgn and row2[1]==ply1_sgn and row2[2]==ply1_sgn:
        return True
    elif row3[0]==ply1_sgn and row3[1]==ply1_sgn and row3[2]==ply1_sgn:
        return True
    elif row1[0]==ply1_sgn and row2[1]==ply1_sgn and row3[2]==ply1_sgn:
        return True
    elif row3[0]==ply1_sgn and row2[1]==ply1_sgn and row1[2]==ply1_sgn:
        return True
    elif row1[0]==ply1_sgn and row2[0]==ply1_sgn and row3[0]==ply1_sgn:
        return True
    elif row1[1]==ply1_sgn and row2[1]==ply1_sgn and row3[1]==ply1_sgn:
        return True
    elif row1[2]==ply1_sgn and row2[2]==ply1_sgn and row3[2]==ply1_sgn:
        return True
    elif row1[0]==ply2_sgn and row1[1]==ply2_sgn and row1[2]==ply2_sgn:
        return True
    elif row2[0]==ply2_sgn and row2[1]==ply2_sgn and row2[2]==ply2_sgn:
        return True
    elif row3[0]==ply2_sgn and row3[1]==ply2_sgn and row3[2]==ply2_sgn:
        return True
    elif row1[0]==ply2_sgn and row2[1]==ply2_sgn and row3[2]==ply2_sgn:
        return True
    elif row3[0]==ply2_sgn and row2[1]==ply2_sgn and row1[2]==ply2_sgn:
        return True
    elif row1[0]==ply2_sgn and row2[0]==ply2_sgn and row3[0]==ply2_sgn:
        return True
    elif row1[1]==ply2_sgn and row2[1]==ply2_sgn and row3[1]==ply2_sgn:
        return True
    elif row1[2]==ply2_sgn and row2[2]==ply2_sgn and row3[2]==ply2_sgn:
        return True
    else:
        return False

print("Welcome to the Game")
ply_nm1=input("Enter Player1 Name\n")
ply_nm2=input("Enter Player2 Name\n")
row1=['1','2','3']
row2=['4','5','6']
row3=['7','8','9']
f=True
count=1
ply1_sgn=input("Select one sign from ('O' or 'X') - Player1 \n")
ply2_sgn=''
if ply1_sgn=='O':
    ply2_sgn='X'
elif ply1_sgn=='X':
    ply2_sgn='O'
else:
    print('''Our System auto assigned signs for
    Player1 - 'O'
    Player2 - 'X'
    ''')
    ply1_sgn='O'
    ply2_sgn='X'
while(f):
    print(row1)
    print(row2)
    print(row3)
    for i in range(2):
        if i==0:
            print("--------------------Player - 1---------------------\n")
            print("Enter value from 0 - 9 \n")
            a=int(input("Enter your position \n"))
            if poscheck(a):
                if a>=1 and a<=3:
                    row1[a-1]=ply1_sgn
                elif a>=4 and a<=6:
                    b=a%3
                    row2[b-1]=ply1_sgn
                elif a>=7 and a<=9:
                    b=a%6
                    row3[b-1]=ply1_sgn
            else:
                print("It is out of Range")

            if anscheck(row1,row2,row3):
                print(row1)
                print(row2)
                print(row3)
                print("\n")
                print("You Win")
                f=False
                break
            count=count+1
        elif i==1 and count!=10:
            count=count+1
            print("--------------------Player - 2---------------------\n")
            print("Enter value from 0 - 9 \n")
            a=int(input("Enter your position \n"))
            if poscheck(a):
                if a>=1 and a<=3:
                    row1[a-1]=ply2_sgn
                elif a>=4 and a<=6:
                    b=a%3
                    row2[b-1]=ply2_sgn
                elif a>=7 and a<=9:
                    b=a%6
                    row3[b-1]=ply2_sgn
            else:
                print("It is out of Range")
                
            if anscheck(row1,row2,row3):
                print(row1)
                print(row2)
                print(row3)
                print("\n")
                print("You Win")
                f=False
                break
        elif count==10:
            print(row1)
            print(row2)
            print(row3)
            print("\n")
            print("No one wins")
            f=False
            break

        
        
