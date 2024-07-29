import re

def criar_tabela_chave(chave):
    chave = re.sub(r'[^a-zA-Z]', '', chave).upper()
    
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    tabela_chave = list(chave)

    for letra in alfabeto:
        if letra not in tabela_chave:
            tabela_chave.append(letra)

    while len(tabela_chave) < 25:
        tabela_chave.append('')

    return tabela_chave


def formatar_texto(texto):
    texto_formatado = texto.upper()
    
    texto_formatado = re.sub(r'[ÁÄÂÀÃ]', 'A', texto_formatado)
    texto_formatado = re.sub(r'[ÉËÊÈ]', 'E', texto_formatado)
    texto_formatado = re.sub(r'[ÍÏÎÌ]', 'I', texto_formatado)
    texto_formatado = re.sub(r'[ÓÖÔÒÕ]', 'O', texto_formatado)
    texto_formatado = re.sub(r'[ÚÜÛÙ]', 'U', texto_formatado)
    texto_formatado = re.sub(r'[Ç]', 'C', texto_formatado)

    return texto_formatado

def encontrar_posicao(tabela_chave, letra):
    posicao = -1

    for i in range(len(tabela_chave)):
        if tabela_chave[i] == letra:
            posicao = i
            break

    return posicao

def criptografar(texto, tabela_chave):

    texto_criptografado = ''
    i = 0
    while i < len(texto):
        if re.match(r'[a-zA-Z]', texto[i]):
            letra1 = texto[i]
            if i+1 < len(texto) and re.match(r'[a-zA-Z]', texto[i+1]):
                letra2 = texto[i+1]
                if texto[i].isupper():
                    tabela_chave_atual = ''.join(tabela_chave).upper()
                else:
                    tabela_chave_atual = ''.join(tabela_chave).lower()
                    
                linha1, coluna1 = divmod(tabela_chave_atual.index(letra1), 5)
                linha2, coluna2 = divmod(tabela_chave_atual.index(letra2), 5)

                if linha1 == linha2:
                    coluna1 = (coluna1 + 1) % 5
                    coluna2 = (coluna2 + 1) % 5
                elif coluna1 == coluna2:
                    linha1 = (linha1 + 1) % 5
                    linha2 = (linha2 + 1) % 5
                else:
                    coluna_temp = coluna1
                    coluna1 = coluna2
                    coluna2 = coluna_temp

                texto_criptografado += tabela_chave_atual[linha1 * 5 + coluna1]
                texto_criptografado += tabela_chave_atual[linha2 * 5 + coluna2]

                i += 2
            else:
                texto_criptografado += letra1
                i += 1
        else:
            texto_criptografado += texto[i]
            i += 1

    return texto_criptografado
   

def descriptografar(texto, tabela_chave):
   
    texto_descriptografado = ''
    i = 0

    while i < len(texto):
        if re.match(r'[a-zA-Z]', texto[i]):
            letra1 = texto[i]
            if i+1 < len(texto) and re.match(r'[a-zA-Z]', texto[i+1]):
                letra2 = texto[i+1]
                if texto[i].isupper():
                    tabela_chave_atual = ''.join(tabela_chave).upper()
                else:
                    tabela_chave_atual = ''.join(tabela_chave).lower()
            
                linha1, coluna1 = divmod(tabela_chave_atual.index(letra1), 5)
                linha2, coluna2 = divmod(tabela_chave_atual.index(letra2), 5)

                if linha1 == linha2:
                    coluna1 = (coluna1 - 1) % 5
                    coluna2 = (coluna2 - 1) % 5
                elif coluna1 == coluna2:
                    linha1 = (linha1 - 1) % 5
                    linha2 = (linha2 - 1) % 5
                else:
                    coluna_temp = coluna1
                    coluna1 = coluna2
                    coluna2 = coluna_temp

                texto_descriptografado += tabela_chave_atual[linha1 * 5 + coluna1]
                texto_descriptografado += tabela_chave_atual[linha2 * 5 + coluna2]

                i += 2
            else:
                texto_descriptografado += letra1
                i += 1
        else:
            texto_descriptografado += texto[i]
            i += 1

    return texto_descriptografado
   

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    return texto

def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(texto)


def main():
    nome_arquivo = input("Digite o nome do arquivo .txt: ")
    modo = input("Digite 'C' para criptografar ou 'D' para descriptografar: ")
    chave = input("Digite a chave para a cifra de Playfair: ")

    texto = ler_arquivo(nome_arquivo)
    tabela_chave_maiusculas = criar_tabela_chave(chave)
    tabela_chave_minusculas = criar_tabela_chave(chave.lower())
    texto_formatado = formatar_texto(texto)

    if modo.upper() == 'C':
        texto_criptografado = criptografar(texto_formatado, tabela_chave_maiusculas)
        nome_arquivo_cripto = nome_arquivo.replace('.txt', '_cripto.txt')
        escrever_arquivo(nome_arquivo_cripto, texto_criptografado)
        print(f"Texto criptografado e salvo no arquivo {nome_arquivo_cripto}.")
    elif modo.upper() == 'D':
        texto_descriptografado = descriptografar(texto_formatado, tabela_chave_maiusculas)
        nome_arquivo_decripto = nome_arquivo.replace('.txt', '_decripto.txt')
        escrever_arquivo(nome_arquivo_decripto, texto_descriptografado)
        print(f"Texto descriptografado e salvo no arquivo {nome_arquivo_decripto}.")
    else:
        print("Modo inválido. Digite 'C' para criptografar ou 'D' para descriptografar.")

if __name__ == '__main__':
    main()



