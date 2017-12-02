# Simulator to model the United States Presidential election one year in advance
import random
import numpy.random as random
from queue import PriorityQueue

class Simulation:
	def __init__(self):
		self.days = 0  #365
		self.events = PriorityQueue()
		
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
		# self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)
		# self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)
		# self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)
		# self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)

		self.american_electorate = American_Electorate()
		# self.swing_voters = american_electorate.swing_vote


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

	# def scheduleYear(self):

		
	# Events specific to candidates propensity

	# def sex_scandal:
		# edit Swing_Vote
		# 
		
	# def russian_intervention:
	#     # rare, but ya know, it happens
	#     print("bit on the nose")

	def bad_press_release(self):
		self.scheduleERV(self.bad_press_release, self.bad_press_rate)
		print("bad press release")


	# Events independent of candidates

	def economic_upturn(self):
		self.scheduleERV(self.economic_downturn, self.economic_downturn_rate)
		print("economic upturn")
		# print(list(self.american_electorate.swing_vote.groups.keys()))
		# update
		# updateVotersBoostRepublican(5, economy, random, 1)
		self.american_electorate.swing_vote.updateVotersBoostRepublican(5, "economy", \
			random.choice(list(self.american_electorate.swing_vote.groups.keys())), 1)
		
	def economic_downturn(self):
		self.scheduleERV(self.economic_upturn, self.economic_upturn_rate)
		print("economic downturn")

	def terrorist_attack(self):
		self.scheduleERV(self.terrorist_attack, self.terrorist_attack_rate)
		print("terrorist attack")

	# def political_debate(self):
	# 	# probably shouldn't be an ERV???
	# 	print("")

	# assume more oil-spill-typle disasters
	def enviromental_disaster(self):
		self.scheduleNRV(self.enviromental_disaster, self.enviromental_disaster_latency, self.enviromental_disaster_stdv)
		print("environmental disaster")

	def war_starts(self):
		# should probably boost incumbent???
		self.scheduleNRV(self.war_starts, self.war_starts_latency, self.war_starts_stdv)
		print("WAARRRRRR!!!!!")        

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
		self.swing_vote = Swing_Vote()
		
		
# TO DO: specify republican and democratic leanings in initial groups (currently half and half)
class Swing_Vote:
	def __init__(self):
		# percentage representing #1 issues for swing voters, ie 20% of swing voters say terrorism is their #1 issue
		self.groups = {
					# Group(%rep, %dem, %undec, %of swing vote as #1 care)
			"terrorism": SwingGroup(35, 35, 30, 20),
			"economy": SwingGroup(35, 35, 30, 30), 
			"foreign_policy": SwingGroup(35, 35, 30, 5),
			"environment": SwingGroup(35, 35, 30, 10),
			"immigration": SwingGroup(35, 35, 30, 9),
			"candidate profile": SwingGroup(35, 35, 30, 25), 
			"other": SwingGroup(35, 35, 30, 1),
		}
	
		# updateVotersBoostRepublican(5, economy, random, 1)
	def updateVotersBoostRepublican(self, partyAmount, groupIncr, groupDecr, groupAmount):
		self.groups[groupIncr].republican = self.groups[groupIncr].republican + partyAmount
		self.groups[groupDecr].democrat = self.groups[groupDecr].democrat - partyAmount
		self.groups[groupIncr].republican = self.groups[groupIncr].swing_percentage + groupAmount
		self.groups[groupDecr].democrat = self.groups[groupDecr].swing_percentage - groupAmount

	def updateVotersBoostDemocrat(self, partyAmount, groupIncr, groupDecr, groupAmount):
		self.groups[groupIncr].democrat = self.groups[groupIncr].democrat + partyAmount
		self.groups[groupDecr].republican = self.groups[groupDecr].republican - partyAmount
		self.groups[groupIncr].democrat = self.groups[groupIncr].swing_percentage + groupAmount
		self.groups[groupDecr].republican = self.groups[groupDecr].swing_percentage - groupAmount

class SwingGroup:
	def __init__(self, percent_leaning_republicans, percent_leaning_democrats, percent_undecided, importance_percentage):
		self.republican = percent_leaning_republicans
		self.democrat = percent_leaning_democrats
		self.undecided = percent_undecided
		self.swing_percentage = importance_percentage

# Do simulation

us2020 = Simulation()
republicanNominee = Candidate("Donald", "Republican", .9, .8)
democratNominee = Candidate("Bernie", "Democrat", .1, .2)
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
