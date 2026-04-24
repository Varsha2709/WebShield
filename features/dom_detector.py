
from bs4 import BeautifulSoup

def detect_dom_attacks(html):

 score=0
 attack="Safe"

 if "eval(" in html:
  score+=30
  attack="XSS"

 if "document.cookie" in html:
  score+=40
  attack="Cookie Theft"

 soup=BeautifulSoup(html,"html.parser")

 if soup.find("iframe"):
  score+=20
  attack="Clickjacking"

 forms=soup.find_all("form")

 for f in forms:
  if f.find("input",{"type":"password"}):
   score+=20
   attack="Phishing Form"

 return score,attack
