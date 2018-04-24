class Batter:
	def __init__(self, BA, name, singles_avg, doubles_avg, triples_avg, HR_avg):
		self.BA = BA
		self.name = name
		self.singles_avg = singles_avg
		self.doubles_avg = doubles_avg
		self.triples_avg = triples_avg
		self.HR_avg = HR_avg

class Pitcher:
	def __init__(self, ERA, name):
		self.ERA = ERA
		self.name = name

def get_true_BA(Batter, Pitcher):
	# Get batter BA and multiply value by pitcher statistic
	print "test"

def determine_event(Batter, Pitcher):
	# Determine whether hit or no hit, and then 
	# determine event based on weights
	# returns event code
	print "test"

def build_team():
	# List options of players to choose from
	# set team based on that... 
	print "test"

def get_pitcher()

def simulate():
	bases = []
	home_team_names = []
	away_team_names = []
	home_score = 0
	away_score = 0
	# instantiate pitcher
	# for each inning
		# loop through each player in team
			# instantiate batter
			# determine event
			# if event is single
				# insert [Player] to beginning of list
				# if length of list is > 3, cut count as score
			# if event is double:
				# insert [None, Player] to beginning of list
				# if length of list is > 3, cut count as score
			# if event is triple
				# insert [None, None, Player] to beginning of list
				# if lenght ...
			# if event is HR:
				# insert [None, None, None] to list
				# cut length
			# destroy player object
		# delete pitcher
		# instantiate pitcher
		# same loop for other team


