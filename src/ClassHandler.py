import random
import matplotlib.pyplot as plt


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

    Methods:
    - __str__(): Returns a string representation of the voter's information.
    - __repr__(): Returns a string representation of the voter's information.
    - determine_most_suitable_party(parties): Determines the political party that is most suitable for the voter based
        on their ideological positions.
    """

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

    def __init__(self, name, economic_ideology, diplomatic_ideology, civil_ideology, social_ideology):
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
    """

    def __init__(self, nof_voters=1000, nof_parties=5, prearrange_list=False):
        """
        Initializes an Election object with an empty list of voters and an empty list of parties.
        Generates a list of voters using the generate_election method.

        Args:
        - nof_voters (int): the number of voters to generate.
        - nof_parties (int): the number of parties to generate.
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

    def prepare_election(self, nof_voters, nof_parties):
        """
        Generates a list of voters and parties with random attributes.

        Args:
        - nof_voters (int): the number of voters to generate.
        - nof_parties (int): the number of parties to generate.
        """
        # Opens the file and reads the contents into a list
        path = "/Users/harveywalker/VotingMethods/data/first_names.txt"
        try:
            with open(path, "r") as f:
                first_names_f = f.readlines()
                first_names_f = [x.strip() for x in first_names_f]
        except FileNotFoundError:
            raise FileNotFoundError("Error! Could not load first_names.txt")

        path = "/Users/harveywalker/VotingMethods/data/last_names.txt"
        try:
            with open(path, "r") as f:
                last_names_f = f.readlines()
                last_names_f = [x.strip() for x in last_names_f]
        except FileNotFoundError:
            raise FileNotFoundError("Error! Could not load last_names.txt")

        path = "/Users/harveywalker/VotingMethods/data/party_names.txt"
        try:
            with open(path, "r") as f:
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
        for party in self.parties:
            for voter in self.voters:
                if voter.preferred_party == party:
                    party.votes += 1

        sorted_parties = sorted(self.parties, key=lambda party: party.votes, reverse=True)
        winner = sorted_parties[0]
        print(f"The winner is {winner.name} with {winner.votes} votes")

        self.generate_pie_charts(winner)
        return winner

    def generate_pie_charts(self, winner):
        # Assume that we have a variable named "winner" that stores the winning party
        winner_name = winner.name
        winner_votes = winner.votes

        # Get the list of all party names and their votes
        party_names = [party.name for party in self.parties]
        party_votes = [party.votes for party in self.parties]

        # Find the index of the winning party in the list of all parties
        winner_index = party_names.index(winner_name)

        # Make a list of colors for the pie chart
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

        # Make the pie chart
        plt.pie(party_votes, labels=party_names, colors=colors,
                explode=[0 if i != winner_index else 0.1 for i in range(len(party_names))],
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.title('Election Results')
        plt.legend(loc='best')
        plt.show()
