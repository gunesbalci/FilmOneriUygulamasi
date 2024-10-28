import pandas as pd

normalizeEdilecekFilmler = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/veriler/movie.csv"
normalizeEdilmişFilmler = "C:/Users/gunes/Desktop/odevprogramlama/yazılımgeliştirme/filmönermeuygulaması/HazırVeriler/filmler.csv"

filmler = pd.read_csv(normalizeEdilecekFilmler)

kategoriler = ["Documentary", "Film-Noir", "Fantasy", "War", "Children", "Horror", "Crime", "Sci-Fi", "Mystery", "Thriller"]

i = 0

for film in filmler['genres']:
    
    dahil = False
    for kategori in kategoriler:
        if kategori in film:
            dahil = True
            break
    
    if not dahil:
        filmler = filmler.drop(i)
    i += 1


filmler = filmler.drop_duplicates()
filmler = filmler.dropna()
filmler.to_csv(normalizeEdilmişFilmler,index=False)
