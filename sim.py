# Simulator to model the United States Presidential election

class Simulation:
    def __init__(self):
        self.time = 0
        self.party_of_incumbent_candidate = ""

    def scheduleERV(self, event, propensity):
        self.events.put((self.time + random.exponential(1.0/propensity), event))

    def scheduleNRV(self, event, mean, stddev):
        self.events.put((self.time + random.normal(mean, stddev), event))

    # Events

    def sex_scandal:
        print(";)")

    def terrorist_attack:
        print("")

    def economic_upturn:
        print("")

    def economic_downturn:
        print("")

    def political_debate:
        # probably shouldn't be an ERV???
        print("")

    def enviromental_disaster:
        print("")

    def war_declared:
        # should probably boost incumbent???
        print("")

    def russian_intervention:
        # rare, but ya know, it happens
        print("bit on the nose")

    def bad_press_release:
        print("")

class Politician:
    def __init__(self, name, party, sex_scandal_rate):
        self.name = name
        self.party = party
        self.sex_scandal_rate = sex_scandal_rate

class American_Electorate:
    def __init__(self):
        # need good research for this one, and this can get real complicated real quick
        self.democrats =
        self.republicans =
        self.third_party =
        self.independent =
