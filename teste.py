
import speech_recognition as sr
import os

def ouvir_microfone():
    """Função para ouvir e reconhecer a fala"""

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")

            # Mapeia comandos para ações
            comandos = {
                "navegador": "start Chrome.exe",
                "excel": "start Excel.exe",
                # Adicione mais comandos aqui
            }

            if texto.lower() in comandos:
                os.system(comandos[texto.lower()])
            else:
                print("Comando não reconhecido.")

        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError as e:

            print(f"Erro de serviço do Google Speech Recognition; {e}")

if __name__ == "__main__":
    while True:
        ouvir_microfone()
