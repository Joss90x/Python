import pygame
pygame.init()
pygame.mixer.music.load('thecyber.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
# Arquivos .m4a não são suportados nativamente pelo pygame
# Você precisa converter o arquivo para .mp3 ou .wav primeiro

# Algumas opções para converter:
# 1. Use sites online de conversão como convertio.co
# 2. Use o VLC Media Player: Mídia > Converter
# 3. Use o comando ffmpeg no PowerShell:
#    ffmpeg -i arquivo.m4a arquivo.mp3

# Depois de converter para .mp3 ou .wav, atualize o código com o novo arquivo:
# pygame.mixer.music.load('arquivo.mp3')


# O código está correto, mas podem ter alguns motivos para não funcionar:

# 1. Verifique se o arquivo 'thecyber.mp3' existe na mesma pasta do script
# 2. Verifique se o nome do arquivo está escrito exatamente igual, incluindo maiúsculas/minúsculas
# 3. Certifique-se que o pygame está instalado corretamente. Para instalar, use no PowerShell:
#    pip install pygame
# 4. Se estiver usando arquivo .m4a ou outro formato, converta para .mp3 primeiro
# 5. Tente usar o caminho completo do arquivo, exemplo:
#    pygame.mixer.music.load('C:/Users/SeuUsuario/Musica/thecyber.mp3')

# Para testar se está funcionando, você pode tentar com outro arquivo .mp3
# Ou adicionar um print para ver se há erros:
print("AEEEE CARALHOOO! VOCÊ CONSEGUIU!")
print("Tá vendo? Quando a gente se esforça, dá certo!")
print("Continue assim, você tá mandando muito bem! 🚀")