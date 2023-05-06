import random
import matplotlib.pyplot as plt
from tqdm import *
import itertools


class Voter:
    """
    A class representing a voter with their personal information and political ideologies.

    Attributes:
    - first_name (str): The first name of the voter.
    - last_name (str): The last name of the voter.
    - age (int): The age of the voter.
    - economic_ideology (float): The economic ideology of the voter, ranging from 0 to 1.
    - diplomatic_ideology (float): The diplomatic ideology of the voter, ranging from 0 to 1.
    - civil_ideology (float): The civil ideology of the voter, ranging from 0 to 1.
    - social_ideology (float): The social ideology of the voter, ranging from 0 to 1.
    - preferred_party (Party): The political party that is most suitable for the voter based on their ideology spectrum

    Methods:
    - __str__(): Returns a string representation of the voter's information.
    - __repr__(): Returns a string representation of the voter's information.
    - determine_most_suitable_party(parties): Determines the political party that is most suitable for the voter based
        on their ideological positions.
    """

    id_obj = itertools.count()

    def __init__(self, first_name: str, last_name: str, age: int, economic_ideology: float,
                 diplomatic_ideology: float, civil_ideology: float, social_ideology: float, election):
        """
        Initializes a Voter object with their personal information and political ideologies.

        Args:
            first_name (str): The first name of the voter.
            last_name (str): The last name of the voter.
            age (int): The age of the voter.
            economic_ideology (float): The economic ideology of the voter, ranging from 0 to 1.
            diplomatic_ideology (float): The diplomatic ideology of the voter, ranging from 0 to 1.
            civil_ideology (float): The civil ideology of the voter, ranging from 0 to 1.
            social_ideology (float): The social ideology of the voter, ranging from 0 to 1.
            election: The Election object the Voter is part of.
        """
        self.id = str("V" + str(next(Voter.id_obj)))
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.economic_ideology: float = economic_ideology
        self.diplomatic_ideology: float = diplomatic_ideology
        self.civil_ideology: float = civil_ideology
        self.social_ideology: float = social_ideology
        self.preferred_party: Party = self.determine_most_suitable_party(election.parties)

    def __str__(self):
        """
        Returns a string representation of the voter's name and ideological positions.
        """
        return f"""{self.first_name} {self.last_name}
        ID: {self.id}
        Age: {self.age}
        Economic Ideology: {self.economic_ideology}
        Diplomatic Ideology: {self.diplomatic_ideology}
        Civil Ideology: {self.civil_ideology}
        Social Ideology: {self.social_ideology}"""

    def __repr__(self):
        """
        Returns a string representation of the voter's name and ideological positions.
        """
        return self.__str__()

    def determine_most_suitable_party(self, parties):
        """
        Determines the most suitable party for the voter based on their ideological positions.

        Args:
            parties: A list of Party objects representing the available political parties in the election.

        Returns:
            The Party object that is most ideologically compatible with the voter.
        """
        party_scores = []

        for party in parties:
            voter_party_difference = [abs(self.economic_ideology - party.economic_ideology),
                                      abs(self.diplomatic_ideology - party.diplomatic_ideology),
                                      abs(self.civil_ideology - party.civil_ideology),
                                      abs(self.social_ideology - party.social_ideology)]

            voter_difference_total = sum(voter_party_difference)
            party_scores.append(voter_difference_total)

        most_suitable_party = parties[party_scores.index(min(party_scores))]
        return most_suitable_party


