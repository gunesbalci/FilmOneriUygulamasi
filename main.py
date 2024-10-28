import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import Paketler.Apriori as ap

kurallar = ap.KurallarıOku(ap.kurallarCSV)
kurallar = ap.KuralFiltreleriOluştur(kurallar)
print(len(kurallar))
