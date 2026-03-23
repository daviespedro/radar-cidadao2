import json

print("Lendo arquivo deputados_brutos.json...")

try:
    # 1️⃣ Abrir o arquivo JSON
    nome_arquivo = 'deputados_brutos.json'
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    print("\n--- SUCESSO! Arquivo carregado ---")

    # 2️⃣ Verificar estrutura
    if isinstance(dados, dict) and 'dados' in dados:
        lista = dados['dados']
    elif isinstance(dados, list):
        lista = dados
    else:
        raise ValueError("Formato do JSON não reconhecido")

    # 3️⃣ Mostrar informações
    print(f"\nTotal de registros: {len(lista)}\n")

    # Mostrar alguns dados (evita travar)
    for item in lista[:20]:
        print(item)

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"O arquivo '{nome_arquivo}' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
