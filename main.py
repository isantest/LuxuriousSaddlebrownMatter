import pygame #importa o pygame

pygame.init()  #ininicaliza o módulo do pygame

dis_width = 600  #largura da tela
dis_height = 400  #altura da tela

dis = pygame.display.set_mode((dis_width, dis_height))  #define o tamanho da tela para o pygame

pygame.display.set_caption('Meu jogo')  # Define o titulo que aparecerá na janela

#Função que sera o loop do jogo
def gameLoop():
    game_over = False

    #Loop principal que ira rodar o jogo
    while not game_over:

      for event in pygame.event.get():  #Captura as teclas que foram pressionadas

        if event.type == pygame.QUIT: #Verifica se o evento foi para finalizar

          game_over = True  #Marcamos que o jogo foi finalizado para sair do jogo

    pygame.quit()

gameLoop()