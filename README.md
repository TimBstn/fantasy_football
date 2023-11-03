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
- The Neural Networks are simply given the data set in the original form. Feature selection and
normalization are not performed. The Neural Network can implicitly do this or not depending on
whether it improves their predictions. Before applying SVR, I scaled the features down to the interval [0, 1] in order to improve the performance specifically for linear and polynomial kernel SVR.
After the normalization comes the feature selection. (Lutz 2015)
- First of all, I filtered the data such that only Quarterbacks
(QB) with at least 5 passes are selected. This restriction is necessary such that non-QB players or
backup QBs are not taken in to account.
- Then, for every game I included as features the current
age of the QB, his experience in years as a professional, the stats of the previous game, the average
stats of the last 10 games as well as the stats of the opposing defense in their last game and their
average over the last 10 games.
- For
defenses, there are 4 categories, namely the number of points allowed, passing and rushing yards
allowed as well as turnovers forced.
- First-year players become a separate
problem because the predictions can not be based on their past production. To overcome this, they
are assigned the average over all first-year QB per-game average stats for the first game. From the
second game on, their own statistics are used.
- Therefore it makes sense to restrict the evaluation to the best QBs that
actually have a chance to be used in Fantasy Football. In standard leagues with 12 teams one QB
starts for every team, so the evaluation considers the predictions of the 24 best QBs 
-  For reasons of comparability with other sources three different errors are shown: Root Mean Squared Error (RMSE),
Mean Absolute Error (MAE) and Mean Relative Error (MRE)
- n. In order to take the trend better into account, the exponentially
weighted moving average (EWMA) could be used to substitute the current game statistics.
- There are also several other interesting features that could be taken into account, such as the injury
report status, suspensions, draft position and college statistics for first-year players, postseason and
preseason performance, overall team performance and changes on the team such as trades or injuries.
- factors (Fokoue 2001): In a similar spirit, this paper considers five years (2006-2010) worth of NFL
end of season statistics, and seek to use data mining and machine learning techniques to
find out if teams can be automatically classified as good or bad based on those statistics,
and also identify as much as possible those factors that seem to discriminate between the
good and the bad teams.
- use p value as in Fokoue 2001 to select features for linear regression

# Next Steps
- vs divisional opponent, AFC, NFC
- Projected Points of ESPN
- Time Series LSTM-RNN model
- use NLP such as in (Baugham 2021): The paper details a novel machine learning NLP pipeline incorporating statistical entity detectors and deep learning feedforward neural networks with 98 layers for player classification. It achieves a high analogy test accuracy of 100% and keyword test accuracy of 80% using news articles, videos, and expert opinions, while providing player classifications and point projections with low Root Mean Squared Error.
- create starting lineup (Gupta 2019); "
Using the points for the past years, time series forecasting techniques were leveraged to predict next year’s performance. To
be robust in approach and consider both linearity and non-linearity, Autoregressive Integrated Moving Average (ARIMA) and
Recurrent Neural Networks (RNNs) were considered for modelling. After obtaining the points for the entire roster, Linear
Programming (LPP) basics were applied to adhere to all constraints and finalise a suitable starting dream team."
# References

## Data

The data structure is displayed in [this database relation diagram](https://dbdiagram.io/d/Fantasy-65446f667d8bbd646565521a).

- [ ] FantasyData. (11/2023). Fantasy Football Stats and Season Leaders. https://fantasydata.com/nfl/fantasy-football-leaders
- [ ] SportsOddsHistory. (11/2023). Historical NFL Game Odds. https://www.sportsoddshistory.com/nfl-game-odds/
- [x] Pro Football Reference. (11/2023). NFL Coaches. https://www.pro-football-reference.com/years/2023/coaches.htm
- [ ] Pro Football Reference. (11/2023). NFL, AFL, and AAFC Stadiums. https://www.pro-football-reference.com/stadiums/
- [ ] Pro Football Reference. (11/2023). NFL Weeks. https://www.pro-football-reference.com/years/2023/week_1.htm
- [ ] Pro Football Reference. (11/2023). NFL Standings & Team Stats. https://www.pro-football-reference.com/years/2023/

## Research
- [x] [Baughman, A., Forester, M., Powell, J., Morales, E., McPartlin, S., & Bohm, D. (2021). Deep Artificial Intelligence for Fantasy Football Language Understanding.](https://arxiv.org/ftp/arxiv/papers/2111/2111.02874.pdf)
- [x] [Fokoue, E., and Foehrenbach D. (2001). A statistical data mining approach to determining the factors that distinguish championship caliber teams in the National Football League.](https://scholarworks.rit.edu/cgi/viewcontent.cgi?article=2749&context=article)
- [x] [Gupta, A. (2019). Time Series Modeling for Dream Team in Fantasy Premier League](https://arxiv.org/ftp/arxiv/papers/1909/1909.12938.pdf)
- [x] [Lutz, R. (2015). Fantasy Football Prediction.](https://arxiv.org/pdf/1505.06918.pdf)
- [ ] [Ramdas, Delano. (2022). Using Convolution Neural Networks to Predict the Performance of Footballers in the Fantasy Premier League.](https://www.researchgate.net/publication/360009648_Using_Convolution_Neural_Networks_to_Predict_the_Performance_of_Footballers_in_the_Fantasy_Premier_League)
