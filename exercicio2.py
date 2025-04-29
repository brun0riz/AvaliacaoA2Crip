from SHA256.SHA256 import generate_hash

def verificar_auteticidade(hash_original, texto_a_verificar):
    # faremos o mesmo processo de criar uma hash e comparar com a hash original
    hash_a_verificar = generate_hash(texto_a_verificar)
    
    # comparando as duas hashes
    if hash_original == hash_a_verificar:
        return True
    else:
        return False

# Aqui se recebe o texto original
texto_original = 'bom dia a todos os tele espectadores'

# Aqui irá se gerar a hash desse texto original, que será a hash de comparação para a autenticidade do texto
hash_original = generate_hash(texto_original)
print(f"Hash Original: {hash_original}")

# iremos receber o texto que será verificado 
texto_a_verificar =  input("Digite o texto a ser verificado: ")
print(f"Texto a ser verificado: {texto_a_verificar}")

# faremos a verificação de autenticidade usando o SHA256
if(verificar_auteticidade(hash_original, texto_a_verificar)):
    print("O texto é autêntico.")
else:
    print("O texto não é autêntico.")

