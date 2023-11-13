# Factor Dictionary

The provided data dictionaries outline the key columns in a dataframe containing comprehensive statistics for NFL teams. Covering a range of metrics from total yards and turnovers to passing efficiency and special teams performance, this dataset facilitates a detailed analysis of team performance. Each column provides a specific insight into the dynamics of NFL teams, with the binary "made_playoffs" column serving as a target variable for investigating the factors influencing playoff qualification. This structured data dictionary serves as a valuable guide for researchers and analysts seeking to uncover patterns and trends in the complex landscape of NFL team performance.

## Offense + Offensive Special Teams

year: Year of season. <br>
team_id: Unique identifier for each NFL team. <br>
games: Number of games played in the season. <br>
total_yards: Total offensive yards gained by the team (through passing and rushing). <br>
offensive_plays: Total number of offensive plays executed. <br>
yards_per_play: Average yards gained per offensive play. <br>
turnovers_lost: Total number of turnovers lost by the team. <br>
first_downs: Total number of first downs achieved. <br>
passes_completed: Number of passes completed by the team. <br>
passes_attempted: Total number of passing attempts. <br>
net_yards_gained_per_pass: Net yards gained per passing attempt. <br>
yards_passing: Total yards gained through passing. <br>
touchdowns_passing: Total passing touchdowns. <br>
interceptions: Number of interceptions thrown. <br>
rushing_attempted: Number of rushing attempts. <br> 
yards_rushing: Total yards gained through rushing. <br>
rushing_yards_per_attempt: Average yards gained per rushing attempt. <br>
touchdowns_rushing: Total rushing touchdowns. <br>
penalties_opponent: Total number of penalties committed by opponents. <br>
yards_penalties_opponent: Total yards penalized against opponents. <br>
pct_drives_ending_score: Percentage of offensive drives ending in a score. <br>
pct_drives_ending_turnover: Percentage of offensive drives ending in a turnover. <br>
completion_pct: Percentage of completed passes. <br>
yards_per_game: Average yards gained per game by offensive plays. <br>
touchdown_interception_ratio: Ratio of touchdowns to interceptions.<br> 
pass_run_ratio: Ratio of passes to runs.<br>
total_touchdowns: Total touchdowns scored. <br>
two_points_made: Total two-point conversions made. <br>
two_points_attempted: Total two-point conversion attempts. <br>
extra_points_made: Total extra points made. <br>
extra_points_attempted: Total extra point attempts. <br>
field_goals_made: Total field goals made. <br>
field_goals_attempted: Total field goal attempts. <br>
points_per_game: Average points scored per game. <br>
field_goal_pct: Field goal percentage. <br>
extra_point_pct: Extra point percentage. <br>
two_point_pct: Two-point conversion percentage. <br>
punts_returned: Number of punts returned. <br>
yards_per_punt_return: Average yards gained per punt return. <br>
kickoffs_returned: Number of kickoffs returned. <br>
yards_per_kickoff_return: Average yards gained per kickoff return. <br>
all_purpose_yards: Total all-purpose yards including offensive, defense, special teams. <br>
punts_avg_yards: Average yards per punt. <br>
punts_touchback_pct: Percentage of punts resulting in touchbacks. <br>
punts_inside_20_pct: Percentage of punts placed inside the opponent's 20-yard line. <br>
third_down_conversion_pct: Percentage of successful third-down conversions. <br>
fourth_down_conversion_pct: Percentage of successful fourth-down conversions. <br>
red_zone_conversion_pct: Percentage of successful red zone conversions. <br>
made_playoffs: Binary indicator (0 or 1) denoting whether the team made the playoffs. 

## Defense + Defensive Special Teams

year: Year of season.<br>
team_id: Unique identifier for each NFL team.<br>
games: Number of games played in the season.<br>
points_against: Total points scored against the team.<br>
total_yards: Total defensive yards allowed.<br>
defensive_plays: Total number of defensive plays executed.<br>
yards_per_play: Average yards allowed per defensive play.<br>
takeaways: Total number of takeaways by the defense.<br>
first_downs: Total number of first downs allowed.<br>
passes_completed: Number of passes completed by opponents.<br>
passes_attempted: Total number of passing attempts by opponents.<br>
yards_passing: Total yards gained through passing by opponents.<br>
touchdowns_passing: Total passing touchdowns allowed.<br>
interceptions: Number of interceptions made by the defense.<br>
net_yards_gained_per_pass: Net yards gained per passing attempt by opponents.<br>
rushing_attempted: Number of rushing attempts by opponents.<br>
yards_rushing: Total yards gained through rushing by opponents.<br>
touchdowns_rushing: Total rushing touchdowns allowed.<br>
rushing_yards_per_attempt: Average yards allowed per rushing attempt.<br>
penalties_commited: Total number of penalties committed by the defense.<br>
yards_penalties_commited: Total yards penalized against the defense.<br>
first_downs_penalties_commited: Total number of first downs achieved by opponents due to defensive penalties.<br>
pct_drives_ending_score: Percentage of defensive drives ending in an opponent's score.<br>
pct_drives_ending_turnover: Percentage of defensive drives ending in a takeaway.<br>
completion_pct: Completion percentage by opponents.<br>
yards_per_game: Average yards allowed per game.<br>
touchdown_interception_ratio: Ratio of touchdowns allowed to interceptions made.<br>
total_touchdowns: Total touchdowns allowed.<br>
points_per_game: Average points allowed per game.<br>
punts_returned: Number of punts returned by opponents.<br>
yards_per_punt_return: Average yards gained per punt return by opponents.<br>
kickoffs_returned: Number of kickoffs returned by opponents.<br>
yards_per_kickoff_return: Average yards gained per kickoff return by opponents.<br>
punts_avg_yards: Average yards per punt by the opponents.<br>
third_down_conversion_pct: Percentage of successful third-down conversions by opponents.<br>
fourth_down_conversion_pct: Percentage of successful fourth-down conversions by opponents.<br>
red_zone_conversion_pct: Percentage of successful red zone conversions by opponents.<br>
made_playoffs: Binary indicator (0 or 1) denoting whether the team made the playoffs.<br>