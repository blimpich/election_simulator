# Simulator to model the United States Presidential election one year in advance
import random

class Simulation:
    def __init__(self):
        self.days = 0  #365
#         self.events = PriorityQueue()
        
        self.economic_upturn_rate = 0.005  # 2/365
        self.economic_downturn_rate = 0.008
        self.terrorist_attack_rate = 0.004
        self.enviromental_disaster_rate = 0.014
        self.war_starts_rate = 0.000547

        self.american_electorate = American_Electorate()

    def scheduleERV(self, event, propensity):
        self.events.put((self.days + random.exponential(1.0/propensity), event))

    def scheduleNRV(self, event, mean, stddev):
        self.events.put((self.days + random.normal(mean, stddev), event))

    def day_passes:
        next_event = self.events.get()
        self.time = next_event[0]
        next_event[1]()
        
    # Events specific to candidates propensity

    def sex_scandal:
        
    # def russian_intervention:
    #     # rare, but ya know, it happens
    #     print("bit on the nose")

    def bad_press_release:
        print("")

    # Events independent of candidates

    def economic_upturn:
        print("")
        
    def economic_downturn:
        print("")

    def terrorist_attack:
        print("")

    def political_debate:
        # probably shouldn't be an ERV???
        print("")

    def enviromental_disaster:
        print("")

    def war_starts:
        # should probably boost incumbent???
        print("")        

class Candidate:
    def __init__(self, name, party, sex_scandal_rate, bad_press_rate):
        self.name = name
        self.party = party
        self.sex_scandal_rate = sex_scandal_rate
        self.bad_press_rate = bad_press_rate
        
class American_Electorate:
    def __init__(self):
        # % of the electorate based roper center cornell stats
        self.democrats = 37 
        self.republicans = 33
        self.swing = 30
        swing_vote = Swing_Vote()
        
        
# TO DO: specify republican and democratic leanings in initial groups (currently half and half)
class Swing_Vote:
    def __init__(self):
        # percentage representing #1 issues for swing voters, ie 20% of swing voters say terrorism is their #1 issue
        groups = {
            "terrorism": Group(35, 35, 30, 20),
            "economy": Group(35, 35, 30, 30), 
            "foreign_policy": Group(35, 35, 30, 5),
            "environment": Group(35, 35, 30, 10),
            "immigration": Group(35, 35, 30, 9),
            "candidate profile": Group(35, 35, 30, 25), 
            "other": Group(35, 35, 30, 1),
        }
        
        def update(area, amount):
            groups[area] = groups[area] + amount

class Group:
    def __init__(self, percent_leaning_republicans, percent_leaning_democrats, percent_undecided, swing_percentage):
        self.republican = percent_republicans
        self.democrats = percent_democrats
        self.undecided = percent_undecided
        self.swing_percentage = swing_percentage
        
# Do simulation

us2020 = Simulation()
republican = Candidate("Donald", "Republican", .9, .8)
democrat = Candidate("Bernie", "Democrat", .1, .2)
self.political_debate =  # theres like three of them right? make this occur a fixed number of times during simulation

# dt = 1
# sim_time = 365
# snapshot_interval = 10
# next_snapshot = snapshot_interval

# while us2020.time < sim_time:
#   # randomly determine whether an event happens this second
#     us2020.day_passes()
#     if ( us2020.time > next_snapshot):
#       print("Time: ", us2020.time)
#       next_snapshot += snapshot_interval
