# Para conseguir acessar o sistema operacional
import os

# Para o chatbot
from chatterbot import ChatBot

# Para treinar o chatbot
from chatterbot.trainers import ListTrainer

# Para criar os statements das frases
from chatterbot.conversation import Statement

# Para o uso de Regular Expressions
import re

# Para ter o módulo de pegar respostas
import pegar_resposta as pr

# Para importa o reconhecimento de áudio
import reconhecimento_fala as rf


##----------Configuração dos chatbots-----------##
##||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||##
##\/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/##

#Configura o chatbot em si
bocasus = ChatBot(

	'BOCASUS',

	storage_adapter='chatterbot.storage.SQLStorageAdapter',

	database_uri='sqlite:///database.sqlite3',

    logic_adapter='chatterbot.logic.BestMatch'

)

#Define todas as respostas já predefinidas
respostas_bocasus = [

    'Olá, em como posso ajudar?',

    'E qual seria a natureza da consulta?',

	'Qual seria a consulta a ser desmarcada?',

	'Abrindo agenda de consultas...'

]

#Define os possíveis diálogos entre o paciente e o bot
conversas = [
	#Cumprimentos
	['oi', respostas_bocasus[0]],
	['olá', respostas_bocasus[0]],
	['oie', respostas_bocasus[0]],
	['hey', respostas_bocasus[0]],
	['alo', respostas_bocasus[0]],
	['bomdia', respostas_bocasus[0]],
	['boatard', respostas_bocasus[0]],
	['boanoit', respostas_bocasus[0]],
	['meucumpr', respostas_bocasus[0]],

	#Marcar consulta
	['quermarc', respostas_bocasus[1]],
	['marcconsult', respostas_bocasus[1]],
	['quermarcconsult', respostas_bocasus[1]],
	['gostmarc', respostas_bocasus[1]],
	['gostmarcconsult', respostas_bocasus[1]],
	['queragend', respostas_bocasus[1]],
	['agendconsult', respostas_bocasus[1]],
	['queragendconsult', respostas_bocasus[1]],
	['gostagend', respostas_bocasus[1]],
	['gostagendconsult', respostas_bocasus[1]],
	['querprogram', respostas_bocasus[1]],
	['programconsult', respostas_bocasus[1]],
	['querprogramconsult', respostas_bocasus[1]],
	['gostprogram', respostas_bocasus[1]],
	['gostprogramconsult', respostas_bocasus[1]],
	['querfaz', respostas_bocasus[1]],
	['fazconsult', respostas_bocasus[1]],
	['querfazconsult', respostas_bocasus[1]],
	['gostfaz', respostas_bocasus[1]],
	['gostfazconsult', respostas_bocasus[1]],

	#Desmarcar uma consulta
	['gostdesmarc', respostas_bocasus[2]],
	['gostdesmarcconsult', respostas_bocasus[2]],
	['querdesmarcconsult', respostas_bocasus[2]],
	['querdesmarc', respostas_bocasus[2]],
	['desmarc', respostas_bocasus[2]],
	['desmarcconsult', respostas_bocasus[2]],

	#Ver a agenda
	['veragend', respostas_bocasus[3]],
	['abragend', respostas_bocasus[3]],
	['veragendconsult', respostas_bocasus[3]],
	['abragendconsult', respostas_bocasus[3]],
	['verconsult', respostas_bocasus[3]],
	['veragendconsultmarc', respostas_bocasus[3]],
	['abragendconsultmarc', respostas_bocasus[3]],
	['verconsultmarc', respostas_bocasus[3]],
	['verconsultagend', respostas_bocasus[3]],
	['consultmarc', respostas_bocasus[3]],
	['consultagend', respostas_bocasus[3]],
	['abrconsultmarc', respostas_bocasus[3]],
	['abrconsult', respostas_bocasus[3]],
	['abrhorarimarc', respostas_bocasus[3]],
	['verhorarimarc', respostas_bocasus[3]],
	['abrhormarc', respostas_bocasus[3]],
	['verhormarc', respostas_bocasus[3]]
]

#Cria um novo objeto do tipo ListTrainer para treinar o bocasus com as palavras acima
professor = ListTrainer(bocasus)

#Treina o bot com a lista de diálogos em um loop para pegar todas as listas da matriz
for x in conversas:

	professor.train(x)

##/\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\##
##||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||##
##----------Configuração dos chatbots-----------##



##------Loop onde vai acontecer a conversa------##
##||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||##
##\/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/##

# Define cada número da lista respostas_bocasus para seu respectivo valor
fun = {'0':'conversa', '1':'marcar', '2':'desmarcar', '3':'agenda'}

# Loop da conversa
while True:

	try:

    	##---------------------------------------------------------------------##
    	## Fazer o bot conseguir lidar com mais de uma mensagem no mesmo input ##
    	##---------------------------------------------------------------------##

		# Determina o curso da conversa e o que o paciente quer fazer
		dic = {'conversa':False, 'marcar':False, 'desmarcar':False, 'agenda':False}
		
		# Envia o input do usuário para a função de pegar a resposta
		resp_final, funcao = [x for x in pr.pegarResposta(bocasus, rf.ouvir_microfone(), dic, fun, respostas_bocasus)]

		# Printa a resposta e recomeça o loop
		resposta = "espeak -s 200 -vpt '" + resp_final + "'"
		os.system(resposta)

		# Quando o paciente engaja em uma função, o bot fica sabendo
		if funcao == 'aprender' or funcao == 'conversa':

			continue

		else:

			dic[funcao] = True

			if dic['marcar']:

				engaj = 'marcar'

			elif dic['desmarcar']:

				engaj = 'desmarcar'

			elif dic['agenda']:

				engaj = 'agenda'

	except (KeyboardInterrupt, EOFError, SystemExit):

		break