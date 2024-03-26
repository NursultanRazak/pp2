import pygame;

pygame.init();

pygame.mixer.music.load('')
pygame.mixer.music.play(0);

sc = pygame.display.set_mode((200, 100));

clock = pygame.time.Clock()

pause = False;
vol = 1.0;
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause;
                if pause:
                    pygame.mixer.music.pause();
                else:
                    pygame.mixer.music.unpause();
            elif event.key == pygame.K_LEFT:
                vol -= 0.1;
                pygame.mixer.music.set_volume(vol);
            elif event.key == pygame.K_RIGHT:
                vol += 0.1;
                pygame.mixer.music.set_volume(vol);


    pygame.display.update();

    clock.tick(60)