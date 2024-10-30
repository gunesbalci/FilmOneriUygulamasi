import pandas as pd
import Paketler.Kategori as kat
import Paketler.Apriori as ap
import Paketler.Dosyalar as dosya

def Iddenİsme_Çoğul(idler):
    filmler = pd.read_csv(dosya.filmlerCSV, usecols=["movieId","title"])
    
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
    filmler = pd.read_csv(dosya.filmlerCSV, usecols=["movieId","title"])
    
    isim = filmler[filmler["movieId"].apply(lambda x: str(x).__eq__(id))]
    return isim

def SetDahil(kullanıcıFilmleri, FilmIDSet):
    dahil = True
    FilmIDSet = FilmIDSet.split()
    for film in FilmIDSet:
        if not kullanıcıFilmleri.__contains__(film):
            dahil = False
    return dahil

def BirKur_İsim(id, kurallar): #birliktelik
    kurallar = kurallar[kurallar['antecedents'] == {id}]
    kurallar = ap.KuralFiltreleriOluştur(kurallar, 0.5)
    öneriler = Iddenİsme_Çoğul(kurallar["consequents"])
    return öneriler

def BirKur_Tür(kategori, kurallar):
    filmler = kat.KategorilerinPopülerleri(kurallar, kategori, True)
    öneriler = Iddenİsme_Çoğul(filmler)
    return öneriler

def Kişisel_Tür(kullanıcı, kurallar, kategori):
    kullanıcılar = pd.read_csv(dosya.kullanıcılarCSV)
    kullanıcınınFilmleri = kullanıcılar["movieId"].iloc[kullanıcı-1]

    kurallar['antecedents'] = [str(i).replace("{","").replace("}","").replace(" ","").replace("'","") for i in kurallar['antecedents']]
    kurallar = kurallar[kurallar['antecedents'].apply(lambda x: SetDahil(kullanıcınınFilmleri, x))]
    filmler = kat.KategorilerinPopülerleri(kurallar, kategori, False)
    dönüştürülmüşFilmler = filmler.apply(lambda x: str(x).replace("{","").replace("}","").replace("'",""))
    filmler = filmler[~(dönüştürülmüşFilmler.apply(lambda x: SetDahil(kullanıcınınFilmleri, x)))]
    öneriler = Iddenİsme_Çoğul(filmler)
    return öneriler