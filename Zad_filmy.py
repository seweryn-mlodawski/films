import random
import datetime

class Film:
    """Klasa reprezentująca film"""
    def __init__(self, title, year, genre):
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

class Series:
    """Klasa reprezentująca serial"""
    def __init__(self, title, year, genre, season_number, episode_number):
        self.title = title
        self.year = year
        self.genre = genre
        self.season_number = season_number
        self.episode_number = episode_number
        self.play_count = 0

    def play(self):
        """Zwiększa liczbę odtworzeń o 1"""
        self.play_count += 1
    
    def __str__(self): 
        """Zwraca string w formacie: 'Tytuł S01E05'"""        
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

# === FUNKCJE LOGICZNE ===

def get_movies(library):
    """Zwraca filmy posortowane alfabetycznie"""
    # Filtrujemy tylko obiekty klasy Film (i wykluczamy Series, by być pewnym)
    movies = [item for item in library if isinstance(item, Film) and not isinstance(item, Series)]
    return sorted(movies, key=lambda x: x.title)

def get_series(library):
    """Zwraca seriale posortowane alfabetycznie"""
    series_list = [item for item in library if isinstance(item, Series)]
    return sorted(series_list, key=lambda x: x.title)

def search(library, title):
    """Szuka tytułu (niezależnie od wielkości liter)"""
    return [item for item in library if title.lower() in item.title.lower()]

def generate_views(library):
    """Losuje element i dodaje mu od 1 do 100 odtworzeń"""
    if not library:
        return
    item = random.choice(library)
    views_to_add = random.randint(1, 100)
    for _ in range(views_to_add):
        item.play()

def run_generate_views_10_times(library):
    """Uruchamia generowanie odtworzeń 10 razy"""
    for _ in range(10):
        generate_views(library)

def top_titles(library, n=3, content_type=None):
    """Zwraca top N najpopularniejszych tytułów"""
    if content_type == 'movies':
        items = get_movies(library)
    elif content_type == 'series':
        items = get_series(library)
    else:
        items = library
    
    # Sortowanie malejąco po liczbie odtworzeń (reverse=True)
    return sorted(items, key=lambda x: x.play_count, reverse=True)[:n]

# === GŁÓWNA CZĘŚĆ PROGRAMU ===

if __name__ == "__main__":
    # 1. Komunikat powitalny
    print('''
=================
Biblioteka filmów
=================''')

    # 2. Wypełnianie biblioteki treścią
    library = []
    
    library.append(Film("Pulp Fiction", 1994, "Kryminał"))
    library.append(Film("Incepcja", 2010, "Sci-Fi"))
    library.append(Film("Skazani na Shawshank", 1994, "Dramat"))
    library.append(Film("Nietykalni", 2011, "Biograficzny"))
    
    library.append(Series("The Simpsons", 1989, "Animacja", 1, 5))
    library.append(Series("Breaking Bad", 2008, "Dramat", 5, 14))
    library.append(Series("Stranger Things", 2016, "Horror", 4, 1))
    library.append(Series("The Crown", 2016, "Dramat", 1, 1))

    # 3. Generowanie odtworzeń
    run_generate_views_10_times(library)

    # 4. Wyświetlanie komunikatu z datą
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {current_date}\n")

    # 5. Wyświetlanie Top 3
    top_3 = top_titles(library, n=3)
    for item in top_3:
        print(f"{item} - {item.play_count} odtworzeń")