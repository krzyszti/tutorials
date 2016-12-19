# Pygame

## Pierwsza aplikacja

Aplikacja wyświetli puste okno a po jego zamknięciu zostanie zakończona.

```python
import pygame


class App(object):
    def __init__(self):
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

```

### 1. Importujemy potrzebne biblioteki

```
import pygame
```

Będzie nam potrzebne aby obsłużyć eventy oraz wyświetlanie okien, obrazków i animacji.

### 2. Definiujemy główną klasę aplikacji

#### a) metoda __init__ wykonywana jest tuż po utworzeniu obiektu klasy App

```python
def __init__(self):
    self._running = True
    pygame.init()
    self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
```

Ustawiana jest zmienna klasy `_running = True` będzie ona użyta do zakończenia głównej pętli aplikacji.

Następnie inicjalizowana jest aplikacja pygame poprzez `pygame.init()`.

Ostatnią rzeczą są ustawienia samego okna któ®e będzie wyświetlone, używając metody `set_mode` zawartej w `pygame.display`.
Pierwszym argumentem `(640, 480)` jest tuple zawierający rozmiary okna, odpowiednio, x a następnie y wyrażone w pixelach.
Kolejny argument to tryb wyświetlania okna, używamy tutaj operatora `or` aby wybrać odpowiedni tryb.
Więcej o trybach można przeczytać [tutaj](http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)

#### b) metoda on_event będzie wykonywana za każdym wykonaniem głównej pętli aplikacji

```python
def on_event(self, event):
    if event.type == pygame.QUIT:
        self._running = False
```

W tym przykładzie sprawdzamy czy event który wystąpił jest eventem zamykającym okno `pygame.QUIT`. Jeśli tak zmienna klasy która odpowiada za główną pętlę aplikacji zostaje ustawiona na False.

#### c) metoda on_execute wywoływana jest po utworzeniu obiektu klasy App

```python
def on_execute(self):
    while self._running:
        for event in pygame.event.get():
            self.on_event(event)

    pygame.quit()
```

W metodzie tej znajduje się pętla, która będzie się wykonywać tak długo aż `_running` będzie prawdą. Następnie sprawdzone są wszystkie eventy które zarejestrowało pygame i wywoływana jest na nich metoda `on_event`.
Jak już wcześniej było wspomniane w przypadku eventu `QUIT` zmienna `_running` zostanie ustawiona na False, co spowoduje zakończenie wykonywania pętli while.
Ostatnią rzeczą będzie wywołanie metody `quit()`, która spowoduje zwolnienie zasobów wykorzystywanych przez pygame zasobów.

### 3. Uruchomienie aplikacji

```python
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
```

Utworzenie obiektu klasy `App` a następnie wykonanie metody `on_execute` która zawiera główną pętlę aplikacji.

## Ogólne porady

Przyjęło się, że aplikacja powinna posiadać następujące metody w swojej pętli głównej.

```python
while True:
    self.events()
    self.loop()
    self.render()
```

`events` - metoda która powinna zawierać obsługę eventów

`loop` - metoda która zajmuje się obliczeniami, może to być np wynik nowej rundy, nowe pozycje elementów na ekranie

`render` - metoda odpowiedzialna za rysowanie obecnego widoku aplikacji

Jeśli zastosujemy te zasady to aplikacja z poprzedniego przykładu będzie wyglądać następująco

```python
import pygame


class App(object):
    def __init__(self):
        self._running = True
        pygame.init()
        self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def events(self):
        for event in pygame.event.get():
            self.on_event(event)

    def loop(self):
        pass

    def render(self):
        pass

    def on_execute(self):
        while self._running:
            self.events()
            self.loop()
            self.render()

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

```

## Eventy

Poznaliśmy już jeden z eventów pygame `QUIT` odpowiedzialny za zamknięcie okna. Jakie jeszcze eventy oferuje pygame?

Jednym z łatwych i szybkich sposobów aby je poznać jest zmiana metody `on_event` w naszej aplikacji oraz dodanie `print(event)`

```python
def on_event(self, event):
    print(event)
    if event.type == pygame.QUIT:
        self._running = False
```

Po uruchomieniu aplikacji możemy zauważyć, że pierwsze eventy zaczną się wyświetlać zanim użytkownik zdąży coś zrobić.
W moim przypadku były to:
```
<Event(1-ActiveEvent {'state': 1, 'gain': 0})>
<Event(4-MouseMotion {'buttons': (0, 0, 0), 'pos': (639, 359), 'rel': (639, 359)})>
```

Pierwszy z nich `ActiveEvent` odpowiada za eventy związane z samym oknem, drugi natomiast zwrócił obecny stan myszki, wciśnięte przyciski oraz pozycję kursora.
Jeśli nie będziemy potrzebowali tych eventów, to możemy je w tej chwili zignorować.

W tym momencie możemy przetestować eventy myszy. Klikanie jej przycisków oraz ruch może dać różne eventy np.

```
<Event(5-MouseButtonDown {'button': 3, 'pos': (286, 166)})>
<Event(4-MouseMotion {'buttons': (0, 0, 1), 'pos': (370, 138), 'rel': (84, -28)})>
<Event(4-MouseMotion {'buttons': (0, 0, 1), 'pos': (371, 138), 'rel': (1, 0)})>
<Event(6-MouseButtonUp {'button': 3, 'pos': (371, 138)})>
<Event(5-MouseButtonDown {'button': 1, 'pos': (371, 138)})>
```

##### Jeśli widzisz tylko eventy myszy oraz używasz `Pythona 3`, musisz wiedzieć że pygame może nie działać w pełni. Pygame powinien działać bez problemu pod wersją pythona `3.2`!

