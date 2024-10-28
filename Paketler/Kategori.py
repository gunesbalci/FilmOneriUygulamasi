import pandas as pd

filmlerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"
filmler = pd.read_csv(filmlerCSV, usecols=["movieId","genres"])

kategoriler = filmler["genres"].apply(lambda x: x.split("|"))

Belgesel = filmler[kategoriler.apply(lambda x: x.__contains__("Documentary"))]
Sanat = filmler[kategoriler.apply(lambda x: x.__contains__("Film-Noir"))]
Fantazi = filmler[kategoriler.apply(lambda x: x.__contains__("Fantasy"))]
Savaş = filmler[kategoriler.apply(lambda x: x.__contains__("War"))]
Çocuk = filmler[kategoriler.apply(lambda x: x.__contains__("Children"))]
Korku = filmler[kategoriler.apply(lambda x: x.__contains__("Horror"))]
Suç = filmler[kategoriler.apply(lambda x: x.__contains__("Crime"))]
BilimKurgu = filmler[kategoriler.apply(lambda x: x.__contains__("Sci-Fi"))]
Gizem = filmler[kategoriler.apply(lambda x: x.__contains__("Mystery"))]
Gerilim = filmler[kategoriler.apply(lambda x: x.__contains__("Thriller"))]