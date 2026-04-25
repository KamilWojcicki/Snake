import turtle
import time
import random

# Ustawienia początkowe
opoznienie = 0.1
wynik = 0

# 1. Przygotowanie ekranu gry
okno = turtle.Screen()
okno.title("Gra Snake")
okno.bgcolor("black") # Kolor tła
okno.setup(width=600, height=600) # Wymiary okna
okno.tracer(0) # Wyłącza automatyczne odświeżanie ekranu (dla płynności)

# 2. Tworzenie głowy węża
glowa = turtle.Turtle()
glowa.speed(0)
glowa.shape("square") # Kształt: kwadrat
glowa.color("green")  # Kolor: zielony
glowa.penup()         # Podnosi "pisak", żeby wąż nie zostawiał linii
glowa.goto(0, 0)      # Start na środku ekranu (x=0, y=0)
glowa.kierunek = "stop" # Początkowy kierunek (wąż stoi w miejscu)

# 3. Tworzenie jedzenia
jedzenie = turtle.Turtle()
jedzenie.speed(0)
jedzenie.shape("circle") # Kształt: koło
jedzenie.color("red")    # Kolor: czerwony
jedzenie.penup()
jedzenie.goto(0, 100)    # Początkowa pozycja jedzenia

# Lista przechowująca segmenty ciała węża
cialo = []

# 4. Funkcje zmieniające kierunek ruchu
def w_gore():
    if glowa.kierunek != "dol": # Wąż nie może zawrócić w miejscu
        glowa.kierunek = "gora"

def w_dol():
    if glowa.kierunek != "gora":
        glowa.kierunek = "dol"

def w_lewo():
    if glowa.kierunek != "prawo":
        glowa.kierunek = "lewo"

def w_prawo():
    if glowa.kierunek != "lewo":
        glowa.kierunek = "prawo"

# Funkcja realizująca przemieszczanie
def ruch():
    if glowa.kierunek == "gora":
        y = glowa.ycor() # Pobiera obecną pozycję Y
        glowa.sety(y + 20) # Przesuwa w górę o 20 pikseli

    if glowa.kierunek == "dol":
        y = glowa.ycor()
        glowa.sety(y - 20)

    if glowa.kierunek == "lewo":
        x = glowa.xcor()
        glowa.setx(x - 20)

    if glowa.kierunek == "prawo":
        x = glowa.xcor()
        glowa.setx(x + 20)

# 5. Przypisanie klawiszy klawiatury
okno.listen() # Nasłuchiwanie wciśnięć klawiszy
okno.onkeypress(w_gore, "Up")
okno.onkeypress(w_dol, "Down")
okno.onkeypress(w_lewo, "Left")
okno.onkeypress(w_prawo, "Right")

okno.update()
# 6. Główna pętla gry (tu dzieje się cała akcja)
while True:
    okno.update() # Odświeża ekran

    # Kolizja ze ścianą (jeśli wąż wyjdzie za ekran)
    if glowa.xcor() > 290 or glowa.xcor() < -290 or glowa.ycor() > 290 or glowa.ycor() < -290:
        time.sleep(1) # Pauza na 1 sekundę
        glowa.goto(0, 0) # Powrót na środek
        glowa.kierunek = "stop" # Zatrzymanie

        # Usuwanie starego ciała węża z ekranu
        for segment in cialo:
            segment.goto(1000, 1000) # Wysyła segmenty poza ekran
        cialo.clear() # Czyści listę

    # Kolizja z jedzeniem
    if glowa.distance(jedzenie) < 20:
        # Losuje nowe miejsce, dopóki nie znajdzie pustego pola
        dobre_miejsce = False
        while not dobre_miejsce:
            # Losujemy liczby od -14 do 14 i mnożymy razy 20, 
            # żeby idealnie pasowały do "kroków" węża
            losowe_x = random.randint(-14, 14) * 20
            losowe_y = random.randint(-14, 14) * 20
            
            dobre_miejsce = True # Zakładamy z góry, że miejsce jest wolne
            
            # Sprawdzamy, czy wylosowane miejsce nie pokrywa się z głową węża
            if glowa.distance(losowe_x, losowe_y) < 20:
                dobre_miejsce = False
                
            # Sprawdzamy, czy wylosowane miejsce nie pokrywa się z żadnym kawałkiem ciała
            for segment in cialo:
                if segment.distance(losowe_x, losowe_y) < 20:
                    dobre_miejsce = False
                    
        # Jeśli pętla się skończyła, mamy pewność, że miejsce jest puste!
        jedzenie.goto(losowe_x, losowe_y)

        # Dodaje nowy segment do węża
        nowy_segment = turtle.Turtle()
        nowy_segment.speed(0)
        nowy_segment.shape("square")
        nowy_segment.color("lightgreen") # Ciało jest jaśniejsze niż głowa
        nowy_segment.penup()
        cialo.append(nowy_segment)

    # Poruszanie ciałem węża (segmenty podążają za głową)
    # Zaczynamy od końca węża i każdy segment idzie na miejsce poprzedniego
    for index in range(len(cialo)-1, 0, -1):
        x = cialo[index-1].xcor()
        y = cialo[index-1].ycor()
        cialo[index].goto(x, y)

    # Pierwszy segment ciała idzie na miejsce głowy
    if len(cialo) > 0:
        x = glowa.xcor()
        y = glowa.ycor()
        cialo[0].goto(x, y)

    ruch() # Wywołanie funkcji ruchu głowy

    # Kolizja z własnym ciałem
    for segment in cialo:
        if segment.distance(glowa) < 20:
            time.sleep(1)
            glowa.goto(0, 0)
            glowa.kierunek = "stop"
            for segment in cialo:
                segment.goto(1000, 1000)
            cialo.clear()

    time.sleep(opoznienie) # Reguluje prędkość gry

okno.mainloop() # Utrzymuje okno otwarte