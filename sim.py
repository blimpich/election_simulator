# Simulator to model the United States Presidential election one year in advance
import random
import numpy.random as random
from queue import PriorityQueue
# from termcolor import colord

''' Class that specifies how to run the simulation '''
class Simulation:

        # Initialize the timeframe, nominees, and events with their frequencies
        def __init__(self):
                self.days = 0  #365
                self.events = PriorityQueue()

                # breakup of the voters into Democrats, Republicans, and Swing
                self.american_electorate = American_Electorate()
                # list of swing vote groups
                self.theGroups = list(self.american_electorate.swing_vote.groups.keys())
                # list of theGroups with candidate profile removed
                self.theGroupsNotCP = [x for x in self.theGroups if x != 'candidate_profile']

                # name, party, sex_scandal_rate
                self.republicanNominee = Candidate("TheDonald", "Republican", 0.02) # 7/365
                self.democratNominee = Candidate("TDS", "Democrat", .01) # 5/365

                # initialize the event rates/latencies
                self.economic_upturn_rate = 0.005  # 2/365
                self.economic_downturn_rate = 0.008 # 3/365
                self.terrorist_attack_rate = 0.004 # 2/365
                self.enviromental_disaster_latency = 73 # every 2.5 months
                self.enviromental_disaster_stdv = 21 # +- 21 days
                self.war_starts_latency = 1095 # every 3 years
                self.war_starts_stdv = 1095 # +- 3 years

                # schedule the first occurence of each event
                self.scheduleERV(self.economic_upturn, self.economic_upturn_rate)
                self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)
                self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)
                self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)
                self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)
                self.scheduleERV(self.sex_scandal_democrat, self.democratNominee.sex_scandal_rate)
                self.scheduleERV(self.sex_scandal_republican, self.republicanNominee.sex_scandal_rate)

                # schedule political debates
                self.events.put((322, self.political_debate))
                self.events.put((335, self.political_debate))
                self.events.put((345, self.political_debate))


        # Schedule an exponential random variable
        def scheduleERV(self, event, propensity):
                self.events.put((self.days + random.exponential(1.0/propensity), event))

        # Schedule a normal random variable
        def scheduleNRV(self, event, mean, stddev):
                self.events.put((self.days + random.normal(mean, stddev), event))

        # Get the next event in the PriorityQueue
        def time_passes(self):
                if(self.events.empty()):
                        print("Empty")
                else:
                        next_event = self.events.get()
                        self.days = next_event[0]
                        next_event[1]()


        ### Events ###
        '''
        Format of event functions:
                schedule the next event
                choose a random swing-voter group that has a specified minimum swing percentage
                update the swing voters' political opinions
        '''

        # Events specific to candidates propensity #

        def sex_scandal_democrat(self):
                print("Democratic sex scandal")

                self.scheduleERV(self.sex_scandal_democrat, self.democratNominee.sex_scandal_rate)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostRepublican(2, "candidate_profile", random_group, 0)

        def sex_scandal_republican(self):
                print("Republican sex scandal")
                self.scheduleERV(self.sex_scandal_republican, self.republicanNominee.sex_scandal_rate)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostDemocrat(1, "candidate_profile", random_group, 0)


        # Events independent of candidates #

        def economic_upturn(self):
                print("economic upturn")
                self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)

                random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostRepublican(5, "economy", random_group, -1)

        def economic_downturn(self):
                print("economic downturn")
                self.scheduleERV(self.economic_upturn, self.economic_upturn_rate)
                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostDemocrat(5, "economy", random_group, 1)

        def terrorist_attack(self):
                print("terrorist attack")
                self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostRepublican(2, "foreign_policy", random_group, 1)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostRepublican(5, "terrorism", random_group, 2)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostRepublican(3, "immigration", random_group, 1)

        # def mass_shooting(self):

        # assume more oil-spill-typle disasters
        def enviromental_disaster(self):
                print("environmental disaster")
                self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 3):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostDemocrat(2, "environment", random_group, 3)

        def war_starts(self):
                print("WAARRRRRR!!!!!")
                self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)

                random_group = random.choice(self.theGroupsNotCP)
                while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 8):
                        random_group = random.choice(self.theGroupsNotCP)
                self.american_electorate.swing_vote.updateVotersBoostDemocrat(1, "foreign_policy", random_group, 8)


        # Political debate #

        def political_debate(self):
                print("political debate")
                # randomly select who wins the debate
                random_winner = random.choice(["Republican", "Democrat"])
                print("the winner is: ", random_winner)

                random_group = random.choice(self.theGroupsNotCP)
                # if the Republican nominee wins, update the swing votes in their favor
                if(random_winner == "Republican"):
                        while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 4):
                                random_group = random.choice(self.theGroupsNotCP)
                        self.american_electorate.swing_vote.updateVotersBoostRepublican(4, "candidate_profile", random_group, 0)
                # otherwise the Democrat nominee wins, so update the swing votes in their favor
                else:
                        while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 4):
                                random_group = random.choice(self.theGroupsNotCP)
                        self.american_electorate.swing_vote.updateVotersBoostDemocrat(4, "candidate_profile", random_group, 0)


        ### Run the election ###
        def run_election(self):
                swing_percent_voting_republican = 0
                swing_percent_voting_democrat = 0
                swing_percent_other_voting = 0

                for group, swingGroupObj in self.american_electorate.swing_vote.groups.items():
                        swing_percent_voting_republican += (swingGroupObj.republican_leaning * swingGroupObj.swing_percentage) / 100
                        swing_percent_voting_democrat += (swingGroupObj.democrat_leaning * swingGroupObj.swing_percentage) / 100
                        swing_percent_other_voting += (swingGroupObj.undecided * swingGroupObj.swing_percentage) / 100

                swing_percent = self.american_electorate.swing/100.0

                swing_percent_voting_republican *= swing_percent
                swing_percent_voting_democrat *= swing_percent
                swing_percent_other_voting *= swing_percent

                self.american_electorate.democrats += swing_percent_voting_democrat
                self.american_electorate.republicans += swing_percent_voting_republican

                print("Democrats: ", str(round(self.american_electorate.democrats, 2)) + "%")
                print("Republican: ", str(round(self.american_electorate.republicans, 2)) + "%")
                print("Third Party/Other: ", str(round(swing_percent_other_voting, 2)) + "%")

                if(self.american_electorate.democrats > self.american_electorate.republicans):
                        print(self.democratNominee.name, "Won")
                else:
                        print(self.republicanNominee.name, "Won")


