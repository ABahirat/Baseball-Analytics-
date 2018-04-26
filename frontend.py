import tkinter as tk
import Simulation
from tkinter.ttk import *
import csv

possibleTeams = []
teamBatters = {}
teamPitchers = {}

with open('teams.csv') as csvfile: #instantiate teams
    reader = csv.DictReader(csvfile)
    for line in reader: #read the csv
        value = line["name"]
        possibleTeams.append(value) #append each team to list of teams
        teamBatters[value] = [] #and add an empty array to track batters and pitchers for each team
        teamPitchers[value] = []

with open('batting.csv') as csvfile: #instantiate batters
    reader = csv.DictReader(csvfile) #reads in the csv where each line is a dictionary based on headers
    for line in reader:
        teamBatters[line["team"]].append(line["name"])

with open('pitching.csv') as csvfile: #instantiate pitchers
    reader = csv.DictReader(csvfile) #reads in the csv where each line is a dictionary based on headers
    for line in reader:
        teamPitchers[line["team"]].append(line["name"])

window = tk.Tk()
window.title("SWP Stat Generator")

homeBatterCombos = []
homeBatterValues = []
awayBatterCombos = []
awayBatterValues = []

#labels
homeTeamLabel = tk.Label(window,text="Home Team: ")
homeTeamLabel.grid(column=1,row=0)

awayTeamLabel = tk.Label(window,text="Away Team: ")
awayTeamLabel.grid(column=3,row=0)

homeBatterLabel = tk.Label(window,text="Batters: ")
homeBatterLabel.grid(column=0,row=3)

awayBatterLabel = tk.Label(window,text="Batters: ")
awayBatterLabel.grid(column=2,row=3)

homePitcherLabel = tk.Label(window,text="Pitcher: ")
homePitcherLabel.grid(column=0,row=13)

awayPitcherLabel = tk.Label(window,text="Pitcher: ")
awayPitcherLabel.grid(column=2,row=13)

vertSpacerTopLabel = tk.Label(window,text=" ")
vertSpacerTopLabel.grid(column=0,row=2)

vertSpacerMidLabel = tk.Label(window,text=" ")
vertSpacerMidLabel.grid(column=0,row=14)

vertSpacerBotLabel = tk.Label(window,text=" ")
vertSpacerBotLabel.grid(column=0,row=16)

horiSpacerLabel = tk.Label(window,text="     ")
horiSpacerLabel.grid(column=4,row=0)

#combobox logic
def selectHomeTeam(eventObject):
    i = 0
    for box in homeBatterCombos:
        box['values'] = teamBatters[homeTeam.get()]
        box.current(i)
        i += 1
    homePitcherCombo['values'] = teamPitchers[homeTeam.get()]
    homePitcherCombo.current(0)

def selectAwayTeam(eventObject):
    i = 0
    for box in awayBatterCombos:
        box['values'] = teamBatters[awayTeam.get()]
        box.current(i)
        i += 1
    awayPitcherCombo['values'] = teamPitchers[awayTeam.get()]
    awayPitcherCombo.current(0)

#comboboxes
homeTeam = tk.StringVar()
homeTeamCombo = Combobox(window, textvariable=homeTeam)
homeTeamCombo['values'] = possibleTeams
homeTeamCombo.current(0)
homeTeamCombo.grid(column=1,row=1)
homeTeamCombo.bind("<<ComboboxSelected>>", selectHomeTeam)

awayTeam = tk.StringVar()
awayTeamCombo = Combobox(window, textvariable=awayTeam)
awayTeamCombo['values'] = possibleTeams
awayTeamCombo.current(1)
awayTeamCombo.grid(column=3,row=1)
awayTeamCombo.bind("<<ComboboxSelected>>", selectAwayTeam)

for i in range(0,9):
    homeBatterValues.append(tk.StringVar())
    homeBatterCombos.append(Combobox(window, textvariable=homeBatterValues[i]))
    homeBatterCombos[i]['values'] = (".")
    homeBatterCombos[i].current(0)
    homeBatterCombos[i].grid(column=1,row=3+i)

for i in range(0,8):
    awayBatterValues.append(tk.StringVar())
    awayBatterCombos.append(Combobox(window, textvariable=awayBatterValues[i]))
    awayBatterCombos[i]['values'] = (".")
    awayBatterCombos[i].current(0)
    awayBatterCombos[i].grid(column=3,row=3+i)

homePitcher = tk.StringVar()
homePitcherCombo = Combobox(window, textvariable=homePitcher)
homePitcherCombo['values'] = (".")
homePitcherCombo.current(0)
homePitcherCombo.grid(column=1,row=13)

awayPitcher = tk.StringVar()
awayPitcherCombo = Combobox(window, textvariable=awayPitcher)
awayPitcherCombo['values'] = (".")
awayPitcherCombo.current(0)
awayPitcherCombo.grid(column=3,row=13)

selectHomeTeam(homeTeamCombo)
selectAwayTeam(awayTeamCombo)

#buttons
def doCalculate():
    print("=== HOME TEAM ===")
    simHomeBatters = ""
    homeBatters = []
    for val in homeBatterValues:
        simHomeBatters += val.get() + ", "
        homeBatters += val.get()
    simHomeBatters = simHomeBatters[:-2]
    print("Batters: " + simHomeBatters)
    print("Pitcher: " + homePitcher.get())
    print("=== AWAY TEAM ===")
    simAwayBatters = ""
    awayBatters = []
    for val in awayBatterValues:
        simAwayBatters += val.get() + ", "
        awayBatters += val.get()
    simAwayBatters = simAwayBatters[:-2]
    print("Batters: " + simAwayBatters)
    print("Pitcher: " + awayPitcher.get())
    #do the main logic and start the backend
    print(Simulation.simulate())

def doExit():
    quit()

startButton = tk.Button(window,text="Calculate",command=doCalculate)
startButton.grid(column=1,row=15)

exitButton = tk.Button(window,text="Exit",command=doExit)
exitButton.grid(column=3,row=15)

#combobox logic




window.mainloop()
