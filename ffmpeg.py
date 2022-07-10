import fnmatch
import os
import sys

# comando windows r'ffmpeg/ffmpeg.exe'
comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
codec_audio = '-crf 23'
crf = '-preset ultrafast'
preset = '-c:a aac'
bit_rate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'         #Caso deseje alterar as configurações, basta editar.

caminho_origem = r'C:\Users'
caminho_destino = r'C:\Users'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        arquivo_saida = f'{caminho_destino}\{nome_arquivo}_NOVO{extensao_arquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bit_rate_audio} {debug} {map_legenda}"{arquivo_saida}"'

        os.system(comando)
