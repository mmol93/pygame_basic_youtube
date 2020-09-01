import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("Background.png")

# 케릭터 불러오기
chracter = pygame.image.load("character.png")
chracter_size = chracter.get_rect().size    # 그림의 크기 가져오기
chracter_width = chracter_size[0]   #케릭터의 가로크기
chracter_height = chracter_size[1]  #케릭터의 세로크기
chracter_x_pos = screen_width / 2 - chracter_width / 2   # 화면 가로의 절반 크기에 해당하는 곳에 위치
chracter_y_pos = screen_height - chracter_height      # 화면 세로의 제일 아래에

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(chracter, (chracter_x_pos, chracter_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()