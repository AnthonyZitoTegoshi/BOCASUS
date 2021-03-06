
# Para processamento de linguagem natural
import nltk

# Para todos os tipos de pontuação que serão irrelevantes
from string import punctuation

# Para o uso de Regular Expressions
import re

# Baixar todas as partes do nltk para o PLN
nltk.download('all')

#Inicia os transformadores de input da nltk
tokenizador = nltk.WhitespaceTokenizer()

radicalizador = nltk.RSLPStemmer()

stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))

# Função que pega o input do usuário e escolhe a melhor resposta
def pegarResposta(bot, frase, dic, fun, respostas_bocasus, default):

    frase = tokenizador.tokenize(re.sub('[.,:;]+', '', frase))

    resp_final = default

    countfun = {'conversa':0, 'marcar':0, 'desmarcar':0, 'agenda':0}

    funcao = 'aprender'

    palavras_sem_stopwords = [palavra for palavra in frase if palavra not in stopwords]

    palavras_radicalizadas = []

    for palavra in palavras_sem_stopwords:

        palavras_radicalizadas.append(radicalizador.stem(palavra))
  
    comb = []

    for i in range(1, len(palavras_radicalizadas) + 1):

        comb.append(list(nltk.ngrams(palavras_radicalizadas, i)))

    max = 0

    for i in range(len(comb)):

        for gram in range(len(comb[i])):

            f = ''

            for p in comb[i][gram]:

                f += p

            resp = bot.get_response(f)
            print(f)
            
            while respostas_bocasus.count(resp.text) < 1 and resp.text != default:

                resp = bot.get_response(f)

            if resp.text != default:

                index = respostas_bocasus.index(resp.text)

                countfun[fun[str(index)]] += resp.confidence

                if countfun[fun[str(index)]] > max:

                    resp_final = resp.text

                    max = countfun[fun[str(index)]]

                    funcao = fun[str(index)]

    return resp_final, funcao