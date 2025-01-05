Email Server Teszter - Python
Email Server Teszter egy Python alapú eszköz, amely az email-szerver teljesítményének és stabilitásának tesztelésére szolgál API, IMAP és SMTP protokollokon keresztül. A rendszer véletlenszerű email címeket generál, véletlenszerű tartalommal email-eket küld, és dinamikus tesztelési stratégiákat alkalmaz, miközben figyeli a rendszer erőforrásait, mint a CPU kihasználtság, memória és hőmérséklet.

Funkcionalitás
API a domain és email címek kezeléséhez
Lekéri a meglévő domain és email címeket egy külső API-n keresztül.
Elmenti az adatokat helyi adatbázisba vagy fájlba.
Törli a meglévő email címeket, majd generál n teszt email címet.
Tesztelési folyamat
Véletlenszerű k hosszúságú karakterláncokat generál.
Véletlenszerűen elküldi a generált karakterláncokat n/2 küldő email címről n/2 fogadó címre.
Az email küldés és fogadás végtelen ciklusban történik, tetszőleges időközönként (t).
A tesztelés IMAP és SMTP protokollokkal zajlik az email-szerver teljeskörű validálása érdekében.
Rendszermonitorozás
A tesztelés során a következő rendszerparamétereket figyeli:
CPU kihasználtság
Memória kihasználtság
CPU hőmérséklet
Az adatokat folyamatosan naplózza az elemzéshez.
Technikai részletek
Fejlesztési nyelv: Python
Használt protokollok és eszközök:
IMAP és SMTP: Az email-ek küldéséhez és fogadásához az imaplib és smtplib Python könyvtárak.
API kezelés: A requests könyvtár API hívásokhoz.
Rendszerfigyelés: A psutil könyvtár a CPU, memória és hőmérséklet monitorozásához.
Email címek generálása:
Véletlenszerű email címek generálása a domain alapján (pl. tester1@test.com, tester2@test.com).
Az email címek ideiglenes eltárolása JSON vagy SQLite adatbázisban.
Hogyan használd
Paraméterek konfigurálása:

Állítsd be a teszt email címek számát (n).
Állítsd be a generált karakterlánc hosszát (k).
Állítsd be az időközt (t) az email küldések között.
Teszt futtatása:

Az eszköz generálja az email címeket, és elkezdi a véletlenszerű email-ek küldését.
A rendszer figyeli az erőforrásokat és naplózza a teljesítmény adatokat.
Folyamatos tesztelés:

A teszt folytatódik addig, amíg manuálisan le nem állítják.
Előnyök
Automatizált Tesztelés: Időmegtakarítás az email-szerver stressz tesztelése során.
Testreszabhatóság: Paraméterezhető tesztelési beállítások.
Átfogó Elemzés: Részletes adatok az email-szerver teljesítményéről és a rendszer állapotáról.
Lehetséges jövőbeli fejlesztések
Grafikus felhasználói felület (GUI): Az egyszerűbb konfiguráció és használat érdekében.
Adatvizualizáció: A tesztelési eredmények vizualizálása (pl. CPU terhelés grafikonok).
További protokollok támogatása: Például POP3.
Követelmények
Python 3.x
Ubuntu 24.04 (Raspberry Pi 5 támogatott)
Könyvtárak: imaplib, smtplib, requests, psutil
Telepítés
Klónozd a repót:

bash
Copy code
git clone https://github.com/your-repository/email-server-tester.git
cd email-server-tester
Telepítsd a szükséges függőségeket:

bash
Copy code
pip install -r requirements.txt
Konfiguráld a tesztelési paramétereket a szükséges módon.

Futtasd a teszt szkriptet:

bash
Copy code
python email_server_tester.py
Licenc
MIT Licenc - a LICENSE fájlban található részletek szerint.

