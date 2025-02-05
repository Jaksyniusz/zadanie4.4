#kod wygenerowany przez AI
import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Funkcja do wyboru działania
def wybierz_dzialanie():
    print(">> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    dzialanie = int(input())  # Pobieramy numer działania
    return dzialanie

# Funkcja do pobierania liczb
def pobierz_liczby():
    liczba1 = float(input("Podaj składnik 1: "))  # Pobieramy pierwszą liczbę
    liczba2 = float(input("Podaj składnik 2: "))  # Pobieramy drugą liczbę
    return liczba1, liczba2

# Funkcja do wykonywania obliczeń
def wykonaj_obliczenie(dzialanie, liczba1, liczba2):
    if dzialanie == 1:
        wynik = liczba1 + liczba2
        logging.info(f"Dodaję {liczba1:.2f} i {liczba2:.2f}")
    elif dzialanie == 2:
        wynik = liczba1 - liczba2
        logging.info(f"Odejmuję {liczba1:.2f} i {liczba2:.2f}")
    elif dzialanie == 3:
        wynik = liczba1 * liczba2
        logging.info(f"Mnożę {liczba1:.2f} i {liczba2:.2f}")
    elif dzialanie == 4:
        if liczba2 == 0:
            logging.error("Nie można dzielić przez zero!")
            return None
        wynik = liczba1 / liczba2
        logging.info(f"Dzielę {liczba1:.2f} i {liczba2:.2f}")
    else:
        logging.error("Nieprawidłowy wybór działania!")
        return None

    return wynik

# Główna funkcja programu
def main():
    dzialanie = wybierz_dzialanie()  # Wybieramy działanie
    liczba1, liczba2 = pobierz_liczby()  # Pobieramy liczby

    # Wykonujemy obliczenie
    wynik = wykonaj_obliczenie(dzialanie, liczba1, liczba2)

    # Wyświetlamy wynik, jeśli obliczenie się powiodło
    if wynik is not None:
        print(f"Wynik to {wynik:.2f}")

# Uruchamiamy program
if __name__ == "__main__":
    main()