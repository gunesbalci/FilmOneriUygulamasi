import pandas as pd
import Paketler.Kategori as kat
import Paketler.Apriori as ap

def Iddenİsme_Çoğul(idler):
    filmlerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"
    filmler = pd.read_csv(filmlerCSV, usecols=["movieId","title"])
    
    idler = idler.apply(lambda x: int(str(x).replace("{","").replace("}","").replace("'","")))
    idler = idler.rename("id")
    idlerDF = pd.DataFrame(idler)
    idlerDF.set_index("id", inplace=True)

    isimler = filmler[filmler["movieId"].isin(idler)]

    isimler.set_index("movieId", inplace=True)
    isimler = isimler.reindex(idlerDF.index)
    isimler.reset_index(inplace=True)
    isimler = isimler["title"]

    return isimler

def Iddenİsme_Tekil(id):
    filmlerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"
    filmler = pd.read_csv(filmlerCSV, usecols=["movieId","title"])
    
    isim = filmler[filmler["movieId"].apply(lambda x: str(x).__eq__(id))]
    return isim

def BirKur_İsim(id, kurallar): #birliktelik
    kurallar = kurallar[kurallar['antecedents'] == {id}]
    kurallar = ap.KuralFiltreleriOluştur(kurallar, 0.5)
    öneriler = Iddenİsme_Çoğul(kurallar["consequents"])
    return öneriler

def BirKur_Tür(kategori, kurallar):
    filmler = kat.KategorilerinPopülerleri(kurallar, kategori)
    öneriler = Iddenİsme_Çoğul(filmler)
    return öneriler