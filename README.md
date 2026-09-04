# Project_Dyplomowy
Dokumentacja projektu – status bieżący
1. Co już zostało zrobione
W tej chwili projekt ma już przygotowaną podstawę backendową w frameworku FastAPI.

Zrealizowane elementy:

utworzenie aplikacji FastAPI w main.py
dodanie głównego endpointu strony startowej
przygotowanie struktury projektu:
book.py
book.py
routers.py
database.py
crud.py
dodanie prostego modelu książki
utworzenie walidacji danych wejściowych za pomocą Pydantic
zintegrowanie bazy SQLite
przygotowanie podstawowych operacji CRUD:
pobranie wszystkich książek
pobranie jednej książki
dodanie książki
aktualizacja książki
usunięcie książki
przygotowanie prostego widoku HTML do obsługi książek w index.html
Dodatkowo projekt ma już działającą strukturę, która pozwala:

uruchomić aplikację lokalnie
korzystać z API
przeglądać dokumentację Swagger
dodawać dane do bazy


2. Obecny stan techniczny
Projekt jest na etapie:

podstawowego backendu
bazy danych
prostego interfejsu użytkownika
To oznacza, że mamy już gotowy fundament, ale nadal brakuje elementów bardziej „produktowych”, takich jak:

pełna obsługa frontendu
lepszy wygląd strony
system logowania
autoryzacja użytkowników
bardziej rozbudowana logika biznesowa


3. Co będzie dalej
Etap 1: Rozbudowa interfejsu
dodanie przycisków do edycji i usuwania książek
poprawa wyglądu strony
dodanie formularzy i komunikatów o sukcesie/błędzie
Etap 2: Ulepszenie backendu
dodanie endpointów do pełnej obsługi książek
poprawa obsługi błędów
dodanie paginacji i filtrowania
zabezpieczenie API
Etap 3: Użytkownicy i logowanie
model użytkownika
rejestracja
logowanie
token JWT
role użytkowników (np. admin / zwykły użytkownik)

Etap 4: Rozszerzenie funkcjonalności projektu
dodanie kategorii książek
dodanie opinii / ocen
możliwość wyszukiwania książek
dodanie sortowania i filterów
Etap 5: Testowanie i finalizacja
testy API
testy jednostkowe
poprawa dokumentacji
przygotowanie projektu do prezentacji / obrony
4. Krótka rekomendacja
Najlepszym kierunkiem na teraz jest dalszy rozwój w kierunku:

backend + baza danych + prosty frontend
To jest najbezpieczniejsza ścieżka, ponieważ projekt już ma działający fundament i można go łatwo rozbudowywać bez ryzyka chaosu w kodzie.

5. Podsumowanie
W tej chwili projekt jest w fazie:

działającego MVP
podstawowego systemu zarządzania książkami
gotowego fundamentu do dalszego rozwoju
Następne kroki powinny skupiać się na:

wygodnym UI
rozbudowie funkcjonalności
użytkownikach i logowaniu
finalizacji projektu pod prezentację
