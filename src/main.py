from ClassHandler import *

if __name__ == '__main__':
    election = Election(nof_voters=100000, nof_parties=3)
    print(election.FPTP_vote())
