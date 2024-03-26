import pygame;

pygame.init();

W, H = 700, 700;


sc = pygame.display.set_mode((W, H));
sc.fill((255, 255, 255))

FPS = 60
clock = pygame.time.Clock()

x = W//2;
y = H//2;
speed = 20;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x>30:
                x -= speed;
            elif event.key == pygame.K_RIGHT and x<670:
                x += speed;
            elif event.key == pygame.K_DOWN and y<670:
                y += speed;
            elif event. key == pygame.K_UP and y>30:
                y -= speed;
    sc.fill((255, 255, 255))
    circle = pygame.draw.circle(sc, (255, 0, 0), (x, y), 25)
    pygame.display.update();

    clock.tick(FPS)