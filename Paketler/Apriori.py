import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

kurallarCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/kurallar.csv"

def FrozenSettenSeriye(data):
    data = data.replace("frozenset({","")
    data = data.replace("})","")
    data = data.replace("'","")
    data = data.replace(" ","")
    data = data.split(",")
    data = set(data)
    return data

def SıkFilmlerAğacıOluştur(dataSet):
    kullanıcılar = dataSet.groupby(['userId'], as_index=False).agg({'movieId': lambda x: ','.join(map(str,x))})['movieId'].str.split(",")

    te = TransactionEncoder()
    te_dizi = te.fit(kullanıcılar).transform(kullanıcılar)
    matris = pd.DataFrame(te_dizi, columns= te.columns_)

    sık_filmler = fpgrowth(matris, min_support=0.1, use_colnames= True)
    return sık_filmler

def KuralYarat_Kaydet(dosyaYolu, sıkData):
    kurallar = association_rules(sıkData, metric='lift', min_threshold=1.1)
    kurallar.to_csv(dosyaYolu, index=False)

def KurallarıOku(dosyaYolu):
    kurallar = pd.read_csv(dosyaYolu)

    kurallar['antecedents'] = kurallar['antecedents'].map(lambda x: FrozenSettenSeriye(x))
    kurallar['consequents'] = kurallar['consequents'].map(lambda x: FrozenSettenSeriye(x))

    return kurallar

def KuralYarat_KısaYol():
    değerlendirmelerCSV = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/değerlendirmeler.csv"
    değerlendirmeler = pd.read_csv(değerlendirmelerCSV, usecols=["userId","movieId"])

    KuralYarat_Kaydet(kurallarCSV,SıkFilmlerAğacıOluştur(değerlendirmeler))

def KuralFiltreleriOluştur(kurallar, zhangs):
    kurallar["consequents_len"] = kurallar["consequents"].apply(lambda x: len(x))
    kurallar = kurallar[(kurallar['consequents_len'] == 1) & (kurallar['zhangs_metric'] > zhangs)
    ].sort_values(by='lift',ascending=False).head(10)
    return kurallar
