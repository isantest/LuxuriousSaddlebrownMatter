import pygame #importa o pygame

pygame.init()  #ininicaliza o módulo do pygame

dis_width = 600  #largura da tela
dis_height = 400  #altura da tela

dis = pygame.display.set_mode((dis_width, dis_height))  #define o tamanho da tela para o pygame

red = (219, 31, 31)
green = (44, 219, 31)

square_size = 20
circle_radius = 10

position_x = 200
position_y = 100

#Função que sera o loop do jogo
def gameLoop():
    game_over = False

    #Loop principal que ira rodar o jogo
    while not game_over:

      pygame.display.update()  #Faz atualização da tela

      for event in pygame.event.get():  #Captura as teclas que foram pressionadas

        if event.type == pygame.QUIT: #Verifica se o evento foi para finalizar

          game_over = True  #Marcamos que o jogo foi finalizado para sair do jogo

      pygame.draw.rect(dis, red, [position_x, position_y, square_size, square_size])
          
      pygame.draw.circle(dis, green,(position_x + 200, position_y), circle_radius)    

    pygame.quit()   #Quiting Pygame

gameLoop()