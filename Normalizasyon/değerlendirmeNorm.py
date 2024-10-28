import pandas as pd

normalizeEdilecekDeğerlendirmeler = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/veriler/rating.csv"
normalizeEdilmişDeğerlendirmeler = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/değerlendirmeler.csv"
filmler = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"

değerlendirmeler = pd.read_csv(normalizeEdilecekDeğerlendirmeler,usecols=["userId","movieId","rating"])
filmIDleri = pd.read_csv(filmler, usecols=["movieId"]).squeeze()
filmSeri = pd.Series(filmIDleri)

kaydedilecek = değerlendirmeler[değerlendirmeler["movieId"].isin(filmSeri)]
kaydedilecek = kaydedilecek.drop_duplicates()
kaydedilecek = kaydedilecek.dropna()
kaydedilecek.to_csv(normalizeEdilmişDeğerlendirmeler, index=False)






