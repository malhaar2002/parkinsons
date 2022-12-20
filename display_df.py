import pandas as pd

sample_data = [[132.9588888, 446.4488196, 75.42733589, 0.028006881, 0.000211396, 0.014384277, 0.016734109,
         0.043152832, 0.194968269, 1.685448298, 0.089904364, 0.147112444, 0.207948142, 0.269713092, 10.33065404]]
sample_dataframe = pd.DataFrame(sample_data, columns=[
    "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter( % )", "MDVP:Jitter(Abs)", "MDVP:RAP",
    "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "HNR"
])

parkinsons_data = pd.read_csv("parkinsons.csv")
parkinsons_data.drop(columns=['name', 'spread1', 'spread2', 'PPE', 'RPDE', 'D2', 'NHR', 'DFA'], axis=1, inplace = True)
parkinsons_grouped = parkinsons_data.groupby('status').mean()