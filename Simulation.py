import csv
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

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
        def __init__(self, name, DASP):
                # Difference form average strikeout probability
                self.DASP = DASP
                self.name = name

def get_true_BA(Batter, Pitcher):

        return (max(Batter.BA + Pitcher.DASP,0)) * (0.5) #roughly account for ground-outs by universally reducing BA

def determine_event(Batter, Pitcher):
        # Get true batting average
        true_BA = get_true_BA(Batter, Pitcher)
        hit = choice([0, 1], p=[1-true_BA, true_BA])
        if hit:
                mix = Batter.singles_avg + Batter.doubles_avg + Batter.triples_avg + Batter.HR_avg
                if mix != 1:
                        Batter.singles_avg += 1 - mix
                determine = "null"
                while determine == "null":
                        determine = choice(["single", "double", "triple", "HR"],p=[Batter.singles_avg, Batter.doubles_avg, Batter.triples_avg, Batter.HR_avg])
                return determine
        else:
                return "strike"

def get_pitcher(name):
        f = open("pitching.csv")
        csv_f = csv.reader(f)
        for row in csv_f:
                if row[0] == name:
                        return Pitcher(name, float(row[2]))


def get_batter(name):
        f = open("batting.csv")
        csv_f = csv.reader(f)
        for row in csv_f:
                if row[0] == name:
                        return Batter(name, float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]))


def simulate(home_batters, away_batters, away_pitcher, home_pitcher):
        bases = [None, None, None]
        home_score = 0
        away_score = 0
        away_pitcher = get_pitcher(away_pitcher)
        home_pitcher = get_pitcher(home_pitcher)
        i = 0
        while i < 9 or home_score == away_score:
                i += 1
                batterCount = 0
                outs = 0
                bases = [None,None,None]
                while(outs < 3):
                        # account for 3 strikes
                        batting_batter = get_batter(home_batters[batterCount])
                        strikes = 0
                        while(strikes < 3 and strikes > -1):
                                event = determine_event(batting_batter, away_pitcher)
                                #print(batting_batter.name + " got " + event)
                                if event == "single":
                                        # insert [Player] to beginning of list
                                        #bases.insert(0, batter_batting.name)
                                        bases = [batting_batter.name] + bases
                                        strikes = -1
                                elif event == "double":
                                        #bases.insert(0, [None, batter_batting.name])
                                        bases = [None, batting_batter.name] + bases
                                        strikes = -1
                                elif event == "triple":
                                        #bases.insert(0, [None, None, batter_batting.name])
                                        bases = [None, None, batting_batter.name] + bases
                                        strikes = -1
                                elif event == "HR":
                                        #bases.insert(0, [None, None, None, batter_batting.name])
                                        bases = [None, None, None, batting_batter.name] + bases
                                        strikes = -1
                                else:
                                        strikes += 1
                        if len(bases) > 3:
                                        difference = len(bases) - 3
                                        off_bases = bases[3:]
                                        bases = bases[:3]
                                        for value in off_bases:
                                                if value is not None:
                                                        home_score+=1               
                        batterCount += 1
                        if batterCount > len(home_batters)-1:
                                batterCount = 0
                        if strikes == 3:
                                #print("Strikeout")
                                outs += 1
                #print("Mid of inning " + str(i+1) + " HOME " + str(home_score) + " AWAY " + str(away_score))
                outs = 0
                batterCount = 0
                bases = [None,None,None]
                while(outs < 3):
                        # account for 3 strikes
                        batting_batter = get_batter(away_batters[batterCount])
                        strikes = 0
                        while(strikes < 3 and strikes > -1):
                                event = determine_event(batting_batter, home_pitcher)
                                #print(batting_batter.name + " got " + event)
                                if event == "single":
                                        # insert [Player] to beginning of list
                                        #bases.insert(0, batter_batting.name)
                                        bases = [batting_batter.name] + bases
                                        strikes = -1
                                elif event == "double":
                                        #bases.insert(0, [None, batter_batting.name])
                                        bases = [None, batting_batter.name] + bases
                                        strikes = -1
                                elif event == "triple":
                                        #bases.insert(0, [None, None, batter_batting.name])
                                        bases = [None, None, batting_batter.name] + bases
                                        strikes = -1
                                elif event == "HR":
                                        #bases.insert(0, [None, None, None, batter_batting.name])
                                        bases = [None, None, None, batting_batter.name] + bases
                                        strikes = -1
                                else:
                                        strikes += 1
                        if len(bases) > 3:
                                difference = len(bases) - 3
                                off_bases = bases[3:]
                                bases = bases[:3]
                                for value in off_bases:
                                        if value is not None:
                                                away_score+=1
                                                #print("Score")
                        batterCount += 1
                        if batterCount > len(away_batters)-1:
                                batterCount = 0
                        if strikes == 3:
                                #print("Strikeout")
                                outs += 1
                #print("End of inning " + str(i+1) + " HOME " + str(home_score) + " AWAY " + str(away_score))
        return (home_score, away_score)

def bulk_win_percentage(home_team, away_team, team_batters, team_pitchers):
        # functon that will bulk one team against another, randomizing pitchers and randomizing batter
        
        #TODO: 
        # Run expectancy for bulk calculation
            # Number of games to runs
        # Win expectancy for bulk calculation vs team matchup win expectancy in lahman
        # Run expectancy for individual game 
        homeWins = 0
        awayWins = 0
        home_score_list = []
        away_score_list = []
        for i in range(0, 100):
                home_batters = team_batters[home_team]
                away_batters = team_batters[away_team]

                home_batters = random.sample(home_batters, 9)
                away_batters = random.sample(away_batters, 9)

                home_pitchers = team_pitchers[home_team]
                away_pitchers = team_pitchers[away_team]

                home_pitcher = random.sample(home_pitchers, 1)
                away_pitcher = random.sample(away_pitchers, 1)

                results = simulate(home_batters, away_batters, away_pitcher[0], home_pitcher[0])
                home_score_list.append(results[0])
                away_score_list.append(results[1])

                if results[0] > results[1]:
                        homeWins += 1
                else:
                        awayWins += 1

        SWP = float(homeWins) / float(homeWins+awayWins)
        print("SWP = " + str(SWP))
        teams_WP = open("teams_WP.csv")
        csv_f = csv.reader(teams_WP)
        for row in csv_f:
            if row[0] == home_team and row[1] == away_team:
                print("AWP = " + str(row[2]))

        #x = np.random.normal(size = 1000)
        plt.hist([home_score_list, away_score_list], color=['g','b'], alpha=0.8, bins=30, label=["Home Team", "Away Team"])
        plt.ylabel('Games')
        plt.xlabel("Runs Scored")
        plt.title("Run Expectancy for Teams")
        plt.legend(loc='upper right')
        plt.show()



def main():
        home_batters = ["Nick Ahmed", "Michael Bourn", "Archie Bradley", "Socrates Brito", "Welington Castillo", "Patrick Corbin", "Brandon Drury", "Paul Goldschmidt", "Tuffy Gosewisch"]
        home_pitcher = "Jake Barrett"
        away_batters = ["Erick Aybar", "Gordon Beckham", "Emilio Bonifacio", "Daniel Castro", "Chase d'Arnaud", "Tyler Flowers", "Mike Foltynewicz", "Jeff Francoeur"]
        away_pitcher = "Dario Alvarez"

        print(simulate(home_batters, away_batters, away_pitcher, home_pitcher))


if __name__ == "__main__":
        main()


                                



