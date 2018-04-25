import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.title("SWP Stat Generator")

homeBatterCombos = []
awayBatterCombos = []

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
homePitcherLabel.grid(column=0,row=12)

awayPitcherLabel = tk.Label(window,text="Pitcher: ")
awayPitcherLabel.grid(column=2,row=12)

vertSpacerTopLabel = tk.Label(window,text=" ")
vertSpacerTopLabel.grid(column=0,row=2)

vertSpacerMidLabel = tk.Label(window,text=" ")
vertSpacerMidLabel.grid(column=0,row=13)

vertSpacerBotLabel = tk.Label(window,text=" ")
vertSpacerBotLabel.grid(column=0,row=15)

horiSpacerLabel = tk.Label(window,text="     ")
horiSpacerLabel.grid(column=4,row=0)

#combobox logic
def selectHomeTeam(eventObject):
    #determine list of valid players in string format
    #for box in homeBatterCombos:
    #   box['values'] = (###list of valid batters for this team###)
    #homePitcherCombo['values'] = (###list of valid pitchers for this team###)

def selectAwayTeam(eventObject):
    #determine valid players in string array format
    #for box in awayBatterCombos:
    #   box['values'] = (###list of valid batters for this team###)
    #awayPitcherCombo['values'] = (###list of valid pitchers for this team###)

#comboboxes
homeTeamCombo = Combobox(window)
#homeTeamCombo['values'] = #array of all possible teams
homeTeamCombo['values'] = ("Colorado Rockies","Just Ameya")
homeTeamCombo.current(1)
homeTeamCombo.grid(column=1,row=1)
homeTeamCombo.bind("<<ComboboxSelected>>", selectHomeTeam)

awayTeamCombo = Combobox(window)
#awayTeamCombo['values'] = #array of all possible teams
awayTeamCombo['values'] = ("Colorado Rockies","Just Ameya")
awayTeamCombo.current(0)
awayTeamCombo.grid(column=3,row=1)
homeTeamCombo.bind("<<ComboboxSelected>>", selectAwayTeam)

for i in range(0,8):
    homeBatterCombos.append(Combobox(window))
    homeBatterCombos[i]['values'] = (".")
    homeBatterCombos[i].current(0)
    homeBatterCombos[i].grid(column=1,row=3+i)

for i in range(0,7):
    awayBatterCombos.append(Combobox(window))
    awayBatterCombos[i]['values'] = (".")
    awayBatterCombos[i].current(0)
    awayBatterCombos[i].grid(column=3,row=3+i)

homePitcherCombo = Combobox(window)
homePitcherCombo['values'] = (".")
homePitcherCombo.current(0)
homePitcherCombo.grid(column=1,row=12)

awayPitcherCombo = Combobox(window)
awayPitcherCombo['values'] = (".")
awayPitcherCombo.current(0)
awayPitcherCombo.grid(column=3,row=12)

#buttons
def doCalculation():
    #do the main logic and start the backend

startButton = tk.Button(window,text="Calculate",command=doCalculation)
startButton.grid(column=1,row=14)

exitButton = tk.Button(window,text="Exit")
exitButton.grid(column=3,row=14)

#combobox logic




window.mainloop()
