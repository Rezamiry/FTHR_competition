import pandas as pd

print("starting...")

df = pd.read_parquet("./trots_2013-2022.parquet")
df.sort_values(['RaceStartTime', "RaceID"], inplace=True)
df.reset_index(inplace=True, drop=True)

df['FinishPosition'] = df['FinishPosition'].str.strip()
df['FinishedFirstSeven'] = df['FinishPosition'].isin(['1','2','3','4','5','6','7'])
df['FinishedBS'] = df['FinishPosition'] == "BS"
df['FinishedPU'] = df['FinishPosition'] == "PU"
df['FinishedFL'] = df['FinishPosition'] == "FL"
df['FinishedNP'] = df['FinishPosition'] == "NP"
df['FinishedUN'] = df['FinishPosition'] == "UN"
df['FinishedDQ'] = df['FinishPosition'] == "DQ"
df['FinishedWC'] = df['FinishPosition'] == "WC"
df['FinishedUR'] = df['FinishPosition'] == "NP"



# horse
df['h_count_race'] = 0
df['h_count_first'] = 0
df['h_count_first_7'] = 0
df['h_count_finish_BS'] = 0
df['h_count_finish_PU'] = 0
df['h_count_finish_FL'] = 0
df['h_count_finish_NP'] = 0
df['h_count_finish_UN'] = 0
df['h_count_finish_DQ'] = 0
df['h_count_finish_WC'] = 0
df['h_count_finish_UR'] = 0
df['h_count_disqualified'] = 0
df['h_count_no_front_cover_0'] = 0
df['h_count_no_front_cover_1'] = 0
 
df['h_average_finish_position'] = 0
df['h_average_beaten_margin'] = 0
df['h_average_pir_position'] = 0
df['h_average_price_sp'] = 0
df['h_average_position_in_running'] = 0
df['h_average_wide_off_rail'] = 0

df['h_total_money_won'] = 0

df['h_won_previous_match'] = 0
df['h_first_seven_in_three_previous_matches'] = 0


# jockey
df['j_count_race'] = 0
df['j_count_first'] = 0
df['j_count_first_7'] = 0
df['j_count_finish_BS'] = 0
df['j_count_finish_PU'] = 0
df['j_count_finish_FL'] = 0
df['j_count_finish_NP'] = 0
df['j_count_finish_UN'] = 0
df['j_count_finish_DQ'] = 0
df['j_count_finish_WC'] = 0
df['j_count_finish_UR'] = 0
df['j_count_disqualified'] = 0
df['j_count_no_front_cover_0'] = 0
df['j_count_no_front_cover_1'] = 0
 
df['j_average_finish_position'] = 0
df['j_average_beaten_margin'] = 0
df['j_average_pir_position'] = 0
df['j_average_price_sp'] = 0
df['j_average_position_in_running'] = 0
df['j_average_wide_off_rail'] = 0

df['j_total_money_won'] = 0

df['j_won_previous_match'] = 0
df['j_first_seven_in_three_previous_matches'] = 0

# trainer
df['t_count_race'] = 0
df['t_count_first'] = 0
df['t_count_first_7'] = 0
df['t_count_finish_BS'] = 0
df['t_count_finish_PU'] = 0
df['t_count_finish_FL'] = 0
df['t_count_finish_NP'] = 0
df['t_count_finish_UN'] = 0
df['t_count_finish_DQ'] = 0
df['t_count_finish_WC'] = 0
df['t_count_finish_UR'] = 0
df['t_count_disqualified'] = 0
df['t_count_no_front_cover_0'] = 0
df['t_count_no_front_cover_1'] = 0
 
df['t_average_finish_position'] = 0
df['t_average_beaten_margin'] = 0
df['t_average_pir_position'] = 0
df['t_average_price_sp'] = 0
df['t_average_position_in_running'] = 0
df['t_average_wide_off_rail'] = 0

df['t_total_money_won'] = 0

df['t_won_previous_match'] = 0
df['t_first_seven_in_three_previous_matches'] = 0

# horse jockey combination
df['hj_count_race'] = 0
df['hj_count_first'] = 0
df['hj_count_first_7'] = 0
df['hj_total_money_won'] = 0

# horse trainer combination
df['ht_count_race'] = 0
df['ht_count_first'] = 0
df['ht_count_first_7'] = 0
df['ht_total_money_won'] = 0


# jockey trainer combination
df['jt_count_race'] = 0
df['jt_count_first'] = 0
df['jt_count_first_7'] = 0
df['jt_total_money_won'] = 0

