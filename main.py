# Importieren der Pygame-Bibliothek
import pygame
import random
import time

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
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Variable für hauptschleife
spielaktiv = True


class Game:
    Feld = [[-1 for i in range(7)] for j in range(6)]  # Feld hat 6 Reihen und 7 Spalten
    amZug = 0
    zeigerPosition = 3  # Feldauswahl

    def __init__(self):
        self.amZug = random.randint(0, 1)
        self.zeigerPosition = 3

    def __str__(self):
        for i in self.Feld:
            print(i)

    def getSpielerColor(self):
        if self.amZug == 0:
            return ROT
        return ORANGE

    def getSpielerColorstr(self):
        if self.amZug == 0:
            return "ROT"
        return "ORANGE"

    def getStoneColor(self, x, y):
        if self.Feld[x][y] == 0:
            return ROT
        elif self.Feld[x][y] == 1:
            return ORANGE
        return WEISS

    def spielerWechsel(self):
        self.amZug = (self.amZug + 1) % 2
        self.zeigerPosition = 3

    def dropStone(self):
        lowstone = 5
        try:
            while self.Feld[lowstone][self.zeigerPosition] != -1:
                lowstone -= 1
        except:
            return 0
        self.Feld[lowstone][self.zeigerPosition] = self.amZug
        '''
        So wird das Feld abgespeichert
        for Reihe in self.Feld:
            print(Reihe)
        '''
        self.checkWin(lowstone, self.zeigerPosition)
        self.spielerWechsel()
        return 1

    def checkWaagerecht(self, x):
        Reihe = 0
        Spieler = -1
        for Element in self.Feld[x]:
            if Element == -1: continue
            if Spieler == Element:
                Reihe += 1
            else:
                Reihe = 1
                Spieler = Element
            if Reihe == 4:
                print(self.getSpielerColorstr(), "WIN")
                return 1
        return 0

    def checkVertikal(self, y):
        Reihe = 0
        Spieler = -1
        for i in range(len(self.Feld) - 1):
            Element = self.Feld[5 - i][y]
            if Element == -1: continue
            if Spieler == Element:
                Reihe += 1
            else:
                Reihe = 1
                Spieler = Element
            if Reihe == 4:
                print(self.getSpielerColorstr(), "WIN")
                return 1
        return 0

    def checkDiagonalcount(self, x, y, count=0, rechts=0, links=0):
        try:
            if self.Feld[x][y] != self.amZug or x >= len(self.Feld):
                return count
        except:
            return count
        if rechts == 1 or rechts == -1:
            return self.checkDiagonalcount(x + rechts, y + rechts, count + 1, rechts, links)
        if links == 1 or links == -1:
            return self.checkDiagonalcount(x + links, y - links, count + 1, rechts, links)

    def checkDiagonal(self, x, y):
        opt = self.checkDiagonalcount(x, y, rechts=1) + self.checkDiagonalcount(x, y, rechts=-1) - 1
        opt2 = self.checkDiagonalcount(x, y, links=1) + self.checkDiagonalcount(x, y, links=-1) - 1
        if max(opt, opt2) >= 4:
            print(self.getSpielerColorstr(), "WIN")
            return 1
        return 0

    def checkWin(self, x, y):
        global spielaktiv
        if self.checkVertikal(y) == 1 or self.checkWaagerecht(x) == 1 or self.checkDiagonal(x, y) == 1:
            hauptmenu(self.getSpielerColorstr())
            spielaktiv = False


# Spiel = Game()
def main():
    Spiel = Game()
    # Schleife Hauptprogramm
    global spielaktiv

    while spielaktiv:
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
                print("Spieler hat Quit-Button angeklickt")
            elif event.type == pygame.KEYDOWN:

                # Taste für Spieler 0
                if event.key == pygame.K_RIGHT:
                    if Spiel.amZug != 0:
                        continue
                    Spiel.zeigerPosition = min(Spiel.zeigerPosition + 1, 6)
                elif event.key == pygame.K_LEFT:
                    if Spiel.amZug != 0:
                        continue
                    Spiel.zeigerPosition = max(Spiel.zeigerPosition - 1, 0)
                elif event.key == pygame.K_DOWN:
                    if Spiel.amZug != 0:
                        continue
                    Spiel.dropStone()

                # Taste für Spieler 1
                elif event.key == pygame.K_a:
                    if Spiel.amZug != 1:
                        continue
                    Spiel.zeigerPosition = max(Spiel.zeigerPosition - 1, 0)
                elif event.key == pygame.K_s:
                    if Spiel.amZug != 1:
                        continue
                    Spiel.dropStone()
                elif event.key == pygame.K_d:
                    if Spiel.amZug != 1:
                        continue
                    Spiel.zeigerPosition = min(Spiel.zeigerPosition + 1, 6)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Spieler hat Maus angeklickt")

        # Spielfeld/figuren zeichnen
        screen.fill(BLAU)
        for i in range(7):  # Breite
            if i == Spiel.zeigerPosition:
                pygame.draw.circle(screen, Spiel.getSpielerColor(), (i * 2 * 50 + 50, 50), 40)  # Zeigerfeld
            for j in range(0, 6):
                pygame.draw.circle(screen, Spiel.getStoneColor(j, i), (i * 2 * 50 + 50, (j + 1) * 2 * 50 + 50), 40)
                # Höhe, um eins nach unter versetzt, damit der Zeiger angezeigt werden kann

        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)


def hauptmenu(winplayer=None):
    hauptmenu = True
    if winplayer != None:
        winplayer = winplayer + " hat das Spiel gewonnen."
    winnerText = myfont.render(winplayer, False, (0, 0, 0))
    textsurface = myfont.render('Klicke mit der Maus, um das Spiel zu starten.', False, (0, 0, 0))
    steuerung1 = myfont.render('Rot Steuerung: Pfeiltasten', False, (0, 0, 0))
    steuerung2 = myfont.render('Orange Steuerung: A,S,D', False, (0, 0, 0))

    while hauptmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Spieler hat Quit-Button angeklickt")
                hauptmenu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                hauptmenu = False
                main()
        screen.fill(WEISS)

        if winplayer is not None:
            screen.blit(winnerText, (0, 0))
            screen.blit(textsurface, (0, 50))

        else:
            screen.blit(textsurface, (0, 0))
            screen.blit(steuerung1, (0, 50))
            screen.blit(steuerung2, (0, 100))

        # Fenster aktualisieren
        pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)


if __name__ == '__main__':
    hauptmenu()

pygame.quit()
