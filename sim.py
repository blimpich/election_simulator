# Simulator to model the United States Presidential election one year in advance
import random
import numpy.random as random
from queue import PriorityQueue

class Simulation:
	def __init__(self):
		self.days = 0  #365
		self.events = PriorityQueue()

		self.american_electorate = American_Electorate()

		# name, party, sex_scandal_rate
		self.republicanNominee = Candidate("TheDonald", "Republican", 0.05)
		self.democratNominee = Candidate("TDS", "Democrat", .03)
		
		self.economic_upturn_rate = 0.005  # 2/365
		self.economic_downturn_rate = 0.008
		self.terrorist_attack_rate = 0.004
		self.enviromental_disaster_latency = 73 # 5/365
		self.enviromental_disaster_stdv = 21
		self.war_starts_latency = 1095
		self.war_starts_stdv = 1095

		# schedule start
		# self.scheduleERV(self.bad_press_release, self.bad_press_rate)
		self.scheduleERV(self.economic_upturn, self.economic_upturn_rate)
		self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)
		self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)
		self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)
		self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)
		self.scheduleERV(self.sex_scandal_democrat, self.democratNominee.sex_scandal_rate)
		self.scheduleERV(self.sex_scandal_republican, self.republicanNominee.sex_scandal_rate)


	def scheduleERV(self, event, propensity):
		self.events.put((self.days + random.exponential(1.0/propensity), event))

	def scheduleNRV(self, event, mean, stddev):
		self.events.put((self.days + random.normal(mean, stddev), event))

	def day_passes(self):
		if(self.events.empty()):
			print("Empty")
		else:
			next_event = self.events.get()
			# print(next_event)

			self.days = next_event[0]
			next_event[1]()

		
	# Events specific to candidates propensity

	def sex_scandal_democrat(self):
		self.scheduleERV(self.sex_scandal_democrat, self.democratNominee.sex_scandal_rate)
		print("Democratic sex scandal")
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))

		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostRepublican(3, "candidate_profile", random_group, 2)

	def sex_scandal_republican(self):
		self.scheduleERV(self.sex_scandal_republican, self.republicanNominee.sex_scandal_rate)
		print("Republican sex scandal")

		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostDemocrat(4, "candidate_profile", random_group, 2)
		
	# def russian_intervention:
	#     # rare, but ya know, it happens
	#     print("bit on the nose")

	# def bad_press_release(self):
	# 	self.scheduleERV(self.bad_press_release, self.bad_press_rate)
	# 	print("bad press release")


	# Events independent of candidates

	def economic_upturn(self):
		self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)
		print("economic upturn")
		# print(list(self.american_electorate.swing_vote.groups.keys()))
		# update
		# updateVotersBoostRepublican(5, economy, random, 1)
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		# while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
		# 	random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostRepublican(5, "economy", random_group, -1)
		
	def economic_downturn(self):
		self.scheduleERV(self.economic_upturn, self.economic_upturn_rate)
		print("economic downturn")
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostDemocrat(7, "economy", random_group, 1)

	def terrorist_attack(self):
		self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)
		print("terrorist attack")
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostRepublican(2, "foreign_policy", random_group, 1)

		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 2):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostRepublican(5, "terrorism", random_group, 2)

		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 1):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostRepublican(3, "immigration", random_group, 1)

	# def political_debate(self):
	# 	# probably shouldn't be an ERV???
	# 	print("")

	# def mass_shooting(self):

	# assume more oil-spill-typle disasters
	def enviromental_disaster(self):
		self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)
		print("environmental disaster")
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 4):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostDemocrat(4, "environment", random_group, 4)

	def war_starts(self):
		# should probably boost incumbent???
		self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)
		print("WAARRRRRR!!!!!")
		random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		while(self.american_electorate.swing_vote.groups[random_group].swing_percentage < 8):
			random_group = random.choice(list(self.american_electorate.swing_vote.groups.keys()))
		self.american_electorate.swing_vote.updateVotersBoostDemocrat(1, "foreign_policy", random_group, 8)


	def run_election(self):
		swing_percent_voting_republican = 0
		for key, value in self.american_electorate.swing_vote.groups.items():
			swing_percent_voting_republican += (value.republican*value.swing_percentage)/100
		swing_percent_voting_republican = swing_percent_voting_republican * (self.american_electorate.swing/100)

		swing_percent_voting_democrat = 0
		for key, value in self.american_electorate.swing_vote.groups.items():
			swing_percent_voting_democrat += (value.democrat*value.swing_percentage)/100
		swing_percent_voting_democrat = swing_percent_voting_democrat * (self.american_electorate.swing/100)

		self.american_electorate.democrats += swing_percent_voting_democrat
		self.american_electorate.republicans += swing_percent_voting_republican

		print("Democrats: ", self.american_electorate.democrats)
		print("Republican: ", self.american_electorate.republicans)
		if(self.american_electorate.democrats > self.american_electorate.republicans):
			print("WE WONNNN!!!!! (the popular vote)")
		else:
			print("WOMP WOMP")


