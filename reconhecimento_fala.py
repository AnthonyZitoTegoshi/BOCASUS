
# Para ouvir e entender
import speech_recognition as sr

# Função que transcreve o áudio para texto e retorna o valor
def ouvir_microfone():

	microfone = sr.Recognizer()

	with sr.Microphone() as source:

		microfone.adjust_for_ambient_noise(source)

		print("Diga alguma coisa: ")

		audio = microfone.listen(source)

	try:

		frase = microfone.recognize_google(audio,language='pt-BR')

	except sr.UnknownValueError:

		frase = ''
	
	return frase