W przypadku niedziałających eventów klawiatury, należy zainteresować się następującą funkcją `pygame.key.get_pressed()`

#### Obsługa eventów klawiatury

```python
def on_event(self, event):
    print(event)
    if event.type == pygame.QUIT:
        self._running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            self._running = False
```

Po sprawdzeniu czy wystąpił event QUIT sprawdzamy czy został przyciśnięty przycisk na klawiaturze, w tym momencie nie ma znaczenia jaki.
Następnie sprawdzamy czy klawisz który został wciśnięty był klawiszem Escape. Jeśli tak to wychodzimy z naszej głównej pętli i aplikacja się kończy.

Niektóre z dostępnych eventów oraz właściwości które posiadają:
```
QUIT             none
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
```

## Grafika

Najprostszym sposobem na wyświetlenie grafiki jest wczytanie jej poprzez `pygame.image.load()`

Zmodyfikujmy naszą metodę `__init__`:

```
def __init__(self):
    self._running = True
    self.background = pygame.image.load('background.png')
    pygame.init()
    self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
```

Zakładając oczywiście, że taki obraz jak `background.png` istnieje w katalogu z naszą aplikacją obraz powinien się wczytać.
Jednak po uruchomieniu aplikacji jeszcze go nie zobaczymy.
Obraz został wczytany, ale musimy go wyrenderować na ekranie.

W tym celu należu zmodyfikować naszą metodę render.

```
def render(self):
    self._display_surf.blit(self.background, (0, 0))
    pygame.display.flip()
```

To może wyglądać jak magia, ale to całkiem proste.
Jak pamiętacie z `__init__` zmienna `_display_surf` zawiera okno pygame. Metoda `blit` powoduje dodanie do ekranu pod koordynatami 0 oraz 0 (tuple) obrazu który przechowujemy w zmiennej background.
`pygame.display.flip()` rysuje to co przygotowaliśmy na ekranie.

## Prosta animacja

Aby zaprezentować jak działają animacje dodamy bohatera gry.
W tym celu znów modyfikujemy `__init__`

```
def __init__(self):
    self._running = True
    self.background = pygame.image.load('background.png')
    self.hero = pygame.image.load('hero.png')
    self.x = 0
    self.y = 0
    pygame.init()
    self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
```

Ładowany jest nowy obraz o nazwie `hero.png` a także koordynaty postaci.

Następnie modyfikowana jest metoda `on_event`

```
def on_event(self, event):
    print(event)
    if event.type == pygame.QUIT:
        self._running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            self._running = False
        if event.key == pygame.K_UP:
            self.y -= 5
        if event.key == pygame.K_DOWN:
            self.y += 5
        if event.key == pygame.K_RIGHT:
            self.x += 5
        if event.key == pygame.K_LEFT:
            self.x -= 5
```

Po wciśnięciu klawiszy strzałek x oraz y naszego bohatera ulegnie zmianie.
Jeśli prawa i lewa strona nie stanowi żadnego problemu (prawo +, lewo -) to góra i dół może na początku trochę zmylić. Ponieważ obraz renderowany jest od góry do dołu. (Góra -, dół +)

Ostatnią rzeczą będzie zmodyfikowanie metody `render`

```
def render(self):
    self._display_surf.blit(self.background, (0, 0))
    self._display_surf.blit(self.hero, (self.x, self.y))
    pygame.display.flip()
```

Poprzez dodanie rysowania naszego obrazka z bohaterem

W tym momencie możemy uruchomić naszą aplikację a po wciśnięciu odpowienich przycisków postać zacznie się poruszać.

Można zauważyć, że będzie też można "wyjechać" postacią poza okno. Aby temu zapobiec modyfikujemy metodę `loop`

```
def loop(self):
    if self.x < 0:
        self.x = 0
    if self.y < 0:
        self.y = 0
```

Sprawdzamy w niej proste warunki, dzięki nim postać pozostanie już w obrębie okna.


## Ostateczny wygląd aplikacji
```
import pygame


class App(object):
    def __init__(self):
        self._running = True
        self.background = pygame.image.load('background.png')
        self.hero = pygame.image.load('hero.png')
        self.x = 0
        self.y = 0
        pygame.init()
        self._display_surf = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_event(self, event):
        print(event)
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_UP:
                self.y -= 5
            if event.key == pygame.K_DOWN:
                self.y += 5
            if event.key == pygame.K_RIGHT:
                self.x += 5
            if event.key == pygame.K_LEFT:
                self.x -= 5

    def events(self):
        for event in pygame.event.get():
            self.on_event(event)

    def loop(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def render(self):
        self._display_surf.blit(self.background, (0, 0))
        self._display_surf.blit(self.hero, (self.x, self.y))
        pygame.display.flip()

    def on_execute(self):
        while self._running:
            self.events()
            self.loop()
            self.render()

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

```

Jak widać jej wygląd oraz styl kodowania może być nieładny, ale pamiętajmy, że to tylko tutorial.

# Co dalej?

Warto odwiedzić dokumentację pygame, jest w niej opisanych wiele przydatnych rzeczy.

[Pygame docs](http://www.pygame.org/docs/)

Tutorial na którym bazowałem można znaleźć [tutaj](http://pygametutorials.wikidot.com/tutorials-basic)

[Invent with python](http://inventwithpython.com/) strona zawierająca kilka darmowych ebooków, w tym o grach w pythonie.

Możecie też odwiedzić moje konto na githubie gdzie umieściłem kiedyś prostą [grę platformową](https://github.com/krzyszti/my_projects/tree/master/Python/Games/Platformer) napisaną w pygame
