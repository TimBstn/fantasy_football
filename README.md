# FootStatsPro: Football Data Mining and Playoff Predictive Analytics

This project presents a rigorous statistical analysis of the factors influencing National Football League (NFL) team qualification for the playoffs, leveraging a comprehensive database encompassing end-of-season offense, defense, kicking, punting, and special teams statistics. The study employs a multifaceted approach, utilizing statistical tests such as t-tests, XGBoost, and Principal Component Analysis (PCA) to identify and extract the most influential factors affecting playoff outcomes.

The research delves into both offensive and defensive dimensions, unraveling the intricate interplay between various performance metrics and postseason success. Through systematic examination and hypothesis testing, the study aims to contribute valuable insights into the nuanced dynamics that separate playoff-bound teams from those falling short.

Key objectives include identifying statistically significant indicators and elucidating their impact on playoff qualification. By employing PCA and XGBoost, the paper seeks to distill complex datasets into their essential components, offering a clearer understanding of the critical variables at play. This research not only sheds light on the relative importance of different offensive and defensive metrics but also provides a holistic perspective on the role of special teams and kicking in determining playoff success.

The findings of this study are expected to provide NFL analysts, coaches, and enthusiasts with actionable insights, enabling more informed decision-making and strategic planning. Furthermore, the methodology employed in this research may serve as a template for similar analyses in other sports contexts, contributing to the broader field of sports analytics.

## Data Dictionary

For a detailed understanding of each column in the dataset, refer to the [Factor Dictionary](factor_dictionary.md), which provides clear explanations for metrics such as total yards, turnovers, passing efficiency, and more. This dictionary serves as a valuable resource for researchers and analysts aiming to unravel the intricacies of NFL team performance.

## Analytics 
### t-test

In the investigation of factors influencing NFL playoff qualification, a t-test is employed to assess the significance of individual factors related to offense, defense, and special teams. The t-test is a statistical method that evaluates whether the means of two groups, in this case, playoff and non-playoff teams, are significantly different from each other. By calculating the t-statistic and obtaining a p-value, researchers can determine the probability of observing such a difference by random chance alone.

Setting a significance level, or alpha, at 0.05, if the p-value is below this threshold, it indicates that the observed difference is unlikely due to chance, suggesting that the factor may be a meaningful predictor of playoff success.

### Gradient Boosting

Continuing the investigation into the factors impacting NFL playoff qualification, classification using XGBoost is employed to extract the significance of each factor. XGBoost, an advanced machine learning algorithm, allows for a more sophisticated analysis of how offensive, defensive, and special teams metrics collectively contribute to predicting whether a team makes the playoffs or not.

In this approach, XGBoost assigns importance scores to each feature, revealing the relative significance of different factors in determining playoff outcomes. By leveraging the strengths of gradient boosting and decision tree ensembles, XGBoost excels at capturing complex relationships within the data.

This classification technique goes beyond traditional regression methods, providing a predictive model that can identify patterns and interactions among various performance metrics. The importance scores derived from XGBoost shed light on which factors play a pivotal role in distinguishing playoff-bound teams from those that do not qualify. Utilizing XGBoost for classification enhances the depth of analysis, offering valuable insights into the nuanced dynamics that underlie NFL playoff success.

### Principal Component Analysis (PCA)
In the final stage of our exploration into the factors influencing NFL playoff qualification, Principal Component Analysis (PCA) is employed to distill the significance of each factor. PCA is a dimensionality reduction technique that transforms the original variables, such as offensive, defensive, and special teams metrics, into a set of linearly uncorrelated components.

By applying PCA, we aim to identify the most influential components that contribute to the variability in playoff outcomes. This method allows us to uncover latent patterns and relationships within the data, providing a simplified yet informative representation of the key factors at play.

PCA serves as a valuable tool for feature extraction and dimensionality reduction, offering a unique perspective on the underlying structure of the data. By examining the loadings of each variable on the principal components, we gain insights into which offensive, defensive, and special teams metrics contribute most significantly to the variability in NFL playoff qualification. PCA adds depth to our analysis by revealing the fundamental factors that shape a team's success in securing a coveted playoff spot.

## Analysis
(Fokoue 2001): In a similar spirit, this paper considers five years (2006-2010) worth of NFL end of season statistics, and seek to use data mining and machine learning techniques to find out if teams can be automatically classified as good or bad based on those statistics, and also identify as much as possible those factors that seem to discriminate between the good and the bad teams.

## Next Steps
1. Predicting Regular Season Performance: Develop models to predict a team's regular-season performance, considering factors such as player statistics, team dynamics, strength of schedule, and historical performance. 
2. Draft Strategy Evaluation: Assess the effectiveness of teams' draft strategies by analyzing the performance of drafted players over time. Examine whether high draft picks lead to improved playoff prospects.
3. Home Field Advantage Analysis: Study the significance of home field advantage in the context of playoff qualification. Analyze teams' performance at home versus away and assess whether certain teams consistently perform better in specific environments.
4. Weather Impact on Performance: Investigate how weather conditions during games influence team performance. Consider factors like temperature, precipitation, and wind speed 
5. Game Outcome Prediction: Extend the analysis to predict the outcome of individual games during the regular season. Explore how well models can predict wins and losses based on various factors.
6. Coin Toss Analysis: Explore the impact of the coin toss on a team's success. Investigate whether winning the coin toss at the beginning of a game correlates with a higher likelihood of winning.

# References

## Data

The data structure is displayed in [this database relation diagram](https://dbdiagram.io/d/Fantasy-65446f667d8bbd646565521a).

- [ ] FantasyData. (11/2023). Fantasy Football Stats and Season Leaders. https://fantasydata.com/nfl/fantasy-football-leaders
- [ ] SportsOddsHistory. (11/2023). Historical NFL Game Odds. https://www.sportsoddshistory.com/nfl-game-odds/
- [x] Pro Football Reference. (11/2023). NFL Coaches. https://www.pro-football-reference.com/years/2023/coaches.htm
- [x] Pro Football Reference. (11/2023). NFL, AFL, and AAFC Stadiums. https://www.pro-football-reference.com/stadiums/
- [x] Pro Football Reference. (11/2023). NFL Weeks. https://www.pro-football-reference.com/years/2023/games.htm
- [x] Pro Football Reference. (11/2023). NFL Standings & Team Stats. https://www.pro-football-reference.com/years/2023/

## Research
- [x] [Baughman, A., Forester, M., Powell, J., Morales, E., McPartlin, S., & Bohm, D. (2021). Deep Artificial Intelligence for Fantasy Football Language Understanding.](https://arxiv.org/ftp/arxiv/papers/2111/2111.02874.pdf)
- [x] [Fokoue, E., and Foehrenbach D. (2001). A statistical data mining approach to determining the factors that distinguish championship caliber teams in the National Football League.](https://scholarworks.rit.edu/cgi/viewcontent.cgi?article=2749&context=article)
- [x] [Gupta, A. (2019). Time Series Modeling for Dream Team in Fantasy Premier League](https://arxiv.org/ftp/arxiv/papers/1909/1909.12938.pdf)
- [x] [Lutz, R. (2015). Fantasy Football Prediction.](https://arxiv.org/pdf/1505.06918.pdf)
- [ ] [Ramdas, Delano. (2022). Using Convolution Neural Networks to Predict the Performance of Footballers in the Fantasy Premier League.](https://www.researchgate.net/publication/360009648_Using_Convolution_Neural_Networks_to_Predict_the_Performance_of_Footballers_in_the_Fantasy_Premier_League)
