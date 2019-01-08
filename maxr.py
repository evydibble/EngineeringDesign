def make_beaver():
	print("")
	print("""
	          .="   "=._.---.
        ."         c ' Y'`p
       /   ,       `.  w_/
   jgs |   '-.   /     / 
 _,..._|      )_-\ \_=.\
`-....-'`------)))`=-'"`'"
	""")
	

   
number_of_beavers = input("How many dragons? ")

if number_of_beavers > 0:
	for x in range(0, number_of_beavers):
		make_beaver()
	print("")
else:
	print("There must be a valid number")
