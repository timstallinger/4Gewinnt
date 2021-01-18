# Importieren der Pygame-Bibliothek
import pygame
import random

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE = (255, 140, 0)
GELB = (255, 0, 0)
BLAU = (0, 0, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)

# Fenster öffnen
screen = pygame.display.set_mode((700, 700))

# Titel für Fensterkopf
pygame.display.set_caption("4 Gewinnt")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


class Game:
    Feld = [[-1 for i in range(7)] for i in range(6)] #Feld hat 6 Reihen und 7 Spalten
    amZug = ROT
    zeigerPosition = 3 #Feldauswahl

    def __init__(self):
        zufall = random.randint(0, 1)
        if zufall:
            self.amZug = ROT
        else:
            self.amZug = ORANGE

    def __str__(self):
        for i in self.Feld:
            print(i)

Spiel = Game()

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                if Spiel.amZug != ROT:
                    continue
                Spiel.zeigerPosition = min(Spiel.zeigerPosition + 1, 6)
            elif event.key == pygame.K_LEFT:
                if Spiel.amZug != ROT:
                    continue
                Spiel.zeigerPosition = max(Spiel.zeigerPosition - 1, 0)
            elif event.key == pygame.K_DOWN:
                Spiel.amZug = ORANGE

            # Taste für Spieler 2
            elif event.key == pygame.K_a:
                if Spiel.amZug != ORANGE:
                    continue
                Spiel.zeigerPosition = max(Spiel.zeigerPosition - 1, 0)
            elif event.key == pygame.K_s:
                Spiel.amZug = ROT
            elif event.key == pygame.K_d:
                if Spiel.amZug != ORANGE:
                    continue
                Spiel.zeigerPosition = min(Spiel.zeigerPosition + 1, 6)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")

    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(BLAU)

    # Spielfeld/figuren zeichnen
    for i in range(7): #Breite
        #TODO: entfernen
        if i == Spiel.zeigerPosition:
            pygame.draw.circle(screen, Spiel.amZug, (i * 2 * 50 + 50, 50), 40) #Zeigerfeld
        for j in range(1,7): # Höhe, um eins nach unter versetzt, damit der Zeiger angezeigt werden kann
            pygame.draw.circle(screen,WEISS,(i * 2 * 50 + 50,j * 2 * 50 + 50),40)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()
