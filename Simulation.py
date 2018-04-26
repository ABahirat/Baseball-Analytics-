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
	def __init__(self, DASP, name):
		# Difference form average strikeout probability
		self.DASP = DASP
		self.name = name

def get_true_BA(Batter, Pitcher):

	return Batter.BA + Pitcher.DASP

def determine_event(Batter, Pitcher):
	# Get true batting average
	true_BA = get_true_BA(Batter, Pitcher)
	hit = choice([0, 1], p=[1-BA, BA])

	if hit:
		return choice(["single", "double", "triple", "HR"], p=[Batter.singles_avg, Batter.doubles_avg, Batter.triples_avg, Batter.HR_avg])
	else:
		return 0

def get_pitcher(name):
	f = open("pitching.csv")
	csv_f = open csv.reader(f)
	for row in csv_f:
		if row[0] == name:
			return Pitcher(name, row[1])


def get_batter(name):
	# instantiates batter from CSV file
	f = open("batting.csv")
	csv_f = csv.reader(f)
	for row in csv_f:
		if row[0] == name:
			return Batter(name, row[2], row[3], row[4], row[5], row[6])

def simulate(home_batters, away_batters, away_pitcher, home_pitcher):
	bases = []
	home_score = 0
	away_score = 0
	away_pitcher = get_pitcher(away_pitcher)
	for i in range(0,9):
		batterCount = 0
		outs = 0
		while(outs < 3):
			# account for 3 strikes
			batting_batter = get_batter(home_batters[batterCount])
			strikes = 0
			while(strikes < 3):
				event = determine_event(away_pitcher, batting_batter)
				if event is "single":
					# insert [Player] to beginning of list
					bases.insert(0, batter_batting.name)
					break
				if event is "double":
					bases.insert(0, [None, batter_batting.name])
					break
				if event is "triple":
					bases.insert(0, [None, None, batter_batting.name])
					break
				if event is "HR":
					bases.insert(0, [None, None, None, batter_batting.name])
					break
				else:
					strikes +=1
			if len(bases) > 3:
					difference = len(bases) - 3
					bases = bases[:-difference]
					off_bases = bases[3:]
					for value in off_bases:
						if value is not None:
							home_score+=1
			batterCount += 1
			if batterCount > len(home_batters)-1:
				batterCount = 0
			if strikes == 3:
				outs += 1
		outs = 0
		while(outs < 3):
			# account for 3 strikes
			batting_batter = get_batter(away_batters[batterCount])
			strikes = 0
			while(strikes < 3):
				event = determine_event(home_pitcher, batting_batter)
				if event is "single":
					# insert [Player] to beginning of list
					bases.insert(0, batter_batting.name)
					break
				if event is "double":
					bases.insert(0, [None, batter_batting.name])
					break
				if event is "triple":
					bases.insert(0, [None, None, batter_batting.name])
					break
				if event is "HR":
					bases.insert(0, [None, None, None, batter_batting.name])
					break
				else:
					strikes +=1
			if len(bases) > 3:
					difference = len(bases) - 3
					bases = bases[:-difference]
					off_bases = bases[3:]
					for value in off_bases:
						if value is not None:
							away_score+=1
			batterCount += 1
			if batterCount > len(away_batters)-1:
				batterCount = 0
			if strikes == 3:
				outs += 1
	return (home_score, away_score)

				



