import random as rand
#neckless_gerald = "  o \n \|/ \n / \\"
# o
#\|/
#/ \
def GeraldExtender(neck_size):


    print("  o")
    for i in range(neck_size):
        print("  |")
    print(" \|/")
    print(" / \\")

def GeraldunExtender(neck_size):


    print("  o")
    for i in range(neck_size):
        print("  |")
    print(" \|")
    print(" / \\")

def GeraldArm(arm_size):

    for i in range(arm_size):
        print("|")

print("Hello, Gerald has a bizarre disease called Giraffian Neck Syndrome. His neck can grown on command.")
print("how big should his neck be?")

user_neck_size = int(input())
GeraldExtender(user_neck_size)
#print(user_input)

print("How long should Gerald's arm be?")

user_arm_size = int(input())
GeraldunExtender(user_neck_size)
GeraldArm(user_arm_size)
#print(user_input)

print("Gerald seems to have lost his arm. Oops.")
print("How many friends should Gerald have?")

gerald_no_friends = int(input())

if gerald_no_friends > 0:
    for i in range(gerald_no_friends):
        friend_neck_size = rand.randint(0,10)
        GeraldExtender(friend_neck_size)
else:
    print("Poor Gerlad!")
