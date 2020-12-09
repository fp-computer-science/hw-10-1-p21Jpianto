# Author: JAP (amdg) 12/9/20

# hw 2-2


def basketball():
    a = 1
    b = 2
    c = 3

    number_free_throws = input("Please tell us how many free throws")
    number_inside_the_box = input("Please tell us how many 2 pointers")
    number_outside_the_box = input("Please tell us how many 3 pointers")

    f_pts = number_free_throws*a
    i_pts = number_inside_the_box*b
    o_pts = number_outside_the_box*c

    total_score = f_pts+i_pts+o_pts

    print(total_score)
    print("This player scored " + str(total_score) + " points in the game")


print(basketball())
