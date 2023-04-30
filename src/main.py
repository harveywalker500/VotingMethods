from ClassHandler import *

if __name__ == '__main__':
    election = Election(nof_voters=50000, nof_parties=10)
    print(election.FPTP_vote())
