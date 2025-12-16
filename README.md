Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Liczba odtworzeń
Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Numer odcinka
Numer sezonu
Liczba odtworzeń
Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
Przechowuje filmy i seriale w jednej liście.
Dodatkowo:

Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.
Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
Napisz funkcję, która uruchomi generate_views 10 razy.
Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
