
'''
LMP = League Match Played
LMG = League Match Goals
LMA = League Match Assists
LMC = League Match Caps

CRMP = Career Match Played
CRMG = Career Match Goals
CRMA = Career Match Assists
CRMC = Career Match Caps
'''

ALL_PLAYERS = []

class Player:
    def __init__(self, name, club, age=0, squadNumber=0, position="PLY", 
    AVG=0, LMP=0, LMG=0, LMA=0, LMC=0, CRMP=0, CRMG=0, CRMA=0, CRMC=0, 
    contactEnds=0):
    
    # self attributes
     self.name=name
     self.club=club
     self.age = age
     self.AVG=AVG
     self.squadNumber = squadNumber
     self.position = position

    # league attributes
     self.LMP=LMP
     self.LMG=LMG
     self.LMA=LMA
     self.LMC=LMC

    # career attributes
     self.CRMP=CRMP
     self.CRMG=CRMG
     self.CRMA=CRMA
     self.CRMC=CRMC

     self.contactEnds = contactEnds

    # register player
     ALL_PLAYERS.append(self)
    
    def Play_League_Match(self):
        self.CRMP += 1
        self.LMP += 1

