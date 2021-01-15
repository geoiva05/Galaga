def open_the_shop():
    running = True

    shop_text = pygame.font.SysFont('Consolas', 32).render('Магазин', True, pygame.color.Color('White'))

    fl1 = 0
    fl2 = 0
    fl3 = 0
    fl4 = 0
    flag1 = 0
    flag2 = 0

    galaxy_group = pygame.sprite.Group()

    galaxy = galaxy_generator(galaxy_group)

    galaxy_group.draw(screen)
    galaxy_group.update()

    fps = 60
    clock = pygame.time.Clock()

    pygame.display.flip()

    while running:
        screen.blit(shop_text, (350, 200))

        skin_button = pygame.draw.rect(screen, (255, 255, 255), (260, 250, 310, 50))
        skin_game_text = pygame.font.SysFont('Consolas', 32).render('Покупка скина', True,
                                                                        pygame.color.Color('Black'))
        screen.blit(skin_game_text, (265, 260))

        hp_button = pygame.draw.rect(screen, (255, 255, 255), (260, 330, 310, 50))
        hp_game_text = pygame.font.SysFont('Consolas', 32).render('Покупка здоровья', True,
                                                                     pygame.color.Color('Black'))
        screen.blit(hp_game_text, (265, 340))

        damage_button = pygame.draw.rect(screen, (255, 255, 255), (260, 410, 310, 50))
        damage_game_text = pygame.font.SysFont('Consolas', 32).render('Покупка урона', True,
                                                                    pygame.color.Color('Black'))
        screen.blit(damage_game_text, (265, 420))

        ex_button = pygame.draw.rect(screen, (255, 255, 255), (260, 490, 310, 50))
        ex_game_text = pygame.font.SysFont('Consolas', 32).render('Выйти из магазина', True,
                                                                    pygame.color.Color('Black'))
        screen.blit(ex_game_text, (265, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 250):
                    if (pygame.mouse.get_pos()[0] <= 570) and (pygame.mouse.get_pos()[1] <= 300):
                        fl1 = 1

                if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 330):
                    if (pygame.mouse.get_pos()[0] <= 570) and (pygame.mouse.get_pos()[1] <= 380):
                        fl2 = 1

                if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 410):
                    if (pygame.mouse.get_pos()[0] <= 570) and (pygame.mouse.get_pos()[1] <= 460):
                        fl3 = 1

                if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 490):
                    if (pygame.mouse.get_pos()[0] <= 560) and (pygame.mouse.get_pos()[1] <= 540):
                        fl4 = 1

        if fl1 == 1:
            screen.fill('Black')
            screen.blit(shop_text, (350, 200))

            if flag1 == 0:
                skin1_button = pygame.draw.rect(screen, (255, 255, 255), (200, 250, 505, 50))
                skin1_game_text = pygame.font.SysFont('Consolas', 32).render('Millennium Falcon: выбран', True,
                                                                             pygame.color.Color('Black'))
                screen.blit(skin1_game_text, (205, 260))

                skin2_button = pygame.draw.rect(screen, (255, 255, 255), (200, 330, 505, 50))
                skin2_game_text = pygame.font.SysFont('Consolas', 32).render('X-Wing: купить', True,
                                                                             pygame.color.Color('Black'))
                screen.blit(skin2_game_text, (205, 340))

            elif flag1 == 1:
                if flag2 == 0:
                    skin1_button = pygame.draw.rect(screen, (255, 255, 255), (200, 250, 505, 50))
                    skin1_game_text = pygame.font.SysFont('Consolas', 32).render('Millennium Falcon: выбран', True,
                                                                                 pygame.color.Color('Black'))
                    screen.blit(skin1_game_text, (205, 260))

                    skin2_button = pygame.draw.rect(screen, (255, 255, 255), (200, 330, 505, 50))
                    skin2_game_text = pygame.font.SysFont('Consolas', 32).render('X-Wing: не выбран', True,
                                                                                 pygame.color.Color('Black'))
                    screen.blit(skin2_game_text, (205, 340))
                else:
                    skin1_button = pygame.draw.rect(screen, (255, 255, 255), (200, 250, 505, 50))
                    skin1_game_text = pygame.font.SysFont('Consolas', 32).render('Millennium Falcon: не выбран', True,
                                                                                 pygame.color.Color('Black'))
                    screen.blit(skin1_game_text, (205, 260))

                    skin2_button = pygame.draw.rect(screen, (255, 255, 255), (200, 330, 505, 50))
                    skin2_game_text = pygame.font.SysFont('Consolas', 32).render('X-Wing: выбран', True,
                                                                                 pygame.color.Color('Black'))
                    screen.blit(skin2_game_text, (205, 340))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pos()[0] >= 200) and (pygame.mouse.get_pos()[1] >= 250):
                        if (pygame.mouse.get_pos()[0] <= 705) and (pygame.mouse.get_pos()[1] <= 300):
                            if flag1 == 1:
                                flag2 = 0

                    if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 330):
                        if (pygame.mouse.get_pos()[0] <= 705) and (pygame.mouse.get_pos()[1] <= 380):
                            flag1 = 1
                            flag2 = 1

                    if (pygame.mouse.get_pos()[0] >= 260) and (pygame.mouse.get_pos()[1] >= 410):
                        if (pygame.mouse.get_pos()[0] <= 705) and (pygame.mouse.get_pos()[1] <= 460):
                            pass

            e_button = pygame.draw.rect(screen, (255, 255, 255), (200, 410, 505, 50))
            e_game_text = pygame.font.SysFont('Consolas', 32).render('Назад', True,
                                                                          pygame.color.Color('Black'))
            screen.blit(e_game_text, (205, 420))

        pygame.display.flip()

        clock.tick(fps)
