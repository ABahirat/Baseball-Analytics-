use retrosheet;

select concat(t.LOC_TEAM_TX, " ", t.NAME_TEAM_TX) as home_team_name, concat(t1.LOC_TEAM_TX, " ", t1.NAME_TEAM_TX) as away_team_name, 
avg(HOME_SCORE_CT > AWAY_SCORE_CT)
from games join teams t on t.TEAM_ID = HOME_TEAM_ID join teams t1 on  t1.TEAM_ID =  AWAY_TEAM_ID
group by home_team_name, away_team_name, HOME_TEAM_ID, AWAY_TEAM_ID ;

select HOME_TEAM_ID, AWAY_TEAM_ID, avg(HOME_SCORE_CT/ (AWAY_SCORE_CT+HOME_SCORE_CT))
from games group by HOME_TEAM_ID, AWAY_TEAM_ID;