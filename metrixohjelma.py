import urllib.request
from bs4 import BeautifulSoup
import ssl
import traceback

def getcompensation(url, tulos, rating, tulos_paarista=True):
    try:
        tulos = int(tulos)
        rating = int(rating)
        context = ssl._create_unverified_context()
        html_page = urllib.request.urlopen(url, context=context).read()
        soup = BeautifulSoup(html_page, features="html.parser")
        table = soup.find_all("table", {"class": "score-table"})
        if table:
            table = table[0]
        else:
            return {"error":"joku meni vituiks"}
        values = table.find_all("td")
        if tulos_paarista:
            par = table.find_all("td", {"class": "center birdie"})
            par_score = int(par[0].find_all(text=True)[0])
            tulos = tulos + par_score
        score_lista = []
        rating_lista = []
        for i in range(len(values)):
            val = values[i].find_all(text=True)
            if i % 2 == 0:
                score_lista.append(int(val[0]))
            else:
                rating_lista.append(int(val[0]))
        score_lista.sort(reverse=True)
        rating_lista.sort()
        lowest = 999
        kiepin_rating = 0
        for i in range(len(rating_lista)):
            if rating >= rating_lista[i]:
                lowest = score_lista[i]
            if tulos == score_lista[i]:
                kiepin_rating = rating_lista[i]
        erotus = tulos-lowest

        return {"round_rating":str(kiepin_rating), "suhteutettu":str(erotus)}
    except:
        return {"error": traceback.format_exc()}
