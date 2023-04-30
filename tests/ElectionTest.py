import unittest
from src.ClassHandler import Election, Voter, Party


class TestElection(unittest.TestCase):

    def setUp(self):
        self.election = Election(nof_voters=1000, nof_parties=5)

    def test_generate_election(self):
        self.assertEqual(len(self.election.voters), 1000)
        self.assertEqual(len(self.election.parties), 5)
        for voter in self.election.voters:
            self.assertTrue(isinstance(voter, Voter))
        for party in self.election.parties:
            self.assertTrue(isinstance(party, Party))

    def test_determine_most_suitable_party(self):
        parties = [
            Party('Party 1', 0.5, 0.5, 0.5, 0.5),
            Party('Party 2', 0.8, 0.2, 0.7, 0.3),
            Party('Party 3', 0.2, 0.8, 0.3, 0.7)
        ]
        voter = Voter('John', 'Doe', 30, 0.6, 0.4, 0.5, 0.3, Election())
        self.assertEqual(voter.determine_most_suitable_party(parties), parties[0])
        voter = Voter('Jane', 'Doe', 25, 0.9, 0.1, 0.8, 0.2, Election())
        self.assertEqual(voter.determine_most_suitable_party(parties), parties[1])
        voter = Voter('Bob', 'Smith', 50, 0.1, 0.9, 0.2, 0.8, Election())
        self.assertEqual(voter.determine_most_suitable_party(parties), parties[2])

    def test_FPTP_vote(self):
        election = Election(nof_voters=5, nof_parties=2)
        election.parties = [
            Party('Party 1', 0.5, 0.5, 0.5, 0.5),
            Party('Party 2', 0.8, 0.2, 0.7, 0.3),
        ]
        election.voters = [
            Voter('John', 'Doe', 30, 0.6, 0.4, 0.5, 0.3, Election()),  # most suitable: party 1
            Voter('Jane', 'Doe', 25, 0.9, 0.1, 0.8, 0.2, Election()),  # most suitable: party 2
            Voter('Bob', 'Smith', 50, 0.1, 0.9, 0.2, 0.8, Election()),  # most suitable: party 2
            Voter('Alice', 'Johnson', 45, 0.4, 0.6, 0.3, 0.9, Election()),  # most suitable: party 1
            Voter('Sarah', 'Lee', 29, 0.2, 0.7, 0.6, 0.4, Election())  # most suitable: party 1
        ]

        for voter in election.voters:
            voter.preferred_party = voter.determine_most_suitable_party(election.parties)
        winner = election.FPTP_vote()


if __name__ == '__main__':
    unittest.main()
