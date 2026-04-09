# Refaktoryzacja Kodu

Należało zrefaktoryzować pierwsze trzy pliki z repozytorium : [Tennis Kata](https://github.com/emilybache/Tennis-Refactoring-Kata/tree/main/python)

## Tennis 1

Przesunięto remis, wygraną i przypisywanie obecnego wyniku do osobnej funkcji/słownika.

Zaprzestano używania sztywnego stringa "player1" oraz "player2" i zmieniono na self.player1_name.

Zmieniono return result w funkcji score, na return w każdym if'ie.

## Tennis 2

Zaprzestano używania sztywnego stringa "player1" oraz "player2" i zmieniono na self.player1_name.

Stworzono point_to_score zwracająca punkty.

Rozbito score na:
- Remis
- mniej niż 4 punkty dla obu zawodników
- wygraną jednego z zawodników
- sytuacje przewagi

Zmieniono kolejność sprawdzania operacji.

Zebranie case'ów do podobnych if'ów.

Dodanie komentarzy.

Usunięcie Deadcode.

## Tennis 3

Zmiana zmiennych z p1_n na p1_name oraz z p1 na p1_score.

W funkcji score:
  - zmiana zmiennych
  - dodanie zmiennych pomocniczych is_draw oraz is_not_win