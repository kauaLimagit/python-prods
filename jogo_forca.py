import random

palavras = ["casa", "carro", "janela", "porta", "mesa", "cadeira", "computador", "teclado", "mouse", "monitor", "livro", "caneta", "lapis", "borracha", "caderno", "mochila", "escola", "professor", "aluno", "quadro", "cidade", "rua", "avenida", "bairro", "praça", "parque", "jardim", "arvore", "flor", "grama", "sol", "lua", "estrela", "ceu", "nuvem", "chuva", "vento", "tempestade", "neve", "gelo", "fogo", "agua", "terra", "ar", "energia", "luz", "som", "tempo", "dia", "noite", "manha", "tarde", "semana", "mes", "ano", "familia", "pai", "mae", "filho", "filha", "irmao", "irma", "amigo", "amizade", "amor", "felicidade", "tristeza", "raiva", "medo", "coragem", "forca", "paz", "guerra", "historia", "cultura", "arte", "musica", "cinema", "teatro", "jogo", "brinquedo", "bola", "campo", "time", "gol", "corrida", "nadar", "pular", "andar", "correr", "viajar", "aviao", "navio", "onibus", "metro", "bicicleta", "estrada", "caminho", "mapa", "destino", "origem", "trabalho", "empresa", "negocio", "dinheiro", "conta", "banco", "mercado", "loja", "produto", "preco", "valor", "numero", "contar", "somar", "subtrair", "multiplicar", "dividir", "calcular", "resultado", "problema", "solucao", "ideia", "projeto", "plano", "objetivo", "meta", "sucesso", "fracasso", "tentativa", "erro", "acerto", "aprendizado", "conhecimento", "sabedoria", "inteligencia", "mente", "corpo", "saude", "doenca", "remedio", "hospital", "medico", "enfermeiro", "tratamento", "cura", "alimentacao", "comida", "bebida", "agua", "suco", "cafe", "leite", "pao", "arroz", "feijao", "carne", "fruta", "legume", "verdura", "cozinha", "receita", "prato", "talher", "garfo", "faca", "colher", "copo", "prato", "geladeira", "fogao", "microondas", "banheiro", "chuveiro", "toalha", "sabonete", "shampoo", "espelho", "cama", "travesseiro", "cobertor", "sono", "descanso", "acordar", "dormir", "sonho", "realidade", "verdade", "mentira", "duvida", "certeza", "pergunta", "resposta", "linguagem", "palavra", "frase", "texto", "leitura", "escrita", "fala", "ouvir", "ver", "olhar", "sentir", "pensar", "agir", "viver", "existir"]
escolha = palavras[random.randint(0, (len(palavras)-1))]
culto = []
palavra_completa = ''

def devide():
    print('---------------------------------------------------')

for i in escolha:
    culto.append('_')

devide()
print(culto)
devide()
  
while True:
        num = 0
        pergunta = str(input("Escolha sua letra:"))
        
        for l in escolha:
            if pergunta == l and culto[num] == '_':
                culto[num] = l
                num+=1
            else:
                num+=1
                
        
                        
        for i in culto:
            palavra_completa += i + ' '
        
        if '_' not in palavra_completa:
            devide()
            print(f'parabens você encontrou a palavra escondida -> {palavra_completa} <-')
            devide()
            break
        
        devide()
        print(palavra_completa)
        devide()
        
        palavra_completa = ''