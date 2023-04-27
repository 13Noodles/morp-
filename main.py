import pygame

"""
struct vecteurVitesse {
    int vitesseX;
    int vitesseY;
}

struct pos {
    int posX;
    int posY;
}

void update_pos(vecteurVitesse, pos){
    pos.posX += vecteurVitesse.vitesseX * (temps qui est passé)
    pos.posY += vecteurVitesse.vitesseY * (temps qui est passé)
}


"""



pygame.init()

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 480

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("window title")

running = True

CELL_EMPTY = 0
CELL_JOUEUR1 = 1
CELL_JOUEUR2 = 2

COLOR_CELL_BORDER = (100,100,0)
COLOR_CELL_EMPTY = (50,50 ,50)
COLOR_CELL_JOUEUR1 = (255,255,255)
COLOR_CELL_JOUEUR2 = (255,0,0)

rectangles = []
cell_values = []

for colonneId in range(0,3):
    colonne = []
    cell_colonne = []
    for ligneId in range(0,3):
        colonne.append( pygame.Rect(colonneId*WINDOW_WIDTH/3 ,ligneId*(WINDOW_HEIGHT/3), WINDOW_WIDTH/3, WINDOW_HEIGHT/3) )
        cell_colonne.append(CELL_EMPTY)
    rectangles.append(colonne)
    cell_values.append(cell_colonne)

print(cell_values)
cell_values[0][0] = CELL_JOUEUR1
cell_values[0][2] = CELL_JOUEUR2

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                # recup colonne
                # recup ligne
                # check que ca rentre dans l'array rectangles (pas d'index out of bound)
                # if ^ ok assigne la valeur du joueur actuel a cell_values
                print(event)
    
    # update


    # drawing
    window.fill((0,0,0))


    """
    for(int=0; i<300; i++){
        r = t[i]
        ... draw.rect(..)
    }
    """

    for colonneId in range(len(rectangles)):
        for ligneId in range(len(rectangles[colonneId])):
            draw_color = COLOR_CELL_EMPTY
            if cell_values[colonneId][ligneId] == CELL_JOUEUR1:
                draw_color = COLOR_CELL_JOUEUR1
            elif cell_values[colonneId][ligneId] == CELL_JOUEUR2:
                draw_color = COLOR_CELL_JOUEUR2

            pygame.draw.rect(window, draw_color, rectangles[colonneId][ligneId], 0)
            pygame.draw.rect(window, COLOR_CELL_BORDER, rectangles[colonneId][ligneId], 1)
    
    pygame.display.update()
