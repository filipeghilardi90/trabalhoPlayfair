Cifra de Playfair
Este é um programa Python que implementa a Cifra de Playfair, um método de criptografia que utiliza uma tabela de chave para substituir pares de letras em um texto.

O programa oferece as seguintes funcionalidades:
Criar Tabela de Chave: A função criar_tabela_chave(chave) gera a tabela de chave com base na chave fornecida.
Formatar Texto: A função formatar_texto(texto) formata o texto de entrada, exclui acentos e mantem letras não acentuadas equivalentes e transforma todo texto 
em maiusculas para evitar erros.
Criptografar: A função criptografar(texto, tabela_chave) criptografa o texto de entrada usando a tabela de chave.
Encontrar posição: A função encontrar_posicao(tabela_chave, letra) encontra a posição de uma letra na tabela de chave
Descriptografar: A função descriptografar(texto, tabela_chave) descriptografa o texto de entrada usando a tabela de chave.
Utilização
Para utilizar o programa, execute o arquivo playfair.py e siga as instruções fornecidas no console. Você será solicitado a fornecer o nome do arquivo.txt, a chave 
de cifragem e o modo de operação (criptografar ou descriptografar).
O arquivo.txt a critografado ou decriptografado precisa estar na mesma pasta.

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.
