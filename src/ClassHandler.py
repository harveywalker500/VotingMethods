class Voter:
    """A class to represent a voter

    Attributes
    ----------
    first_name : str
        The first name of the voter
    last_name : str
        The last name of the voter
    age : int
        The age of the voter
    economic_ideology : float
        The economic ideology of the voter
    diplomatic_ideology : float
        The diplomatic ideology of the voter
    civil_ideology : float
        The civil ideology of the voter
    social_ideology : float
        The social ideology of the voter

    Methods
    -------
    __str__()
        Returns a string representation of the voter
    __repr__()
        Returns a string representation of the voter
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
        return f"""{self.first_name} {self.last_name}
        Age: {self.age}
        Economic Ideology: {self.economic_ideology}
        Diplomatic Ideology: {self.diplomatic_ideology}
        Civil Ideology: {self.civil_ideology}
        Social Ideology: {self.social_ideology}"""

    def __repr__(self):
        return self.__str__()
