import random


class Voter:
    """
    A class representing a voter with their personal information and political ideologies.

    Attributes:
    first_name (str): The first name of the voter.
    last_name (str): The last name of the voter.
    age (int): The age of the voter.
    economic_ideology (float): The economic ideology of the voter, ranging from 0 (left) to 1 (right).
    diplomatic_ideology (float): The diplomatic ideology of the voter, ranging from 0 (isolationist) to 1 (internationalist).
    civil_ideology (float): The civil ideology of the voter, ranging from 0 (authoritarian) to 1 (libertarian).
    social_ideology (float): The social ideology of the voter, ranging from 0 (conservative) to 1 (progressive).

    Methods:
    str(): Returns a string representation of the voter's information.
    repr(): Returns a string representation of the voter's information.

    Usage:
    voter = Voter(first_name='John', last_name='Doe', age=25, economic_ideology=5.0,
    diplomatic_ideology=7.5, civil_ideology=-2.0, social_ideology=8.0)
    print(voter)
    # prints 'John Doe\nAge: 25\nEconomic Ideology: 5.0\nDiplomatic Ideology: 7.5\nCivil Ideology: -2.0\nSocial Ideology: 8.0'
    """
    def __init__(self, first_name: str, last_name: str, age: int, economic_ideology: float,
                 diplomatic_ideology: float, civil_ideology: float, social_ideology: float):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.economic_ideology: float = economic_ideology
        self.diplomatic_ideology: float = diplomatic_ideology
        self.civil_ideology: float = civil_ideology
        self.social_ideology: float = social_ideology

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
    - __str__(): returns a string representation of the party's name and ideological positions.
    - __repr__(): returns a string representation of the party's name and ideological positions.
    """

    def __init__(self, name, economic_ideology, diplomatic_ideology, civil_ideology, social_ideology):
        self.name = name
        self.economic_ideology = economic_ideology
        self.diplomatic_ideology = diplomatic_ideology
        self.civil_ideology = civil_ideology
        self.social_ideology = social_ideology

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

    python
    Copy code
    Attributes:
    - voters (list): a list of Voter objects representing the voters in the election.
    - parties (list): a list of Party objects representing the political parties in the election.

    Methods:
    - __str__(): returns a string representation of the election's voters and parties.
    - __repr__(): returns a string representation of the election's voters and parties.
    - generate_voter_list(nof_voters): generates a list of voters with random attributes.
    """
    def __init__(self):
        """
        Initializes an Election object with an empty list of voters and an empty list of parties.
        Generates a list of voters using the generate_voter_list method.
        """
        self.voters = []
        self.parties = []
        self.generate_voter_list()

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

    def generate_voter_list(self, nof_voters=1000):
        """
        Generates a list of voters with random attributes.

        Args:
        - nof_voters (int): the number of voters to generate. Default is 1000.
        """
        # Opens the file and reads the contents into a list
        with open("data/first_names.txt", "r") as f:
            first_names_f = f.readlines()
            first_names_f = [x.strip() for x in first_names_f]

        with open("data/last_names.txt", "r") as f:
            last_names_f = f.readlines()
            last_names_f = [x.strip() for x in last_names_f]

        for i in range(nof_voters):
            self.voters.append(Voter(random.choice(first_names_f), random.choice(last_names_f), random.randint(18, 100),
                                     round(random.random(), 2), round(random.random(), 2), round(random.random(), 2),
                                     round(random.random(), 2)))
