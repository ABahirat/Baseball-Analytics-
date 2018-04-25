import csv

from numpy.random import choice

class Batter:
	def __init__(self, name, singles_avg, doubles_avg, triples_avg, HR_avg, BA):
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
	# Get true batting average
	true_BA = get_true_BA(Batter, Pitcher)
	hit = choice([0, 1], p=[1-BA, BA])

	if hit:
		return choice(["single", "double", "triple", "Home Run"], p=[Batter.singles_avg, Batter.doubles_avg, Batter.triples_avg, Batter.HR_avg])
	else:
		return 0

def build_team(team_name):
	# List options of players to choose from
	# set team based on that... 
	print "test"

def get_pitcher(name):
	f = open("pitching.csv")
	csv_f = open csv.reader(f)

	for row in csv_f:
		if row[0] == name:
			# probably will change
			return Pitcher(name, row[0])


def get_batter(name):
	# instantiates batter from CSV file
	f = open("batting.csv")
	csv_f = csv.reader(f)

	for row in csv_f:
		if row[0] == name:
			return Batter(name, row[2], row[3], row[4], row[5], row[6])

def simulate():
	bases = []
	home_team_names = []
	away_team_names = []
	home_score = 0
	away_score = 0
	#instantiate pitcher
	# for each inning
		# loop through each player in team
			# account for 3 strikes
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


