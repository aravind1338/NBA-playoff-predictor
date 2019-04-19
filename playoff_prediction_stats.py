from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

seasons = ["OKC_POR", "GSW_LAC", "HOU_UTA", "DEN_SAS", "MIL_DET", "TOR_ORL", "PHI_BKN", "IND_BOS", "MIL_BOS", "TOR_PHI", "GSW_HOU", "DEN_OKC", "MIL_PHI", "GSW_OKC", "MIL_GSW"]

pages = ["https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=OKC&opp_id=POR&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=GSW&opp_id=LAC&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=HOU&opp_id=UTA&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=DEN&opp_id=SAS&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=MIL&opp_id=DET&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=TOR&opp_id=ORL&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=PHI&opp_id=NJN&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=IND&opp_id=BOS&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=MIL&opp_id=BOS&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=TOR&opp_id=PHI&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=GSW&opp_id=HOU&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=DEN&opp_id=OKC&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=MIL&opp_id=PHI&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=GSW&opp_id=OKC&c1stat=ast&c1comp=gt&c1val=0&order_by=pts", "https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&match=game&lg_id=NBA&is_playoffs=N&team_seed_cmp=eq&opp_seed_cmp=eq&year_min=2014&year_max=2019&is_range=N&game_num_type=team&team_id=MIL&opp_id=GSW&c1stat=ast&c1comp=gt&c1val=0&order_by=pts"]

for i in range(0, 15):
	# For each playoff matchup, collect relevant data

	quote_page = pages[i]
	page = urlopen(quote_page)

	soup = BeautifulSoup(page, 'html.parser')
	#soup now contains the html of the page

	# POINTS #

	points_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"pts"})
	points_for = [points_for.text.strip() for points_for in points_for_box]

	points_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_pts"})
	points_against = [points_against.text.strip() for points_against in points_against_box]

	point_diff = [float(x) - float(y) for x, y in zip(points_for, points_against)]

	# ASSISTS #

	assists_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"ast"})
	assists_for = [assists_for.text.strip() for assists_for in assists_for_box]

	assists_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_ast"})
	assists_against = [assists_against.text.strip() for assists_against in assists_against_box]

	assist_diff = [float(x) - float(y) for x, y in zip(assists_for, assists_against)]

	# STEALS #

	steals_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"stl"})
	steals_for = [steals_for.text.strip() for steals_for in steals_for_box]

	steals_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_stl"})
	steals_against = [steals_against.text.strip() for steals_against in steals_against_box]

	steal_diff = [float(x) - float(y) for x, y in zip(steals_for, steals_against)]

	# BLOCKS #

	blocks_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"blk"})
	blocks_for = [blocks_for.text.strip() for blocks_for in blocks_for_box]

	if seasons[i] == "DEN_SAS":
		blocks_for.insert(12, '0')
	elif seasons[i] == "PHI_BKN":
		blocks_for.insert(18, '0')
	elif seasons[i] == "IND_BOS":
		blocks_for.insert(2, '0')
	elif seasons[i] == "TOR_PHI":
		blocks_for.insert(8, '0')

	blocks_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_blk"})
	blocks_against = [blocks_against.text.strip() for blocks_against in blocks_against_box]
	
	if seasons[i] == "GSW_LAC":
		blocks_against.insert(7, '0')
	elif seasons[i] == "MIL_DET":
		blocks_against.insert(10, '0')
		blocks_against.insert(22, '0')
	elif seasons[i] == "GSW_HOU":
		blocks_against.insert(18, '0')
	elif seasons[i] == "DEN_OKC":
		blocks_against.insert(10, '0')

	block_diff = [float(x) - float(y) for x, y in zip(blocks_for, blocks_against)]

	# TURNOVERS #

	tov_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"tov"})
	tov_for = [tov_for.text.strip() for tov_for in tov_for_box]

	tov_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_tov"})
	tov_against = [tov_against.text.strip() for tov_against in tov_against_box]

	tov_diff = [float(x) - float(y) for x, y in zip(tov_for, tov_against)]

	# FG% #

	fgpct_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"fg_pct"})
	fgpct_for = [fgpct_for.text.strip() for fgpct_for in fgpct_for_box]

	fgpct_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_fg_pct"})
	fgpct_against = [fgpct_against.text.strip() for fgpct_against in fgpct_against_box]

	fgpct_diff = [float(x) - float(y) for x, y in zip(fgpct_for, fgpct_against)]

	# 3PT% #
	fg3pct_for_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"fg3_pct"})
	fg3pct_for = [fg3pct_for.text.strip() for fg3pct_for in fg3pct_for_box]

	fg3pct_against_box = soup.find_all('td', attrs={"class":"right ", "data-stat":"opp_fg3_pct"})
	fg3pct_against = [fg3pct_against.text.strip() for fg3pct_against in fg3pct_against_box]

	fg3pct_diff = [float(x) - float(y) for x, y in zip(fg3pct_for, fg3pct_against)]


	length = len(point_diff)
	data = [(point_diff[j], assist_diff[j], steal_diff[j], block_diff[j], tov_diff[j], fgpct_diff[j], fg3pct_diff[j]) for j in range(0, length)]

	## Create CSV files with the differential categories as columns
	file_name = seasons[i]
	with open(file_name, 'a') as csv_file:
	 	writer = csv.writer(csv_file)
	 	writer.writerow(["pts_diff", "ast_diff", "stl_diff", "blk_diff%", "tov_diff", "fg_diff", "fg3_diff"])
	 	for pts, ast, stl, blk, tov, fg, fg3 in data:
	 		writer.writerow([pts, ast, stl, blk, tov, fg, fg3])