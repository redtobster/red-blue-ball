import random

# UTILITY FUNCTION TO PICK TWO BALLS RANDOMLY
def pick_two_balls_randomly(red_ball, blue_ball):
    # FIRST SELECTION
    first_selection = random.randrange(1, red_ball+blue_ball+1)
    if first_selection <= red_ball:
        first_ball = "RED BALL TAKEN"
        red_ball -= 1
    else:
        first_ball = "BLUE BALL TAKEN"
        blue_ball -= 1

    # SECOND SELECTION
    try:
        second_selection = random.randrange(1, red_ball+blue_ball)
        if second_selection <= red_ball:
            second_ball = "RED BALL TAKEN"
            red_ball -= 1
        else:
            second_ball = "BLUE BALL TAKEN"
            blue_ball -= 1
    except:
        if red_ball == 1:
            second_ball = "RED BALL TAKEN"
            red_ball -= 1
        else:
            second_ball = "BLUE BALL TAKEN"
            blue_ball -= 1


    return {"first_ball": first_ball, "second_ball": second_ball, "red_ball": red_ball, "blue_ball": blue_ball}

# UTILITY FUNCTION TO ASK USER FOR INPUT
def input_ball_value():
    try:
        user_input = int(input())
        return user_input
    except:
        print("THE DATA TYPE OF INPUT SHOULD BE INTEGER, TRY AGAIN")
        return input_ball_value()

# STARTING THE ROUND HERE!
print("WELCOME TO CHOOSING RED AND BLUE BALLS FROM A BAG!")
print("YOU ARE FIRST FREE TO CHOOSE A BAG OF BLUE AND RED BALLS")

print("THE FOLLOWING ARE THE RULES:")
print("\tAT EACH ROUND, I TAKE TWO BALLS RANDOMLY FROM THE BAG")
print("\tIF THEY ARE THE SAME COLOR, I DISCARD THEM AND ADD A BLUE BALL")
print("\tIF THEY ARE DIFFERENT COLOR, I DISCARD THE BLUE BALL AND ADD THE RED BALL BACK")
print("WHAT DO YOU KNOW ABOUT THE FINAL BALL?")

print("-"*20)
print("ONCE YOU HAVE UNDERSTOOD THE RULES, PLEASE SELECT NUMBER OF RED BALL")
red_ball = input_ball_value()
print("OK, WE START WITH", red_ball, "RED BALLS")
print("NOW PLEASE SELECT NUMBER OF BLUE BALLS")
blue_ball = input_ball_value()
print("OK, WE START WITH", blue_ball, "BLUE BALLS")
print("STARTING ROUND ...")
round_number = 1
while red_ball + blue_ball > 1:
    # pick two balls randomly
    print("\n"*2)
    print("THIS IS ROUND NUMBER", round_number)
    print("PYTHON PICKS UP TWO RANDOM BALLS NOW")
    selection_result = pick_two_balls_randomly(red_ball, blue_ball)
    first_result = selection_result["first_ball"]
    second_result = selection_result["second_ball"]
    print("FIRST RESULT:", first_result)
    print("SECOND RESULT:", second_result)

    if first_result == second_result:
        print("SAME COLOR SELECTED, SO I AM GOING TO PUT A BLUE BALL AND DISCARD BOTH BALLS")
        if "BLUE" in first_result:
            blue_ball -= 2
        else:
            red_ball -= 2
        blue_ball += 1
        print("REMAINING BLUE BALL:", blue_ball)
        print("REMAINING RED BALL:", red_ball)
    else:
        print("DIFFERENT COLOR SELECTED, SO I AM GOING TO DISCARD BLUE BALL")
        blue_ball -= 1
        print("REMAINING BLUE BALL:", blue_ball)
        print("REMAINING RED BALL:", red_ball)

    print("END OF ROUND", round_number)
    print("-"*20)
    round_number += 1

print("\n"*2)
print("END GAME AT ROUND", round_number)
if blue_ball == 1:
    print("THE FINAL BALL IS BLUE")
else:
    print("THE FINAL BALL IS RED")
