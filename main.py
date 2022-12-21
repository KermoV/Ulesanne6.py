import pygame # Impordime pygame'i
import sys # Impordime sys'i

pygame.init() # Algatan pygame'i

# Load the background music
pygame.mixer.music.load("Fluffing-a-Duck.mp3")

# Set the volume of the music
pygame.mixer.music.set_volume(0.3)

# Play the music in a loop
pygame.mixer.music.play(-1)

#Värvid
lBlue = [153, 204, 255] # Muutuja lBlue saab väärtuseks [153, 204, 255]

#Ekraani seaded
screenX = 640 # ScreenX saab väärtuseks 640px
screenY = 480 # ScreenY saab väärtuseks 480px
screen=pygame.display.set_mode([screenX,screenY]) # Muutuja screen saab väärtuseks pygame.display.set_mode([640,480])
pygame.display.set_caption('6') # Määrab praeguse akna pealkirja
screen.fill(lBlue) # Täidab ekraani
clock = pygame.time.Clock() # Loon kella objekti

#Lisame tausta
bg = screen.fill(lBlue) # Muutja bg saab väärtuse pygame.image.load("bg_rally.jpg")

#Lisame palli
pall = pygame.image.load("ball.png") # Muutuja pall saab väärtuse pygame.image.load("ball.png")
screen.blit(pall,[299,390]) # Palli asetus ekraanil (laius,kõrgus)

#Palli kiirus ja asukoht
posX1, posY1 = 180, 50 # X ja Y asetus ekraanil
speedX1, speedY1 = 3, 3 # X ja Y kiirus ekraanil

# Balli laiuse ja suuruse võtmine
ball_width, ball_height = pall.get_size()

# Ekraani laiuse ja suuruse võtmine
screenX, screenY = screen.get_size()

#Lisame aluse
alus = pygame.image.load("pad.png") #Muutuja alus saab väärtuse pygame.image.load("pad.png")
alus = pygame.transform.scale(alus, (120, 20)) #Muutuja alus saab väärtuse pygame.transform.scale(alus, (120, 20))

# Määrab ekraani keskpunkti X suunas
screen_center_x = screenX / 2 # Muutuja screen_center_x saab väärtuseks screenX jagatud 2

#Aluse asukoht
pad_pos_x = screen_center_x - (alus.get_width() / 2) # Muutuja pad_pos_x saab väärtuse screen_center_x - (alus.get_width() / 2)
pad_pos_y = screenY / 1.5 # Muutuja pad_pos_y saab väärtuse screenY jagatud 1.5
screen.blit(alus, [pad_pos_x, pad_pos_y]) #Aluse asukoht ekraanil

skoor = 0  # Muutuja skoor saab väärtuseks 0

# Pygame exit
gameover = False  # Muutuja gameover saab väärtuseks False

# Muutuja, et jälgida, kas vasaknooleklahvi hoitakse all
left_key_held = False

# Muutuja, et jälgida, kas paremnooleklahvi hoitakse all
right_key_held = False