class Candidate:
	def __init__(self, name, party, sex_scandal_rate):
		self.name = name
		self.party = party
		self.sex_scandal_rate = sex_scandal_rate
		# self.bad_press_rate = bad_press_rate
		
class American_Electorate:
	def __init__(self):
		# % of the electorate based roper center cornell stats
		self.democrats = 35
		self.republicans = 35
		self.swing = 30
		self.swing_vote = Swing_Vote()
		
		
# TO DO: specify republican and democratic leanings in initial groups (currently half and half)
class Swing_Vote:
	def __init__(self):
		# percentage representing #1 issues for swing voters, ie 20% of swing voters say terrorism is their #1 issue
		self.groups = {
					# Group(%rep, %dem, %undec, %of swing vote as #1 care)
			"terrorism": SwingGroup(45, 25, 30, 20),
			"economy": SwingGroup(35, 35, 30, 30),
			"foreign_policy": SwingGroup(35, 35, 30, 5),
			"environment": SwingGroup(15, 70, 15, 10),
			"immigration": SwingGroup(55, 25, 20, 9),
			"candidate_profile": SwingGroup(35, 35, 30, 25),
			"other": SwingGroup(35, 35, 30, 1),
		}
	
		# updateVotersBoostRepublican(5, economy, random, 1)
	def updateVotersBoostRepublican(self, partyAmount, groupIncr, groupDecr, groupAmount):
		if(self.groups[groupIncr].republican+partyAmount > 100):
			difference = 100-self.groups[groupIncr].republican
			partyAmount = difference

		if(self.groups[groupIncr].democrat-partyAmount < 0):
			difference = self.groups[groupIncr].democrat
			partyAmount = difference

		self.groups[groupIncr].republican += partyAmount
		self.groups[groupIncr].democrat -= partyAmount
		self.groups[groupIncr].swing_percentage += groupAmount
		self.groups[groupDecr].swing_percentage -= groupAmount
		for key, value in self.groups.items():
			print(key, value.printGroup())
		print("\n")

	def updateVotersBoostDemocrat(self, partyAmount, groupIncr, groupDecr, groupAmount):
		if(self.groups[groupIncr].democrat+partyAmount > 100):
			difference = 100-self.groups[groupIncr].democrat
			partyAmount = difference

		if(self.groups[groupIncr].republican-partyAmount < 0):
			difference = self.groups[groupIncr].republican
			partyAmount = difference

		self.groups[groupIncr].democrat += partyAmount
		self.groups[groupIncr].republican -= partyAmount
		self.groups[groupIncr].swing_percentage += groupAmount
		self.groups[groupDecr].swing_percentage -= groupAmount
		for key, value in self.groups.items():
			print(key, value.printGroup())
		print("\n")

class SwingGroup:
	def __init__(self, percent_leaning_republicans, percent_leaning_democrats, percent_undecided, importance_percentage):
		self.republican = percent_leaning_republicans
		self.democrat = percent_leaning_democrats
		self.undecided = percent_undecided
		self.swing_percentage = importance_percentage

	def printGroup(self):
		# print("Repub.: "self.republican, "Dem.: ", self.democrat, "Undec.: ", self.undecided, "Swing %: ", self.swing_percentage)
		return [self.republican, self.democrat, self.undecided, self.swing_percentage]




# Do simulation

us2020 = Simulation()
# self.political_debate =  # theres like three of them right? make this occur a fixed number of times during simulation

dt = 1
sim_time = 365
snapshot_interval = 10
next_snapshot = snapshot_interval

while us2020.days < sim_time:
  # randomly determine whether an event happens this second
	us2020.day_passes()
	if ( us2020.days > next_snapshot):
	  print("Time: ", us2020.days)
	  next_snapshot += snapshot_interval
us2020.run_election()
