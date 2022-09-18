import random
import time

print("Welcome to Adventure game.")

skills = ["mosquito", "peanut", "butter", "bengi", "bubble"]
enemy_skills = ["mosquito", "peanut", "butter", "bengi", "bubble"]
list = ["mosquito", "peanut", "butter", "bengi", "bubble"]


def valid(x):
    a = False

    if len(x) != 0:
        a = True

    else:
        a = False

    return a


def cooldown(x):
    cooldown_skill = 0

    if x == "mosquito":
        cooldown_skill = 5

    elif x == "peanut":
        cooldown_skill = 10

    elif x == "butter":
        cooldown_skill = 2

    elif x == "bengi":
        cooldown_skill = 12

    elif x == "bubble":
        cooldown_skill = 15

    return cooldown_skill


def skill_damage(x):
    dmg = 0
    if x == "mosquito":
        dmg = 10

    elif x == "peanut":
        dmg = random.randint(10, 25)

    elif x == "butter":
        dmg = 5

    elif x == "bengi":
        dmg = 15

    elif x == "bubble":
        dmg = 30

    return dmg


def used(x, y):
    print(
        "A skill is going to be retrieved")  # make every skill has a timer and when that timer hits 0 the skill is back
    x.append(random.choice(list))
    y.append(random.choice(list))

    return x, y


def attack():
    coins = 0
    enemy_health = 100
    health = 100
    print("Your health: ", health)
    print("Enemy's health: ", enemy_health)

    while health > 0 and enemy_health > 0:
        print("Your skills: ", skills)

        if valid(skills) and valid(enemy_skills):
            skill_choice = input("Which skill do you want to choose.")
            enemy_skill = random.choice(enemy_skills)

            while skill_choice not in skills:
                skill_choice = input("Which skill do you want to choose.")

            if skill_choice == enemy_skill:
                print("You both used the same ability")

            else:
                enemy_health -= skill_damage(skill_choice)
                health -= skill_damage(enemy_skill)

                print("Your health: ", health)
                print("Enemy's health: ", enemy_health)

            skills.remove(skill_choice)
            enemy_skills.remove(enemy_skill)

        else:
            used(skills, enemy_skills)
            print(skills)

    else:
        if enemy_health <= 0:
            print("You killed the enemy successfully.")
            coins += 100
            print("You have", coins, "coins")

        elif health <= 0:
            print("You died.")
            exit()


def play():  # main program
    choice_1 = int(input("There's 3 options which one do you want to go: "))

    if choice_1 == 1:
        print("You chosen the right path.")

    else:
        print("There's an enemy in front of you."
              "You need to kill him if you want to continue forward.")

        choice_2 = int(input("1/ Fight the enemy. 2/ Go around : "))

        if choice_2 == 2:
            print("The enemy is far now."
                  "You may continue your journey.")

        else:
            print("The enemy is challenging you")
            choice_3 = int(
                input("The enemy is attacking you do you want to 1.block it or 2.dodge it or 3.attack him : "))

            if choice_3 == 1:
                print("You blocked it successfully")

            elif choice_3 == 2:
                print("You dodge the attack")

            else:
                attack()


def main():
    play()
    repeat = input("Do you want to play again? Y/N").upper()

    if repeat == "Y":
        play()


main()

#  make the skills have a timer
#  make it bigger
