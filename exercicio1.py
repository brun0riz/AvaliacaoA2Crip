from SHA256.SHA256 import generate_hash

TABELA_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def criptografar(string):
    binario = ''.join(format(ord(c), '08b') for c in string)
    
    # Preencher até múltiplo de 6
    while len(binario) % 6 != 0:
        binario += '0'

    grupos = [binario[i:i+6] for i in range(0, len(binario), 6)]
    indices = [int(grupo, 2) for grupo in grupos]
    base64_str = ''.join(TABELA_BASE64[i] for i in indices)

    while len(base64_str) % 4 != 0:
        base64_str += '='
    
    return base64_str

def descriptografar(texto_codificado):
    texto_codificado = texto_codificado.replace('=', '')
    indices = [TABELA_BASE64.index(c) for c in texto_codificado]
    binario = ''.join(format(i, '06b') for i in indices)

    # Dividir em grupos de 8 bits e remover qualquer byte inválido
    grupos = [binario[i:i+8] for i in range(0, len(binario), 8)]
    texto = ''
    for grupo in grupos:
        if len(grupo) == 8:
            texto += chr(int(grupo, 2))
    return texto

def verificar_autenticidade(texto_original, texto_decodificado):
    hash_original = generate_hash(texto_original)
    hash_decodificado = generate_hash(texto_decodificado)
    
    print(f"Hash Original: {hash_original}")
    print(f"Hash Decodificado: {hash_decodificado}")
    
    return hash_original == hash_decodificado

def menu():
    opcao = 0
    texto = ''
    texto_criptografado = ''
    texto_decodificado = ''

    while opcao != 4:
        print("\nEscolha uma opção:")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Verificar autenticidade")
        print("4 - Sair")
        
        opcao = int(input("Digite sua opção: "))
        
        if opcao == 1:
            texto = input("Digite o texto a ser criptografado: ")
            texto_criptografado = criptografar(texto)
            print(f"Texto criptografado: {texto_criptografado}")
        
        elif opcao == 2:
            if not texto_criptografado:
                print("Primeiro você precisa criptografar um texto.")
                continue
            texto_decodificado = descriptografar(texto_criptografado)
            print(f"Texto decodificado: {texto_decodificado}")
        
        elif opcao == 3:
            if not texto or not texto_decodificado:
                print("Você precisa criptografar e descriptografar antes de verificar.")
                continue
            if verificar_autenticidade(texto, texto_decodificado):
                print("O texto codificado é autêntico.")
            else:
                print("O texto codificado não é autêntico.")
        
        elif opcao == 4:
            print("Saindo...")
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
