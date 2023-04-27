from ClassHandler import *
import random


def generate_voter_name_list():
    # Opens the file and reads the contents into a list
    with open("data/first_names.txt", "r") as f:
        first_names_f = f.readlines()
        first_names_f = [x.strip() for x in first_names_f]

    with open("data/last_names.txt", "r") as f:
        last_names_f = f.readlines()
        last_names_f = [x.strip() for x in last_names_f]

    return first_names_f, last_names_f


def generate_voters(first_names_f, last_names_f):
    voters_f = []
    for i in range(1000):
        voters_f.append(Voter(random.choice(first_names_f), random.choice(last_names_f), random.randint(18, 100),
                              round(random.random(), 2), round(random.random(), 2), round(random.random(), 2),
                              round(random.random(), 2)))
    return voters_f


if __name__ == '__main__':
    first_names, last_names = generate_voter_name_list()
    voters = generate_voters(first_names, last_names)
    for voter in voters:
        print(voter)
