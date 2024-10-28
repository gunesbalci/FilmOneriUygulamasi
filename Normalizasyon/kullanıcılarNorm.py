import pandas as pd

değerlendirmelerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/değerlendirmeler.csv"
kullanıcılarCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/kullanıcılar.csv"

değerlendirmeler = pd.read_csv(değerlendirmelerCSV, usecols=["userId","movieId"])

kullanıcılar = değerlendirmeler.groupby(['userId'], as_index=False).agg({'movieId': lambda x: ','.join(map(str,x))})

kullanıcılar.to_csv(kullanıcılarCSV, index=False)