# horse jockey trainer combination
df['hjt_count_race'] = 0
df['hjt_count_first'] = 0
df['hjt_count_first_7'] = 0
df['hjt_total_money_won'] = 0



print("starting the loop ... ")

for index, row in df.iterrows():
    if index % 10000 == 0:
        print(index)
    # horse
    prev_df = df.iloc[:index]
    t = prev_df[prev_df['HorseID'] == row['HorseID']]
    if t.shape[0] > 0:
        df.loc[index, 'h_count_race'] = t.shape[0]
        df.loc[index, 'h_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'h_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'h_count_finish_BS'] = sum(t['FinishedBS'])
        df.loc[index, 'h_count_finish_PU'] = sum(t['FinishedPU'])
        df.loc[index, 'h_count_finish_FL'] = sum(t['FinishedFL'])
        df.loc[index, 'h_count_finish_NP'] = sum(t['FinishedNP'])
        df.loc[index, 'h_count_finish_UN'] = sum(t['FinishedUN'])
        df.loc[index, 'h_count_finish_DQ'] = sum(t['FinishedDQ'])
        df.loc[index, 'h_count_finish_WC'] = sum(t['FinishedWC'])
        df.loc[index, 'h_count_finish_UR'] = sum(t['FinishedUR'])
        df.loc[index, 'h_count_disqualified'] = sum(t['Disqualified'])
        df.loc[index, 'h_count_no_front_cover_0'] = sum(t['NoFrontCover'] == 0)
        df.loc[index, 'h_count_no_front_cover_1'] = sum(t['NoFrontCover'] == 1)
        
        df.loc[index, 'h_average_finish_position'] = t['FinishPosition'][t['FinishPosition'].isin(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'])].astype(int).mean()
        df.loc[index, 'h_average_beaten_margin'] = t['BeatenMargin'][t['BeatenMargin'] != 999].mean()
        df.loc[index, 'h_average_pir_position'] = t['PIRPosition'].mean()
        df.loc[index, 'h_average_price_sp'] = t['PriceSP'].mean()
        df.loc[index, 'h_average_position_in_running'] = t['PositionInRunning'][t['PositionInRunning']!=-9].mean()
        df.loc[index, 'h_average_wide_off_rail'] = t['WideOffRail'][t['WideOffRail']!=-9].mean()

        df.loc[index, 'h_total_money_won'] = t['Prizemoney'].sum()

        df.loc[index, 'h_won_previous_match'] = t.iloc[-1]['FinishPosition'] == "1"
        df.loc[index, 'h_first_seven_in_three_previous_matches'] = sum(t.iloc[-3:]['FinishedFirstSeven'])>0



    # jockey
    t = prev_df[prev_df['JockeyID'] == row['JockeyID']]
    if t.shape[0] > 0:
        df.loc[index, 'j_count_race'] = t.shape[0]
        df.loc[index, 'j_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'j_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'j_count_finish_BS'] = sum(t['FinishedBS'])
        df.loc[index, 'j_count_finish_PU'] = sum(t['FinishedPU'])
        df.loc[index, 'j_count_finish_FL'] = sum(t['FinishedFL'])
        df.loc[index, 'j_count_finish_NP'] = sum(t['FinishedNP'])
        df.loc[index, 'j_count_finish_UN'] = sum(t['FinishedUN'])
        df.loc[index, 'j_count_finish_DQ'] = sum(t['FinishedDQ'])
        df.loc[index, 'j_count_finish_WC'] = sum(t['FinishedWC'])
        df.loc[index, 'j_count_finish_UR'] = sum(t['FinishedUR'])
        df.loc[index, 'j_count_disqualified'] = sum(t['Disqualified'])
        df.loc[index, 'j_count_no_front_cover_0'] = sum(t['NoFrontCover'] == 0)
        df.loc[index, 'j_count_no_front_cover_1'] = sum(t['NoFrontCover'] == 1)
        
        df.loc[index, 'j_average_finish_position'] = t['FinishPosition'][t['FinishPosition'].isin(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'])].astype(int).mean()
        df.loc[index, 'j_average_beaten_margin'] = t['BeatenMargin'][t['BeatenMargin'] != 999].mean()
        df.loc[index, 'j_average_pir_position'] = t['PIRPosition'].mean()
        df.loc[index, 'j_average_price_sp'] = t['PriceSP'].mean()
        df.loc[index, 'j_average_position_in_running'] = t['PositionInRunning'][t['PositionInRunning']!=-9].mean()
        df.loc[index, 'j_average_wide_off_rail'] = t['WideOffRail'][t['WideOffRail']!=-9].mean()

        df.loc[index, 'j_total_money_won'] = t['Prizemoney'].sum()

        df.loc[index, 'j_won_previous_match'] = t.iloc[-1]['FinishPosition'] == "1"
        df.loc[index, 'j_first_seven_in_three_previous_matches'] = sum(t.iloc[-3:]['FinishedFirstSeven'])>0



    # trainer
    t = prev_df[prev_df['TrainerID'] == row['TrainerID']]
    if t.shape[0] > 0:
        df.loc[index, 't_count_race'] = t.shape[0]
        df.loc[index, 't_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 't_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 't_count_finish_BS'] = sum(t['FinishedBS'])
        df.loc[index, 't_count_finish_PU'] = sum(t['FinishedPU'])
        df.loc[index, 't_count_finish_FL'] = sum(t['FinishedFL'])
        df.loc[index, 't_count_finish_NP'] = sum(t['FinishedNP'])
        df.loc[index, 't_count_finish_UN'] = sum(t['FinishedUN'])
        df.loc[index, 't_count_finish_DQ'] = sum(t['FinishedDQ'])
        df.loc[index, 't_count_finish_WC'] = sum(t['FinishedWC'])
        df.loc[index, 't_count_finish_UR'] = sum(t['FinishedUR'])
        df.loc[index, 't_count_disqualified'] = sum(t['Disqualified'])
        df.loc[index, 't_count_no_front_cover_0'] = sum(t['NoFrontCover'] == 0)
        df.loc[index, 't_count_no_front_cover_1'] = sum(t['NoFrontCover'] == 1)
        
        df.loc[index, 't_average_finish_position'] = t['FinishPosition'][t['FinishPosition'].isin(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'])].astype(int).mean()
        df.loc[index, 't_average_beaten_margin'] = t['BeatenMargin'][t['BeatenMargin'] != 999].mean()
        df.loc[index, 't_average_pir_position'] = t['PIRPosition'].mean()
        df.loc[index, 't_average_price_sp'] = t['PriceSP'].mean()
        df.loc[index, 't_average_position_in_running'] = t['PositionInRunning'][t['PositionInRunning']!=-9].mean()
        df.loc[index, 't_average_wide_off_rail'] = t['WideOffRail'][t['WideOffRail']!=-9].mean()
        
        df.loc[index, 't_total_money_won'] = t['Prizemoney'].sum()

        df.loc[index, 't_won_previous_match'] = t.iloc[-1]['FinishPosition'] == "1"
        df.loc[index, 't_first_seven_in_three_previous_matches'] = sum(t.iloc[-3:]['FinishedFirstSeven'])>0



    # horse jockey
    t = prev_df[(prev_df['HorseID'] == row['HorseID']) & (prev_df['JockeyID'] == row['JockeyID'])]
    if t.shape[0] > 0:
        df.loc[index, 'hj_count_race'] = t.shape[0]
        df.loc[index, 'hj_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'hj_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'hj_total_money_won'] = t['Prizemoney'].sum()

    # horse trainer
    t = prev_df[(prev_df['HorseID'] == row['HorseID']) & (prev_df['TrainerID'] == row['TrainerID'])]
    if t.shape[0] > 0:
        df.loc[index, 'ht_count_race'] = t.shape[0]
        df.loc[index, 'ht_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'ht_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'ht_total_money_won'] = t['Prizemoney'].sum()

    # jockey trainer
    t = prev_df[(prev_df['JockeyID'] == row['JockeyID']) & (prev_df['TrainerID'] == row['TrainerID'])]
    if t.shape[0] > 0:
        df.loc[index, 'jt_count_race'] = t.shape[0]
        df.loc[index, 'jt_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'jt_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'jt_total_money_won'] = t['Prizemoney'].sum()

    # horse jockey trainer
    t = prev_df[(prev_df['HorseID'] == row['HorseID']) & (prev_df['JockeyID'] == row['JockeyID']) & (prev_df['TrainerID'] == row['TrainerID'])]
    if t.shape[0] > 0:
        df.loc[index, 'hjt_count_race'] = t.shape[0]
        df.loc[index, 'hjt_count_first'] = sum(t['FinishPosition'] == "1")
        df.loc[index, 'hjt_count_first_7'] = sum(t['FinishedFirstSeven'])
        df.loc[index, 'hjt_total_money_won'] = t['Prizemoney'].sum()


    

df.fillna(0, inplace=True)

print("start saving")
df.to_pickle("./df_hist.pkl")