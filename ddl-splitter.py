import os
import re

def dividir_ddl_em_arquivos():
    """
    Busca por um arquivo .sql no diretório 'Input',
    e divide as declarações CREATE TABLE em arquivos
    separados no diretório 'Output', mantendo os comentários.
    """
    # Define os diretórios de entrada e saída baseados na localização do script
    try:
        # __file__ está disponível quando o script é executado como um arquivo
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Fallback para o diretório de trabalho atual se executado interativamente
        script_dir = os.getcwd()

    input_dir = os.path.join(script_dir, 'Input')
    output_dir = os.path.join(script_dir, 'Output')

    # 1. Verificar e encontrar o arquivo .sql de entrada
    if not os.path.isdir(input_dir):
        print(f"Erro: O diretório 'Input' não foi encontrado em '{script_dir}'.")
        print("Por favor, crie uma pasta chamada 'Input' e coloque seu arquivo .sql dentro dela.")
        return

    arquivo_sql_entrada = None
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.sql'):
            arquivo_sql_entrada = os.path.join(input_dir, filename)
            print(f"Arquivo de entrada encontrado: {filename}")
            break

    if not arquivo_sql_entrada:
        print(f"Erro: Nenhum arquivo com extensão .sql foi encontrado no diretório 'Input'.")
        return

    # 2. Criar o diretório de saída
    os.makedirs(output_dir, exist_ok=True)

    # 3. Ler o conteúdo do arquivo e processá-lo
    try:
        with open(arquivo_sql_entrada, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Nova lógica de divisão:
        # Divide o texto no final de cada instrução (';' seguido por quebra de linha)
        # somente se for seguido por um comentário (--) ou outro CREATE TABLE.
        # O 'lookahead' (?=...) garante que o delimitador não seja consumido.
        padrao_split = r';\s*\n(?=--\s*\w|CREATE TABLE)'
        scripts_tabela = re.split(padrao_split, conteudo, flags=re.IGNORECASE)

        if not scripts_tabela or len(scripts_tabela) <= 1:
            print("\nNão foi possível dividir o arquivo. Verifique se há múltiplas tabelas no formato esperado.")
            return

        print(f"\nIniciando a separação de {len(scripts_tabela)} tabelas...")
        contador_arquivos = 0

        for i, script_parcial in enumerate(scripts_tabela):
            script = script_parcial.strip()
            if not script:
                continue

            # Adiciona o ';' de volta, exceto para o último item se ele não precisar.
            if i < len(scripts_tabela) - 1:
                script += ';'

            # Extrai o nome da tabela para usar como nome do arquivo
            match = re.search(r'CREATE TABLE\s+`?([\w\._-]+)`?', script, re.IGNORECASE)

            if match:
                nome_tabela = match.group(1).replace('`', '')
                nome_arquivo_saida = f"{nome_tabela}.sql"
                caminho_arquivo_saida = os.path.join(output_dir, nome_arquivo_saida)

                with open(caminho_arquivo_saida, 'w', encoding='utf-8') as out_f:
                    out_f.write(script)
                print(f"  -> DDL da tabela '{nome_tabela}' salvo em: {nome_arquivo_saida}")
                contador_arquivos += 1

        if contador_arquivos > 0:
            print(f"\nProcesso concluído! {contador_arquivos} arquivos DDL foram gerados no diretório 'Output'.")
        else:
            print("\nNenhuma declaração 'CREATE TABLE' válida foi encontrada no arquivo de entrada.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_sql_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Ponto de entrada do script
if __name__ == '__main__':
    dividir_ddl_em_arquivos()