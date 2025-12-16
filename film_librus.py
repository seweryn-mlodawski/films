# Biblioteka filmów i seriali

import datetime


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
    

        # === Funkcje dodatkowe ===
    def get_movies(library):
        """Zwraca listę filmów posortowanych alfabetycznie po tytule
        Argumenty:
            library (list): Lista filmów i seriali
        Zwraca:
            list: Posortowana lista filmów
        """
        movies = [item for item in library if isinstance(item, Film)]
        return sorted(movies, key=lambda x: x.title)
    
    def get_series(library):
        """Zwraca listę seriali posortowanych alfabetycznie po tytule
        Argumenty:
            library (list): Lista filmów i seriali
        Zwraca:
            list: Posortowana lista seriali
        """
        series_list = [item for item in library if isinstance(item, Series)]
        return sorted(series_list, key=lambda x: x.title)
    
    def search(library, title):
        """Wyszukuje film lub serial po tytule
        Argumenty:
            library (list): Lista filmów i seriali
            title (str): Tytuł do wyszukania
        Zwraca:
            list: Lista pasujących filmów/seriali
        """
        title_lower = title.lower()
        return [item for item in library if title_lower in item.title.lower()]
    
    def generate_views(library):
        """Losowo zwiększa liczbę odtworzeń losowego filmu lub serialu
        Argumenty:
            library (list): Lista filmów i seriali
        """
        if not library:
            print("Biblioteka jest pusta.")
            return
        
        item = random.choice(library)
        views_to_add = random.randint(1, 100)
        for _ in range(views_to_add):
            item.play()

    def generate_views_multiple(library, times=10):
        """Generuje losowe odtworzenia dla losowych filmów/seriali wielokrotnie
        Argumenty:
            library (list): Lista filmów i seriali
            times (int): Liczba losowych generacji odtworzeń
        """
        for _ in range(times):
            generate_views(library)


    def top_titles(library, n=3, content_type=None):
        """Zwraca top n filmów lub seriali według liczby odtworzeń
        Argumenty:
            library (list): Lista filmów i seriali
            n (int): Liczba top pozycji do zwrócenia
            content_type (str): 'movie' lub 'series' lub None dla obu
        Zwraca:
            list: Lista top n filmów/seriali
        """
        if content_type == 'movie':
            filtered_library = [item for item in library if isinstance(item, Film)]
        elif content_type == 'series':
            filtered_library = [item for item in library if isinstance(item, Series)]
        else:
            filtered_library = library
        
        sorted_items = sorted(filtered_library, key=lambda x: x.play_count, reverse=True)
        return sorted_items[:n]
        
            # Główna część programu
if __name__ == "__main__":

    # 1. Wyświetlanie komunikatu
    print("=" * 30)
    print("  BIBLIOTEKA FILMÓW  ")
    print("=" * 30)
    # Tworzenie przykładowych filmów i seriali
    library = []

    # 2. Dodawanie filmów (wypełnianie treścią)
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

    # 3. Wygeneruj odtworzenia za pomocą generate_views (10 razy)
    generate_views_multiple(library, times=10)
    
    # 4. Wyświetl komunikat z bieżącą datą w formacie DD.MM.RRRR
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    print(f"\n=== TOP 3 FILMY na dzień {current_date} ===\n")
    print("=" * 30)
   
   # 5. Wyświetl listę top 3 najpopularniejszych tytułów (filmów i seriali)
    top_3 = top_titles(library, n=3)
    for idx, item in enumerate(top_3, start=1):
        typ = "Film" if isinstance(item, Film) else "Serial"
        print(f"{idx}. {typ}: {item} - Liczba odtworzeń: {item.play_count}")

    # Wyświetlanie statystyk
    print("\n=== STATYSTYKI BIBLIOTEKI ===\n")
    for item in library:
        typ = "Film" if isinstance(item, Film) else "Serial"
        print(f"{typ}: {item}")
        print(f"Gatunek: {item.genre}")
        print(f"Rok wydania: {item.year}")
        print(f"Liczba odtworzeń: {item.play_count}")
        print()