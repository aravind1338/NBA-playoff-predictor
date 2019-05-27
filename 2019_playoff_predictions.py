import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

currentRound = 1

while (currentRound < 5):

	column = ['pts_diff', 'ast_diff', 'stl_diff', 'blk_diff', 'tov_diff', 'fg_diff', 'fg3_diff', 'game_value']
	base_path = "~/Desktop/NBA/"

	if currentRound == 1:

		print ("First round predictions:")
		print ("\n")

		matchups = ["MIL_DET", "TOR_ORL", "PHI_BKN", "IND_BOS", "GSW_LAC", "DEN_SAS", "OKC_POR", "HOU_UTA"]

		game_values = [[0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0], [0, 0, 1, -1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, -1, 0, 0, 1, 1, 0, 0], [1, -1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, -1, 0, 1, -1, 0], [0, -1, 0, 0, 0, 0, 1, 1, -1, 0, 0, 0, -1, 1, 0, -1, 1, 1, -1, 0, 0, -1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, -1, 0, 0, -1, 0, -1, 0, -1, 0], [1, 0, 0, -1, 0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 1, 0, -1, 0], [0, 1, 0, 0, 0, 0, 1, 0, -1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, -1, -1]]

		results = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0]]

		regular_season_numbers = [[908, 291, 46, 155, 2, 0.036, 0.005, 19], [584, -10, 137, -8, 68, 0.02, 0.01, 16], [238, 253, 67, 93, -13, 0.022, 0.006, 9], [-359, -27, 7, -31, 70, 0.01, 0.009, -1], [208, 443, 64, 140, -24, 0.02, -0.003, 9], [-81, 232, 133, -23, 110, -0.012, -0.041, 6], [-15, 30, 220, 12, 10, -0.013, -0.011, -4], [180, -392, 37, -78, -140, -0.019, 0, 3]]

	elif currentRound == 2:

		print ("Conference Semifinal predictions:")
		print ("\n")

		matchups = ["MIL_BOS", "TOR_PHI", "GSW_HOU", "DEN_OKC"]

		game_values = [[1, 0, 0, 1, 0, -1, 1, 0, 0, 1, 1, 0, -1, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0], [-1, 1, -1, 0, 1, 1, 0, -1, 1, 1, -1, 1, -1, 0, 0, 1, 0, 0, 1, 0, 0], [-1, 0, 1, 0, 1, -1, 0, 0, 1, 0, 0, 0, -1, 1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0]]

		results = [[1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

		regular_season_numbers = [[470, -19, -91, 51, 85, 0.011, -0.012, 11], [-61, -122, 74, 5, -73, 0.003, 0.007, 7], [309, 672, -75, 120, 71, 0.042, 0.029, 4], [-312, 328, -132, -62, -43, 0.012, 0.003, 5]]

	elif currentRound == 3:

		print ("Conference Final predictions:")
		print ("\n")

		matchups = ["MIL_PHI", "GSW_OKC"]

		game_values = [[1, 1, -1, 0, 0, 0, 0, 1, 1, -1, 0, 1, 0, 0, -1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, -1, -1, 1, 0]]

		results = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0]]

		regular_season_numbers = [[241, -71, 9, 54, -86, 0.005, -0.006, 9], [263, 496, -141, 100, 24, 0.037, 0.037, 8]]

	else:
		print ("NBA Finals prediction:")
		print ("\n")

		matchups = ["MIL_GSW"]

		game_values = [[1, -1, 1, 0, 0, 0, -1, -1, -1, 0, 0, -1]]

		results = [[1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

		regular_season_numbers = [[36, -277, -10, -39, -32, -0.015, -0.032, 3]]

	i = -1
	for matchup in matchups:
		i += 1
		path = base_path + matchup
		df = pd.read_csv(path)
		df.round(4)
		df["game_value"] = pd.Series(game_values[i])
		df["result"] = pd.Series(results[i])
		
		regular_df = pd.DataFrame(np.array([regular_season_numbers[i]]), columns=column)

		playoff_feature_values = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
		playoff_target_values = df.iloc[:, [-1]]

		model = LogisticRegression()
		model.fit(playoff_feature_values, playoff_target_values)

		regular_feature_values = regular_df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
		prediction = model.predict(regular_feature_values)

		val = model.decision_function(regular_feature_values)/np.sum(regular_feature_values.values)
		probability = 1/(1+np.exp(-val))

		if currentRound == 1:

			if i == 0:
				if prediction == 1:
					print ("Milwaukee Bucks over the Detroit Pistons")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Detroit Pistons over the Milwaukee Bucks")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 1:
				if prediction == 1:
					print ("Toronto Raptors over the Orlando Magic")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Orlando Magic over the Toronto Raptors")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 2:
				if prediction == 1:
					print ("Philadelphia 76ers over the Brooklyn Nets")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Brooklyn Nets over the Philadelphia 76ers")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 3:
				if prediction == 1:
					print ("Indiana Pacers over the Boston Celtics")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Boston Celtics over the Indiana Pacers")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 4:
				if prediction == 1:
					print ("Golden State Warriors over the Los Angeles Clippers")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Los Angeles Clippers over the Golden State Warriors")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 5:
				if prediction == 1:
					print ("Denver Nuggets over the San Antonio Spurs")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("San Antonio Spurs over the Denver Nuggets")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 6:
				if prediction == 1:
					print ("Oklahoma City Thunder over the Portland Trailblazers")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Portland Trailblazers over the Oklahoma City Thunder")
					print ("confidence: ", probability[0]*100, "%")
			else:
				if prediction == 1:
					print ("Houston Rockets over the Utah Jazz")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Utah Jazz over the Houston Rockets")
					print ("confidence: ", probability[0]*100, "%")

			print ("\n")

		elif currentRound == 2:

			if i == 0:
				if prediction == 1:
					print ("Milwaukee Bucks over the Boston Celtics")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Boston Celtics over the Milwaukee Bucks")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 1:
				if prediction == 1:
					print ("Toronto Raptors over the Philadelphia 76ers")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Philadelphia 76ers over the Toronto Raptors")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 2:
				if prediction == 1:
					print ("Golden State Warriors over the Houston Rockets")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Houston Rockets over the Golden State Warriors")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 3:
				if prediction == 1:
					print ("Denver Nuggets over the Oklahoma City Thunder")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Oklahoma City Thunder over the Denver Nuggets")
					print ("confidence: ", probability[0]*100, "%")

			print ("\n")

		elif currentRound == 3:

			if i == 0:
				if prediction == 1:
					print ("Milwaukee Bucks over the Philadelphia 76ers")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Philadelphia 76ers over the Milwaukee Bucks")
					print ("confidence: ", probability[0]*100, "%")
			elif i == 1:
				if prediction == 1:
					print ("Golden State Warriors over the Oklahoma City Thunder")
					print ("confidence: ", probability[0]*100, "%")
				else:
					print ("Oklahoma City Thunder over the Golden State Warriors")
					print ("confidence: ", probability[0]*100, "%")

			print ("\n")

		else:
			if prediction == 1:
				print ("Milwaukee Bucks over the Golden State Warriors")
				print ("confidence: ", probability[0]*100, "%")
			else:
				print ("Golden State Warriors over the Milwaukee Bucks")
				print ("confidence: ", probability[0]*100, "%")

	currentRound += 1