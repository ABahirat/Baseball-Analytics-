use lahman2016;
select distinct concat(m.nameFirst, " ", m.nameLast) as name, t.name as team, (b.H-b.2B-b.3B-b.HR)/(b.H) as 1Bprob, (b.2B)/(b.H) as 2Bprob, (b.3B)/(b.H) as 3Bprob, (b.HR)/(b.H) as HRprob, (b.H)/(b.AB) as BA,
(b.H-b.2B-b.3B-b.HR)/(b.H) + (b.2B)/(b.H) + (b.3B)/(b.H) + (b.HR)/(b.H) as totalprob
from batting as b
inner join teams as t on t.teamID = b.teamID and t.yearID = b.yearID
inner join master as m on m.playerID = b.playerID
where b.yearID = 2016 and b.AB > 30;

select distinct concat(m.nameFirst, " ", m.nameLast) as name, t.name as team, (p.so/p.bfp - .20752) as DASP from pitching as p #Difference from Average Strikeout Probability
inner join teams as t on t.teamID = p.teamID and t.yearID = p.yearID
inner join master as m on m.playerID = p.playerID
where p.yearID = 2016 and p.G > 3;

select name from teams where yearID = 2016; #just teams

