import Inputs
user=Inputs.get_users()
keep_Playing=True
potCheck(user.name,user.chipCount,sb)
def potCheck(name,chipCount,sb):
    if chipCount==0 or chipCount<sb:
        print("\n",name,"is out of the game")
    else:
        keep_Playing=True


rounds=1
numUsers=5
while keep_Playing==True:
    if rounds==numUsers+1:
        sb=sb*2

    