class Party:
    """
    A class representing a political party with its name and ideological positions.

    Attributes:
    - name (str): the name of the political party.
    - economic_ideology (str): the economic ideology of the party.
    - diplomatic_ideology (str): the diplomatic ideology of the party.
    - civil_ideology (str): the civil ideology of the party.
    - social_ideology (str): the social ideology of the party.

    Methods:
    - __str__(): Returns a string representation of the party's name and ideological positions.
    - __repr__(): Returns a string representation of the party's name and ideological positions.
    """

    id_obj = itertools.count()

    def __init__(self, name, economic_ideology, diplomatic_ideology, civil_ideology, social_ideology):
        self.id = str("P" + str(next(Party.id_obj)))
        self.name = name
        self.economic_ideology = economic_ideology
        self.diplomatic_ideology = diplomatic_ideology
        self.civil_ideology = civil_ideology
        self.social_ideology = social_ideology
        self.votes = 0

    def __str__(self):
        """
        Returns a string representation of the party's name and ideological positions.
        """
        return f"""{self.name}
        ID: {self.id}
        Economic Ideology: {self.economic_ideology}
        Diplomatic Ideology: {self.diplomatic_ideology}
        Civil Ideology: {self.civil_ideology}
        Social Ideology: {self.social_ideology}"""

    def __repr__(self):
        """
        Returns a string representation of the party's name and ideological positions.
        """
        return self.__str__()


