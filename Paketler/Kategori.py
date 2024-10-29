import pandas as pd

filmlerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"
filmler = pd.read_csv(filmlerCSV, usecols=["movieId","genres"])

kategoriler = filmler["genres"].apply(lambda x: x.split("|"))

def KategorilerinPopülerleri(kurallar, kategori):
    KategoriFilmleri = filmler[kategoriler.apply(lambda x: x.__contains__(kategori))]["movieId"].apply(lambda x: set([str(x)]))
    kurallar["antecedents_len"] = kurallar["antecedents"].apply(lambda x: len(x))
    kurallar = kurallar[kurallar['antecedents_len'] == 1]
    kurallar = kurallar.loc[:,["antecedents","antecedent support"]]
    kurallar = kurallar[kurallar["antecedents"].isin(KategoriFilmleri)]
    kurallar = kurallar.sort_values(by='antecedent support',ascending=False)["antecedents"].apply(lambda x: str(x)).drop_duplicates()
    return kurallar