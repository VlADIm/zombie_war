def level1():
    bg = pygame.image.load("background.png")
    effect = pygame.mixer.Sound('thump.wav')
    score = 0
    count = 0
    pop = 5
    pop1z = 0
    pop2z = 0
    pop3z = -5
    hou = []
    hou2 = []
    clock = pygame.time.Clock()
    crashed = True
    zombieg = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    h2 = house(425, 300, pop2z, 'h2', hou, hou2)
    h = house(240, 550, pop, 'h', hou, hou2)
    h1 = house(50, 300, pop1z, 'h1', hou, hou2)
    h3 = house(240, 100, pop3z, 'h3', hou, hou2)
    houses = [h1,h2,h3]
    houses2 = [h,h1,h2,h3]
    while crashed:
        count += 1
        gdisplay.fill(white)
        gdisplay.blit(bg, (0,0))
        h.update(pop)
        h1.update(pop1z)
        h2.update(pop2z)
        h3.update(pop3z)
        allsprites.add(h1,h2,h,h3)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                crashed = False
        for i in range(len(houses2)):
            stuff = str(houses2[i])
            stuff = stuff.split()
            x = int(stuff[0])
            y = int(stuff[1])
            name = stuff[2]
            i2 = i+1
            if i2 >= 4:
                i2 = 0
            stuff2 = str(houses2[i2])
            stuff2 = stuff2.split()
            x2 = int(stuff[0])
            y2 = int(stuff[1])
            name2 = stuff[2]

            if x+100 > mouse[0] > x and y+200 > mouse[1] > y:
                if click == (1,0,0):
                    hou.append(name)
            if x2+100 > mouse[0] > x2 and y2+200 > mouse[1] > y2 and name in hou:
                if click == (1,0,0):
                    hou2.append(name2)


        if 'h' in hou and 'h2' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb = zombie(350,550, 1, -3,'zombieup.png')
                zombieg.add(zomb)
                allsprites.add(zomb)
                if pop > 1:
                    pop -= 1
        if 'h' in hou and 'h1' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb1 = zombie(180,550, -1, -3, 'zombieup.png')
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                if pop > 1:
                    pop -= 1
        if 'h1' in hou2 and 'h3' in hou:
            if count % 30 == 0 and pop1z > 1:
                zomb2 = zombie(200,300, 1, -3, 'zombieup.png')
                zombieg.add(zomb2)
                allsprites.add(zomb2)
                pop1z -= 1
        if 'h2' in hou2 and 'h3' in hou:
            if count % 30 == 0 and pop2z > 1:
                zomb3 = zombie(360,300, -1, -3, 'zombieup.png')
                zombieg.add(zomb3)
                allsprites.add(zomb3)
                pop2z -= 1

        for i in range(len(houses2)):
            if click == (0,0,1):
                stuff = str(houses2[i])
                stuff = stuff.split()
                name = stuff[2]
                if name in hou:
                    hou.remove(name)
                if name in hou2:
                    hou2.remove(name)

        if pop > 0:
            if count % 60 == 0:
                pop += 1
        if pop1z > 0:
            if count % 60 == 0:
                pop1z += 1
        if pop2z > 0:
            if count % 60 == 0:
                pop2z += 1

        zombieg.update()
        allsprites.draw(gdisplay)
        zombieg.draw(gdisplay)

        for zomb in zombieg:
            for i in houses:
                allsprites.add(h,h1,h2,h3)
                allsprites.remove(h,h1,h2,h3)
                allsprites.remove(zomb)
                allsprites.add(i)
                if pygame.sprite.spritecollide(zomb, allsprites, False):
                    zombieg.remove(zomb)
                    allsprites.remove(zomb)
                    effect.play()
                    if h1 in allsprites:
                        pop1z += 1
                    if h2 in allsprites:
                        pop2z += 1
                    if h3 in allsprites:
                        pop3z += 1
        if pop > 0 and pop1z > 0 and pop2z > 0 and pop3z > 0:
            gdisplay.fill(white)
            return

        font = pygame.font.Font("freesansbold.ttf",20)
        btext= font.render(str(pop), 1,(0,0,0))
        gdisplay.blit(btext, (240, 550))
        btext= font.render(str(pop1z), 1,(0,0,0))
        gdisplay.blit(btext, (50,300))
        btext= font.render(str(pop2z), 1,(0,0,0))
        gdisplay.blit(btext, (425,300))
        btext= font.render(str(pop3z), 1,(0,0,0))
        gdisplay.blit(btext, (240,100))
        pygame.display.flip()

    clock.tick(60)