''' Create a candidate profile '''
class Candidate:
        def __init__(self, name, party, sex_scandal_rate):
                self.name = name
                self.party = party
                self.sex_scandal_rate = sex_scandal_rate
                # self.bad_press_rate = bad_press_rate


''' Create the breakdown of American voters '''
class American_Electorate:
        def __init__(self):
                # % of the electorate based Roper Center Cornell stats
                self.democrats = 35
                self.republicans = 35
                self.swing = 30
                self.swing_vote = Swing_Vote()


''' Create a class for swing voters, where their political decision is based on the importance of a certain political topic,
    and functions that will update their opinions based on an event. '''
class Swing_Vote:
        # Initialize the political opinions for each group for the start of the year
        def __init__(self):
                self.groups = {
                                        # SwingGroup(%rep, %dem, %undec, %of swing vote as #1 care)
                        "terrorism": SwingGroup(45, 25, 30, 20),
                        "economy": SwingGroup(35, 35, 30, 30),
                        "foreign_policy": SwingGroup(35, 35, 30, 5),
                        "environment": SwingGroup(15, 70, 15, 10),
                        "immigration": SwingGroup(55, 25, 20, 9),
                        "candidate_profile": SwingGroup(35, 35, 30, 25),
                        "other": SwingGroup(35, 35, 30, 1),
                }

        def printUpdate(self):
                for key, value in self.groups.items():
                        print('{:>18s} {}'.format(key.upper() + ':', value.printGroup()))
                print("\n")

        # Update swing voters' opinions in favor of the Republicans
        def updateVotersBoostRepublican(self, partyAmount, groupIncr, groupDecr, groupAmount):
                # check that the update will not create a percentage greater than 100,
                #    and if so, update the amount increase to make it up to but not greater than 100
                if(self.groups[groupIncr].republican_leaning+partyAmount > 100):
                        difference = 100-self.groups[groupIncr].republican_leaning
                        partyAmount = difference

                # check that the update will not create a percentage less than 0,
                #    and if so, update the amount increase to make it as low as to but not less than 0
                if(self.groups[groupIncr].democrat_leaning-partyAmount < 0):
                        difference = self.groups[groupIncr].democrat_leaning
                        partyAmount = difference

                # update the swing voters to vote more frequently for Republicans and less frequently for Democrats
                self.groups[groupIncr].republican_leaning += partyAmount
                self.groups[groupIncr].democrat_leaning -= partyAmount
                # update the importance of the given group (political topic) by the given amount
                self.groups[groupIncr].swing_percentage += groupAmount
                self.groups[groupDecr].swing_percentage -= groupAmount

                # print out the update
                self.printUpdate()

        # Update swing voters' opinions in favor of the Democrats
        def updateVotersBoostDemocrat(self, partyAmount, groupIncr, groupDecr, groupAmount):
                # check that the update will not create a percentage greater than 100,
                #    and if so, update the amount increase to make it up to but not greater than 100
                if(self.groups[groupIncr].democrat_leaning+partyAmount > 100):
                        difference = 100-self.groups[groupIncr].democrat_leaning
                        partyAmount = difference

                # check that the update will not create a percentage less than 0,
                #    and if so, update the amount increase to make it as low as to but not less than 0
                if(self.groups[groupIncr].republican_leaning-partyAmount < 0):
                        difference = self.groups[groupIncr].republican_leaning
                        partyAmount = difference

                # update the swing voters to vote more frequently for Democrats and less frequently for Republicans
                self.groups[groupIncr].democrat_leaning += partyAmount
                self.groups[groupIncr].republican_leaning -= partyAmount
                # update the importance of the given group (political topic) by the given amount
                self.groups[groupIncr].swing_percentage += groupAmount
                self.groups[groupDecr].swing_percentage -= groupAmount

                # print out the update
                self.printUpdate()

''' Create a class specifying how the swing voters are voting. '''
class SwingGroup:
        def __init__(self, percent_leaning_republicans, percent_leaning_democrats, percent_undecided, importance_percentage):
                self.republican_leaning = percent_leaning_republicans
                self.democrat_leaning = percent_leaning_democrats
                self.undecided = percent_undecided
                self.swing_percentage = importance_percentage

        def printGroup(self):
                init = 'Leaning Rep {:3d}% Leaning Dem {}%, Undecided {}%, Overall % of Swing Vote {}%'
                return init.format(self.republican_leaning, self.democrat_leaning, self.undecided, self.swing_percentage)




### Do simulation ###

us2020 = Simulation()

# initialize time variables
dt = 1
sim_time = 365
snapshot_interval = 30
next_snapshot = snapshot_interval

# walk through the simulation, printing out the time about every month
while us2020.days < sim_time:
        us2020.time_passes()
        if (us2020.days > next_snapshot):
                print("Day: ", int(round(us2020.days, 0)))
                next_snapshot += snapshot_interval

# have the election
us2020.run_election()
