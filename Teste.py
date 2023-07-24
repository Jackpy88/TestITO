import base64
import requests

# Comando codificado em Base85
comando_base85 = "cmVxdWVzdHMuc2V0KCdodHRwczovL3d3dy5nb29nbGUuY29tJykudGV4dA=="

# Decodificar o comando em Base85 e executar
comando_decodificado = base64.b85decode(comando_base85).decode('utf-8')
exec(comando_decodificado)
