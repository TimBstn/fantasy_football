# Fantasy Football - Use Machine Learning to predict future performance 

Fantasy football has become a widely popular and engaging pastime, with millions of participants worldwide. Accurate prediction of player performance and points is crucial for fantasy football enthusiasts to make informed decisions when selecting their fantasy teams. This project addresses the problem of predicting fantasy football points using machine learning techniques, specifically focusing on regression and neural networks.

In this project, we employ a comprehensive dataset of historical player statistics, encompassing variables such as player attributes, team dynamics, and previous performance. We explore the performance of two primary machine learning methodologies: multiple linear regression and artificial neural networks. Our analysis involves feature engineering and selection to enhance the predictive power of the models.

We evaluate the effectiveness of these techniques by considering metrics such as Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and R-squared. Additionally, we investigate the potential of model interpretability, enabling fantasy football enthusiasts to gain insights into the factors influencing player performance predictions.

The results of our experiments demonstrate the comparative strengths and weaknesses of regression and neural networks in predicting fantasy football points. We also discuss the implications of our findings for fantasy football enthusiasts and researchers in the field of sports analytics. This prject serves as a valuable reference for those seeking to leverage machine learning techniques to gain a competitive edge in the world of fantasy football.

# Notes
- prediction is PPR style - explain
- https://github.com/DelanoDZR/fpl-predictor-neural-nets/blob/main/models.py - models

# Prediction
- use average of last n games
- for regression: normalize data before predicting
- opponent record as percentage
- home/away game?
- opponents rank defensive, offensive (split by receiving, rushing, total)

# Next Steps
- vs divisional opponent, AFC, NFC
- Projected Points of ESPN
- Weather

# References

## Data
- FantasyPros. (11/2023). Fantasy Football Stats. https://www.fantasypros.com/nfl/stats/qb.php
- FantasyData. (11/2023). Fantasy Football Stats and Season Leaders. https://fantasydata.com/nfl/fantasy-football-leaders
- SportsOddsHistory. (11/2023). Historical NFL Game Odds. https://www.sportsoddshistory.com/nfl-game-odds/
- NFL. (11/2023). Games. https://www.nfl.com/scores/
- Pro Football Reference. (11/2023). NFL Coaches. https://www.pro-football-reference.com/years/2023/coaches.htm

## Research
- [Baughman, A., Forester, M., Powell, J., Morales, E., McPartlin, S., & Bohm, D. (2021). Deep Artificial Intelligence for Fantasy Football Language Understanding.](https://arxiv.org/ftp/arxiv/papers/2111/2111.02874.pdf)
- [Gupta, A. (2019). Time Series Modeling for Dream Team in Fantasy Premier League](https://arxiv.org/ftp/arxiv/papers/1909/1909.12938.pdf)
- [Lutz, R. (2015). Fantasy Football Prediction.](https://arxiv.org/pdf/1505.06918.pdf)
- [Ramdas, Delano. (2022). Using Convolution Neural Networks to Predict the Performance of Footballers in the Fantasy Premier League.](https://www.researchgate.net/publication/360009648_Using_Convolution_Neural_Networks_to_Predict_the_Performance_of_Footballers_in_the_Fantasy_Premier_League)