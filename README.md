## Zaawansowane języki programowania

### Tytuł: Refaktoryzacja kodu
### Autor: Zofia Tabaczyńska 271295
### Link: https://github.com/zofia123/zaawansowane-jezyki
### Refaktoryzowany kod:
https://github.com/emilybache/Parrot-Refactoring-Kata/tree/master/Python
### Kontekst:
Kod jest inspirowany przykładem z książki Martina Fowlera „Refaktoryzacja”. Celem projektu jest refaktoryzacja kodu, czyli wprowadzenie zmian poprawiających czytelność kodu oraz jego jakość w celu łatwiejszej jego konserwacji w przyszłości.

### Opis:
Program Parrot przechowuje informacje na temat trzech różnych rodzajów papug: Europejskiej, Afrykańskiej i Norweskiej.

### Narzędzie Metrics:
+ Radon
+ Wily

#### Maintainability Index (MI)
|MI score|Rank|Maintainability
|-|-|-
|```100-20```| A |Very high
|```19-10```| B |Medium
|```9-0```| C |Extremely low

#### Cyclomatic Complexity (CC)
|CC score|Rank|Risk 
|-|-|-
|```1-5```|A|low - simple block
|```6-10```|B|low - well structured and stable block
|```11-20```|C |moderate - slighltly complex block
|```21-30```|D|more than moderate - more complex block
|```31-40```|E|high - complex block, alarming
|```41+```|F|very high - error-prone, unstable block

## Etapy refaktoryzacji:
> ## V0
> + MI: 69.70
> + CC: A (1.86)
> + LOC: 38
> 
> Code smells:
> + Zduplikowany kod(Duplicated Code)
> + Nadmiernie rozbudowana klasa (Large Class)
> + Zmiany z wielu przyczyn (Divergent Change)

> ## V1
> + MI: 66.90
> + CC: A (1.63)
> + LOC: 48
>
> Refactors:
> + Zamiana liczby na zdefiniowaną stałą (Replace Magic Literal)
> + Zamiana metod na zdefiniowaną stałą (Replace Magic Literal)
> + Usunięcie zbędnych metod (Remove Dead Code)
>   - _load_factor()
>   - _base_speed()
> + Ekstrakcja metody (Extract method)
>   - utworzono metodę _african_speed()
>   - utworzono metodę _norwegian_speed()
>   - utworzono metodę _european_speed()
> + Usunięcie parametru z funkcji (Remove Parameter)
>   - usunięto parametr z funkcji _african_speed()
>
> Code Smells:
> + Nadmiernie rozbudowana klasa (Large Class)
> + Spekulacyjne uogólnianie (Speculative Generality)
> + Skomplikowane instrukcje warunkowe (Switch Statements)


> ## V2
> + MI: 67.86
> + CC: A(1.31)
> + LOC: 59
> 
> Refactors:
> + Ekstrakcja klasy (Extract Class)
>   - utworzenie klasy EuropeanParrot i przeniesienie metody _european_speed()
>   - utworzenie klasy AfricanParrot i przeniesienie metody _african_speed()
>   - utworzenie klasy NorwegianParrot i przeniesienie metody _norwegian_speed()
> + Użycie polimorfizmu w miejsce instrukcji warunkowych (Replace Conditional with Polymorphism)
> + Usunięcie klasy enum (Remove enum)
> + Usunięcie zbędnych parametrów (Remove parameter)
>   - __init__() w klasie EuropeanParrot
>   - __init__() w klasie AfricanParrot
>   - __init__() w klasie NorwegianParrot
>
> Code Smells:
> + Spekulacyjne uogólnianie (Speculative Generality)
> + Zazdrość o funkcje (Feature Envy)


> ## V3 - Infinity
> + MI: 75.05
> + CC: A(1.4)
> + LOC: 39
>
> Refactors:
> +  Przeniesienie pól do innych klas (Push Down Field)
>   - self.number_of_coconuts do klasy AfricanParrot
>   - self.voltage = voltage oraz self.nailed = nailed do klasy NorwegianParrot
>   - LOAD_FACTOR do klasy AfricanParrot
>   - MAX_SPEED do NorwegianParrot
> + Usunięcie zbędnych parametrów (Remove parameter)
>   - __init__() w klasie EuropeanParrot
>   - __init__() w klasie AfricanParrot
>   - __init__() w klasie NorwegianParrot
> + Usunięcie zbędnych metod (Remove Method)
>   - usunięcie _european_speed()
>   - usunięcie _african_speed()
>   - usunięcie _norwegian_speed()
> + Przeniesienie metody do wyższej klasy (Pull Up Method)
>   - przeniesienie metody speed() z klasy EuropeanParrot do klasy Parrot

## Podsumowanie
<p align="center">
    <img src="Chart/metryki.png">
</p>
