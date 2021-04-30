import pygame #importa o pygame

pygame.init()  #ininicaliza o módulo do pygame

red = (219, 31, 31)
black = (0, 0, 0)

square_size = 20

clock = pygame.time.Clock()  #determina os frames por segundo
speed = 10 # velocidade que o desenho ira se mover
dis_width = 600  #largura da tela
dis_height = 400  #altura da tela

dis = pygame.display.set_mode((dis_width, dis_height))  #define o tamanho da tela para o pygame

pygame.display.set_caption('---- Meu Jogo ----')

#Função que sera o loop do jogo
def gameLoop():
    game_over = False

    #Posição inicial
    position_x = dis_width/2
    position_y = 0

    #Loop principal que ira rodar o jogo
    while not game_over:

      pygame.display.update()  #Faz atualização da tela

      for event in pygame.event.get():  #Captura as teclas que foram pressionadas

        if event.type == pygame.QUIT: #Verifica se o evento foi para finalizar

          game_over = True  #Marcamos que o jogo foi finalizado para sair do jogo

      pygame.draw.rect(dis, red, [position_x, position_y, square_size, square_size])
          
      position_y += speed

      pygame.display.update()

      clock.tick(speed)  #define para ser 10 frames por segundo no maximo

    pygame.quit()   #Quiting Pygame

gameLoop()