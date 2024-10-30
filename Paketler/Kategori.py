import pandas as pd
import Paketler.Dosyalar as dosya

filmler = pd.read_csv(dosya.filmlerCSV, usecols=["movieId","genres"])

kategoriler = filmler["genres"].apply(lambda x: x.split("|"))

def KategorilerinPopülerleri(kurallar, kategori, antecedent):
    KategoriFilmleri = filmler[kategoriler.apply(lambda x: x.__contains__(kategori))]["movieId"].apply(lambda x: set([str(x)]))

    if antecedent == True:
        kurallar["antecedents_len"] = kurallar["antecedents"].apply(lambda x: len(x))
        kurallar = kurallar[kurallar['antecedents_len'] == 1]
        kurallar = kurallar[kurallar["antecedents"].isin(KategoriFilmleri)]
        kurallar = kurallar.sort_values(by='antecedent support',ascending=False)
        kurallar["antecedents"] = kurallar["antecedents"].apply(lambda x: str(x))
        kurallar = kurallar["antecedents"].drop_duplicates()
    else:
        kurallar["consequents_len"] = kurallar["consequents"].apply(lambda x: len(x))
        kurallar = kurallar[kurallar['consequents_len'] == 1]
        kurallar = kurallar[kurallar["consequents"].isin(KategoriFilmleri)]
        kurallar = kurallar.sort_values(by='lift',ascending=False)
        kurallar["consequents"] = kurallar["consequents"].apply(lambda x: str(x))
        kurallar = kurallar["consequents"].drop_duplicates()
    return kurallar