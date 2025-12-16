# Biblioteka filmów i seriali

class Film:
    """Klasa reprezentująca film"""

    def __init__(self, title, year, genre):
        """
        Inicjalizacja filmu
        
        Argumenty:
            title (str): Tytuł filmu
            year (int): Rok wydania filmu
            genre (str): Gatunek filmu
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.play_count = 0

    def play(self):
        """Zwiększa liczbę odtworzeń o 1"""
        self.play_count += 1
    
    def __str__(self):
        """Zwraca string w formacie: 'Tytuł (Rok)'"""
        return f"{self.title} ({self.year})"
    # nic ciekawego
class Series:
    """Klasa reprezentująca serial"""
    
    def __init__(self, title, year, genre, season_number, episode_number):
        """
        Inicjalizacja serialu
        
        Argumenty:
            title (str): Tytuł serialu
            year (int): Rok wydania serialu
            genre (str): Gatunek serialu
            episode_number (int): Numer odcinka
            season_number (int): Numer sezonu
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.episode_number = episode_number
        self.season_number = season_number
        self.play_count = 0

    def play(self):
        """Zwiększa liczbę odtworzeń o 1"""
        self.play_count += 1
    
    def __str__(self): 
        """Zwraca string w formacie: 'Tytuł S01E05'"""
        return f"{self.title} ({self.year}) - S{self.season_number:02d}E{self.episode_number:02d}"
    
    # Główna część programu
if __name__ == "__main__":
    # Tworzenie przykładowych filmów i seriali
    library = []

    # Dodawanie filmów
    film1 = Film("Incepcja", 2010, "Sci-Fi")
    film2 = Film("Matrix", 1999, "Sci-Fi")
    film3 = Film("Gladiator", 2000, "Akcja")
    
    # Dodawanie seriali
    series1 = Series("Stranger Things", 2016, "Horror", 1, 1)
    series2 = Series("Breaking Bad", 2008, "Kryminał", 2, 1)
    series3 = Series("The Crown", 2016, "Dramat", 1, 1)

    library.append(film1)
    library.append(film2)
    library.append(film3)

    library.append(series1)
    library.append(series2)
    library.append(series3)

    # Symulacja odtwarzania filmów i seriali
    film1.play()
    film1.play()
    film2.play()
    print(f"{film1} - Liczba odtworzeń: {film1.play_count}")

    series1.play()
    series1.play()
    series1.play()
    series2.play()
    print(f"{series1} - Liczba odtworzeń: {series1.play_count}")

    # Wyświetlanie statystyk
    print("\n=== STATYSTYKI BIBLIOTEKI ===\n")
    for item in library:
        typ = "Film" if isinstance(item, Film) else "Serial"
        print(f"{typ}: {item}")
        print(f"Gatunek: {item.genre}")
        print(f"Rok wydania: {item.year}")
        print(f"Liczba odtworzeń: {item.play_count}")
        print()    