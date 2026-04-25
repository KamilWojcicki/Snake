# 🐍 Gra Snake w Pythonie (Moduł Turtle)

Prosta implementacja klasycznej gry "Snake" (Wąż) napisana w języku Python z wykorzystaniem wbudowanej biblioteki `turtle`. Projekt idealny na zaliczenie zajęć z podstaw programowania.

## 🚀 Wymagania i Uruchomienie

Aby uruchomić grę, potrzebujesz zainstalowanego [Pythona](https://www.python.org/) w wersji 3.x. Gra korzysta wyłącznie z wbudowanych modułów, więc nie wymaga instalowania żadnych zewnętrznych bibliotek.

1. Pobierz plik `snake.py` na swój komputer.
2. Otwórz terminal / wiersz poleceń w folderze z plikiem.
3. Uruchom grę wpisując:
   ```bash
   python snake.py


Opis:

# Sekcja Początkowa: Narzędzia i ustawienia
* import ...: Na samym początku sprowadzamy do programu trzy "skrzynki z narzędziami". turtle posłuży nam do rysowania grafiki, time do kontrolowania prędkości gry, a random do losowania pozycji jedzenia.
* Zmienne początkowe: opoznienie = 0.1 to pauza między każdą "klatką" gry. Dzięki temu wąż porusza się w tempie, które pozwala graczowi zareagować (inaczej latałby z prędkością światła).
 
## 🖥️ Krok 1: Przygotowanie planszy
* Tworzymy okno gry (okno), nadajemy mu czarne tło i rozmiar 600x600 pikseli.
* okno.tracer(0): To bardzo ważna funkcja! Wyłącza ona pokazywanie żmudnego procesu rysowania figur przez system. Dzięki temu gra nie pokazuje, jak kwadracik powoli przesuwa się po ekranie, tylko "teleportuje" go na nowe miejsce, tworząc złudzenie płynnego skoku na kolejną kratkę.
  
## 🐍 Krok 2 i 3: Aktorzy (Wąż i Jedzenie)
* Głowa: Tworzymy obiekt (tzw. "żółwia"), nadajemy mu kształt kwadratu, kolor zielony i ustawiamy na samym środku ekranu – czyli na współrzędnych X=0, Y=0. Podnosimy też pisak (penup()), żeby wąż nie zostawiał za sobą kreski jak flamaster. Nadajemy mu początkowy stan: kierunek = "stop", więc wąż czeka na ruch gracza.
* Jedzenie: Robimy dokładnie to samo, co przy głowie, ale zmieniamy kształt na kółko, kolor na czerwony i przesuwamy nieco wyżej (X=0, Y=100), żeby wąż nie zjadł go od razu na starcie.
* cialo = []: To jest serce mechaniki wzrostu. Tworzymy pustą listę (taki "worek"), do której będziemy wrzucać kolejne kwadraciki, gdy wąż zje jabłko.
  
## 🕹️ Krok 4: System poruszania się
* Funkcje zmiany kierunku: Napisałeś cztery małe funkcje (w_gore, w_dol, itd.). Zauważ, że mają one wbudowane zabezpieczenie – wąż idący w górę nie może nagle pójść w dół (nie może wejść sam w siebie). Zmieniają one tylko "stan umysłu" węża (czyli zmienną kierunek).
* Funkcja ruch(): To tutaj dzieje się fizyczne przesunięcie. Program sprawdza, w jakim kierunku patrzy głowa. Jeśli w górę, bierze jej obecną pozycję Y, dodaje do niej 20 pikseli (tyle szerokości ma nasz kwadrat) i ustawia głowę w nowym miejscu.
  
## ⌨️ Krok 5: Klawiatura
* okno.listen() każe programowi nadstawić uszu na to, co robisz na klawiaturze. Przypisujemy strzałki na klawiaturze ("Up", "Down" itd.) do funkcji z Kroku 4. Zatem wciśnięcie strzałki w górę wywołuje funkcję w_gore.
  
## 🔄 Krok 6: Główna pętla gry (Silnik)
To jest kod zamknięty w while True:. Kręci się on w kółko bez przerwy aż do wyłączenia programu. To tutaj tętni życie gry.
1. Odświeżenie ekranu (okno.update()): Ponieważ na początku wyłączyliśmy automatyczne odświeżanie (tracer(0)), teraz musimy ręcznie co ułamek sekundy mówić systemowi: "pokaż graczowi, co narysowałem".
2. Śmierć od ściany: Program sprawdza, czy pozycja X lub Y głowy węża przekroczyła 290 lub -290 pikseli (czyli krawędzie okna). Jeśli tak, gra się resetuje: wąż wraca na środek, kierunek to "stop", a wszystkie segmenty jego ciała są "teleportowane" daleko poza ekran (1000, 1000) i usuwane z listy cialo.
3. Zjedzenie jabłka (Inteligentne): Program mierzy odległość głowy od jedzenia. Jeśli wynosi mniej niż 20 pikseli (nachodzą na siebie):
    * Wchodzi w pętlę losowania nowego miejsca (while not dobre_miejsce).
    * Losuje punkty, ale za każdym razem sprawdza, czy to wylosowane miejsce nie leży dokładnie na głowie albo na którymś z kwadracików tworzących ogon.
    * Gdy znajdzie bezpieczne miejsce, przenosi tam jabłko.
    * Tworzy nowy, jasnozielony kwadrat i wrzuca go do "worka" (listy cialo).
4. Poruszanie ogonem: To bardzo sprytny mechanizm. Zamiast kazać każdemu segmentowi osobno "myśleć" gdzie ma iść, robimy tak: pętla idzie od końca ogona i każdy kwadracik przesuwa się na miejsce kwadracika, który był tuż przed nim. Pierwszy segment tuż za głową idzie na miejsce głowy.
5. Wykonanie kroku głowy: Odpalamy funkcję ruch(), która przesuwa samą głowę na nowe pole.
6. Śmierć od własnego ogona: Program przegląda listę cialo i sprawdza, czy którykolwiek z segmentów dotyka głowy. Jeśli tak – następuje reset gry (podobnie jak przy zderzeniu ze ścianą).
7. Pauza (time.sleep(opoznienie)): Pętla czeka ułamek sekundy (0.1s), zanim zacznie całą procedurę od nowa.
Na samym końcu okno.mainloop() utrzymuje okno otwarte, żeby po skończonej grze po prostu nie zniknęło.