class Election:
    """
    A class representing an election with voters and political parties.

    Attributes:
    - voters (list): a list of Voter objects representing the voters in the election.
    - parties (list): a list of Party objects representing the political parties in the election.

    Methods:
    - __str__(): Returns a string representation of the election's voters and parties.
    - __repr__(): Returns a string representation of the election's voters and parties.
    - generate_election(nof_voters): Generates a list of voters with random attributes.
    - FPTP_vote(): Determines the winner of the election using First Past The Post.
    - generate_pie_charts(): Generates pie charts of the election winners.
    """

    def __init__(self, nof_voters=1000, nof_parties=5, prearrange_list=False):
        """
        Initializes an Election object with an empty list of voters and an empty list of parties.
        Generates a list of voters using the generate_election method.

        Args:
        - nof_voters (int): the number of voters to generate.
        - nof_parties (int): the number of parties to generate.
        - prearrange_list (bool): whether to generate a list of voters and parties or not.
        """
        self.voters = []
        self.parties = []
        if not prearrange_list:
            self.prepare_election(nof_voters, nof_parties)

    def __str__(self):
        """
        Returns a string representation of the election's voters and parties.
        """
        return f"""Voters: {self.voters}
        Parties: {self.parties}"""

    def __repr__(self):
        """
        Returns a string representation of the election's voters and parties.
        """
        return self.__str__()

    def prepare_election(self, nof_voters, nof_parties, first_name_path=None, last_name_path=None,
                         party_name_path=None):
        """
        Generates a list of voters and parties with random attributes.

        Args:
        - nof_voters (int): the number of voters to generate.
        - nof_parties (int): the number of parties to generate.
        - first_name_path (str): the path to the first_names.txt file.
        - last_name_path (str): the path to the last_names.txt file.
        - party_name_path (str): the path to the party_names.txt file.
        """
        # Opens the file and reads the contents into a list
        if not first_name_path:
            first_name_path = input("Enter the path to the first_names.txt file: ")
        if not last_name_path:
            last_name_path = input("Enter the path to the last_names.txt file: ")
        if not party_name_path:
            party_name_path = input("Enter the path to the party_names.txt file: ")

        try:
            with open(first_name_path, "r") as f:
                first_names_f = f.readlines()
                first_names_f = [x.strip() for x in first_names_f]
        except FileNotFoundError:
            raise FileNotFoundError("Error! Could not load first_names.txt")

        try:
            with open(last_name_path, "r") as f:
                last_names_f = f.readlines()
                last_names_f = [x.strip() for x in last_names_f]
        except FileNotFoundError:
            raise FileNotFoundError("Error! Could not load last_names.txt")

        try:
            with open(party_name_path, "r") as f:
                parties_f = f.readlines()
                parties_f = [x.strip() for x in parties_f]
        except FileNotFoundError:
            raise FileNotFoundError("Error! Could not load party_names.txt")

        # Generates a list of parties
        for i in range(nof_parties):
            self.parties.append(Party(parties_f[i], round(random.random(), 2), round(random.random(), 2),
                                      round(random.random(), 2), round(random.random(), 2)))

        for i in range(nof_voters):
            self.voters.append(Voter(random.choice(first_names_f), random.choice(last_names_f), random.randint(18, 100),
                                     round(random.random(), 2), round(random.random(), 2), round(random.random(), 2),
                                     round(random.random(), 2), self))

    def FPTP_vote(self):
        """Determines the winner of the election using First Past The Post. Returns the winner of the party."""
        for party in self.parties:
            for voter in tqdm(self.voters, desc=f"Counting votes for {party.name}", unit="voters"):
                if voter.preferred_party == party:
                    party.votes += 1

        sorted_parties = sorted(self.parties, key=lambda party: party.votes, reverse=True)
        winner = sorted_parties[0]
        print(f"The winner is {winner.name} with {winner.votes} votes")

        self.generate_pie_charts(winner)
        return winner

    def generate_pie_charts(self, winner):
        """Creates a pie chart of the election results."""
        winner_name = winner.name

        party_names = [party.name for party in self.parties]
        party_votes = [party.votes for party in self.parties]

        winner_index = party_names.index(winner_name)

        colours = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

        plt.pie(party_votes, labels=party_names, colors=colours,
                explode=[0 if i != winner_index else 0.1 for i in range(len(party_names))],
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title('Election Results')
        plt.legend(loc='best')
        plt.show()

    def clear_parties(self):
        """Clears the list of parties."""
        self.parties = []

    def clear_voters(self):
        """Clears the list of voters."""
        self.voters = []

    def add_party(self, name: str, economic_ideology: float, diplomatic_ideology: float, civil_ideology: float,
                  social_ideology: float):
        """
        Adds a new party to the election.

        Args:
        - name (str): the name of the party.
        - economic_ideology (float): the economic ideology of the party.
        - diplomatic_ideology (float): the diplomatic ideology of the party.
        - civil_ideology (float): the civil ideology of the party.
        - social_ideology (float): the social ideology of the party.
        """
        if not name:
            name = input("Enter the name of the party: ")
        if not economic_ideology:
            economic_ideology = float(input("Enter the economic ideology of the party: "))
        if not diplomatic_ideology:
            diplomatic_ideology = float(input("Enter the diplomatic ideology of the party: "))
        if not civil_ideology:
            civil_ideology = float(input("Enter the civil ideology of the party: "))
        if not social_ideology:
            social_ideology = float(input("Enter the social ideology of the party: "))

        self.parties.append(Party(name, economic_ideology, diplomatic_ideology, civil_ideology, social_ideology))

    def add_voter(self, first_name: str, last_name: str, age: int, economic_ideology: float,
                  diplomatic_ideology: float, civil_ideology: float, social_ideology: float):
        """Adds a voter to the list of voters.

        Args:
        - first_name (str): the first name of the voter.
        - last_name (str): the last name of the voter.
        - age (int): the age of the voter.
        - economic_ideology (float): the economic ideology of the voter.
        - diplomatic_ideology (float): the diplomatic ideology of the voter.
        - civil_ideology (float): the civil ideology of the voter.
        - social_ideology (float): the social ideology of the voter.
        """
        if not first_name:
            first_name = input("Enter the first name of the voter: ")
        if not last_name:
            last_name = input("Enter the last name of the voter: ")
        if not age:
            age = input("Enter the age of the voter: ")
        if not economic_ideology:
            economic_ideology = input("Enter the economic ideology of the voter: ")
        if not diplomatic_ideology:
            diplomatic_ideology = input("Enter the diplomatic ideology of the voter: ")
        if not civil_ideology:
            civil_ideology = input("Enter the civil ideology of the voter: ")
        if not social_ideology:
            social_ideology = input("Enter the social ideology of the voter: ")

        self.voters.append(Voter(first_name, last_name, age, economic_ideology, diplomatic_ideology,
                                 civil_ideology, social_ideology, self))

    def delete_party(self, party_id):
        """Deletes a party from the list of parties."""
        if not party_id:
            party_id = input("Enter the ID of the party you want to delete: ")

        for party in self.parties:
            if party.id == party_id:
                self.parties.remove(party)
                break

    def delete_voter(self, voter_id):
        """Deletes a voter from the list of voters."""
        if not voter_id:
            voter_id = input("Enter the first name of the voter you want to delete: ")

        for voter in self.voters:
            if voter.name == voter_id:
                self.voters.remove(voter)
                break
