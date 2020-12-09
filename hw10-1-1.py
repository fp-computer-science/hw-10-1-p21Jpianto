# Author: JAp (amdg) 12/9/20

def points():
    f_team = input("Who was the home team?")
    wins = input(" How many wins does " + (f_team) + " have?")
    ties = input("How many ties does " + (f_team) + " have?")

    t_points = (wins * 3) + (ties * 1)

    s_team = input("Who was the away team?")

    wins2 = input(" How many wins does " + (s_team) + " have?")

    ties2 = input("How many ties does " + (s_team) + " have?")

    t_points2 = (wins2 * 3) + (ties2 * 1)

    if t_points > t_points2:
        print(f_team + " had more points in the group stage than " + s_team)
    else:
        print(s_team + " had more points in group stage than " + f_team)


print(points())