while not gameover:  # Juhul kui pole gameover

    # Eventi käsitlemine
    for event in pygame.event.get():
        #Vaatab kas event on x nupu vajutus
        if event.type == pygame.QUIT:
            # Kui vajutatakse x nuppu, siis programm suletakse
            pygame.quit()
            sys.exit()

        # Kontrollib kas nuppu on vajutautd
        elif event.type == pygame.KEYDOWN:
            # Kontrollib kas vasakut noolt on vajutatud
            if event.key == pygame.K_LEFT: # Kui muutuja event.key on võrdeline pygame.K_LEFT
                left_key_held = True  # Muutuja left_key_held saab väärtuse True
            # Kontrollib kas paremat noolt on vajutatud
            elif event.key == pygame.K_RIGHT: # Kui muutuja event.key on võrdeline pygame.K_RIGHT
                right_key_held = True  # Muutuja right_key_held saab väärtuse True
        # Kontrollib kas nupp on lahti lasutd
        elif event.type == pygame.KEYUP:
            # Kontrollib kas vasak nool on lahti lastud
            if event.key == pygame.K_LEFT: # Kui muutuja event.key on võrdeline pygame.K_LEFT
                left_key_held = False  # Muutuja left_key_held saab väärtuse False
            # Kontrollib kas parem nool on lahti lastud
            elif event.key == pygame.K_RIGHT: # Kui muutuja event.key on võrdeline pygame.K_RIGHT
                right_key_held = False  # Muutuja right_key_held saab väärtuse False

    # Uuendab aluse asukohta vasaku ja parema noole vajutuse järgi
    if left_key_held: # Kui vasakut noolt all hoitakse
        pad_pos_x -= 5  # Decrease the paddle's X position by 5 pixels
    if right_key_held: # Kui paremat noolt all hoitakse
        pad_pos_x += 5  # Increase the paddle's X position by 5 pixels

    # Kontrollib, kas alus on jõudnud paremasse äärde
    if pad_pos_x < 0: # Kui pad_pos_x on väiksem kui 0
        pad_pos_x = 0  # Aluse asukoht on 0
    elif pad_pos_x > screenX - alus.get_width():
        pad_pos_x = screenX - alus.get_width()  # Aluse asukohaks saab parem ekraani äär

    # FPS
    clock.tick(60)  # FPS väärtuseks saab 60

    # Uuendab Palli asukohta
    posX1 += speedX1  # Suurendab palli X positsiooni X kiiruse võrra
    posY1 += speedY1  # Suurendab palli Y positsiooni Y kiiruse võrra

    # Kontrollib, kas pall on tabanud paremat või vasakut äärt
    if posX1 < 0 or posX1 > screenX - ball_width:
        speedX1 = -speedX1 # Pöörab X suunda

    # Kontrollib, kas pall on tabanud ülemist või alumist äärt
    if posY1 < 0 or posY1 > screenY - ball_height:
        speedY1 = -speedY1 # Pöörab Y suunda

    # Kontrollib kas pall on tabanud alust
    elif posY1 + ball_height > pad_pos_y and posX1 > pad_pos_x and posX1 < pad_pos_x + alus.get_width():
        speedY1 = -speedY1  # Pöörab Y suunda
        skoor += 1  # Muutuja skoor saab väärtuse + 1

    # Vaatab kas pall on jõudnud ekraani alumisse äärde
    if posY1 > screenY - ball_height:
        gameover = True  # Muutuja gameover saab väärtuse True
        pygame.quit()  # Quit Pygame
        sys.exit()  # Lahkub programmist

    #Fondi loomine
    font = pygame.font.SysFont("Arial", 20) # Muutuja font saab väärtuseks pygame.font.SysFont(fondi nimetus, fondi suurus)
    text = font.render("Skoor: " + str(skoor), True, (0, 0, 0)) # Muutuja text saab väärtuseks font.render("Skoor: " + str(counter), True, (0, 0, 0)) screen.blit(text, (10, 10)) Teksti asetus ekraanil (laius,kõrgus)

    #Tausta uuesti laadmimine
    screen.fill(lBlue)  # Täidab ekraani sinise värviga

    #Pildi lisamine ekraanile
    screen.blit(pall, [posX1, posY1])  # Uuendab palli asukohta ekraanil

    # Balli lisamine ekraanile
    screen.blit(pall, [posX1, posY1]) # Uuendab palli asukohta ekraanil

    # Aluse lisamine ekraanile
    screen.blit(alus, [pad_pos_x, pad_pos_y]) # Uuendab aluse asukohta ekraanil

    # Skoori lisamine ekraanile
    screen.blit(text, (10, 10)) # Uuendab skoori asukohta ekraanil

    pygame.display.flip() #Kuvab lisatud objektid ekraanile



