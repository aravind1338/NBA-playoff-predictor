# NBA-playoff-predictor
Python program to predict the 2019 NBA playoffs

Using BeautifulSoup to scrape the web, pandas dataframes to store scraped data and logistic regression, the program attempts to predict the results of the 2019 NBA playoffs.

The metrics used are -- in terms of difference in totals between the two teams in question -- points, assists, steals, blocks, turnovers, fg%, 3pt% and game value. There are better metrics that can be used, but these were the easiest ones to scrape.
Game value is something I came up with to quantify a result taking into account home-court advantage : -1 for a home loss, 0 for a home win/road loss, +1 for a road win.

I scraped data from https://www.basketball-reference.com/ going back 5 years, focusing on head to head matchups between the two teams.

Run playoff_prediction_stats.py once to create CSV files and 2019_playoff_predictions.py to see the predicted results.

The results for the first round were in line with what the ESPN experts picked -- including the 6-seed Oklahoma City Thunder over the 3-seed Portland Trailblazers
