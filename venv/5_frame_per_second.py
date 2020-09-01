import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS 설정
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("Background.png")

# 케릭터 불러오기
chracter = pygame.image.load("character.png")
chracter_size = chracter.get_rect().size    # 그림의 크기 가져오기
chracter_width = chracter_size[0]   #케릭터의 가로크기
chracter_height = chracter_size[1]  #케릭터의 세로크기
chracter_x_pos = screen_width / 2 - chracter_width / 2   # 화면 가로의 절반 크기에 해당하는 곳에 위치
chracter_y_pos = screen_height - chracter_height      # 화면 세로의 제일 아래에

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
chracter_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #dt = delta를 의미, 숫자는 프레임수를 의미

    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= chracter_speed
            elif event.key == pygame.K_RIGHT:
                to_x += chracter_speed
            elif event.key == pygame.K_DOWN:
                to_y += chracter_speed
            elif event.key == pygame.K_UP:
                to_y -= chracter_speed
        if event.type == pygame.KEYUP: #방향키에서 손뗌
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    chracter_x_pos += to_x * dt
    chracter_y_pos += to_y * dt

    # 가로 경계값 처리
    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos = screen_width - chracter_width

    # 세로 경계값 처리
    if chracter_y_pos < 0:
        chracter_y_pos = 0
    elif chracter_y_pos > screen_height - chracter_height:
        chracter_y_pos = screen_height - chracter_height

    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(chracter, (chracter_x_pos, chracter_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()