
# Importando a biblioteca nltk
import nltk

# Baixando o pacote punkt
nltk.download('punkt')

with open('treinamento.txt', mode='r', encoding='utf8') as f:
    treinamento = f.read()


def separa_palavras(lista_tokens):

    # Criando uma lista vazia para armazenar as palavras separadas dos caracteres especiais
    lista_palavras = []

    # Iterando por toda a lista de tokens
    for token in lista_tokens:

        # Separando as palavras dos caracteres especiais
        if token.isalpha():

            # Armazenando somente as palavras
            lista_palavras.append(token)
    
    # Retornando uma lista somente com as palavras
    return lista_palavras

def normalizacao(lista_palavras):
    
    # Criando uma lista vazia para armazenar as palavras normalizadas
    lista_normalizada = []

    # Iterando por toda a lista de palavras
    for palavra in lista_palavras:

        # Armazenando as palavras normalizadas
        lista_normalizada.append(palavra.lower())
    
    # Retornando uma lista com as palavras normalizadas
    return lista_normalizada

lista_tokens = nltk.tokenize.word_tokenize(treinamento)
lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
frequencia = nltk.FreqDist(lista_normalizada)
total_palavras = len(lista_normalizada)

def insere_letras(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Iterando por toda letra das variável letras
        for letra in letras:

            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito)
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

# Função gerador_palavras()
def gerador_palavras(palavra):

    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []

    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):

        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))

    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)

    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas

# Função probabilidade()
def probabilidade(palavra_gerada):

    # Retorna a probabilidade de determinada palavra aparecer no nosso corpus
    return frequencia[palavra_gerada] / total_palavras

def gerador_inception(palavras_geradas):

    # Criando uma nova lista para armazenar as novas palavras
    novas_palavras = []

    # Iterando em cada palavra da lista recebida
    for palavra in palavras_geradas:

        # Chamando a função gerador_palavras() aqui dentro da nova função
            # Por isso o nome gerador_inception()
        novas_palavras += gerador_palavras(palavra)
    
    # Retornando as novas palavras
    return novas_palavras

vocabulario = set(lista_normalizada)

def corretor_super_sayajin(palavra_errada):

    # Chama a função gerador_palavras() usando como parâmetro a palavra 
        # escrita de forma incorreta
    palavras_geradas = gerador_palavras(palavra_errada)

    # Chamando a função gerador_inception() e armazenando o seu retorno
        # em uma variável
    palavras_inception = gerador_inception(palavras_geradas)

    # Juntando todas as palavras geradas
    todas_palavras = set(palavras_geradas + palavras_inception)

    # Criando uma lista para armazenar os possíveis candidatos a palavra 
    candidatos = [palavra_errada]

    # Iterando por todas as palavras geradas pelas duas funções
    for palavra in todas_palavras:

        # Verificando se a palavra já se encontra no vocabulário
        if palavra in vocabulario:

            # Adicionando a palvara a lista de candidatos
            candidatos.append(palavra)

    # Selecionando a palavra com maior probabilidade de aparecer em nosso corpus
        # Essa será a palavra correta
    palavra_correta = max(candidatos, key=probabilidade)

    # Retornando a palavra corrigida
    return palavra_correta






# Digite aqui a sua palavra incorreta
teste = 'carrros'

# Mostrando as respostas dos dois corretores
print(f'Entrada =================> {teste}\nResposta do corretor() ==> {corretor_super_sayajin(teste)}')