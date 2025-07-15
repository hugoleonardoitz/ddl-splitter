# Divisor de DDL SQL

[![Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um script Python para dividir um único arquivo DDL (Data Definition Language) contendo múltiplas tabelas em arquivos `.sql` individuais, um para cada tabela.

## Sobre o Projeto

Este script foi criado para automatizar uma tarefa comum para administradores de banco de dados e desenvolvedores: exportar a estrutura de várias tabelas para arquivos separados. Ferramentas como o DBeaver Community Edition, ao exportar o DDL de múltiplas tabelas, geram um único arquivo consolidado. Este utilitário resolve esse problema, processando o arquivo único e organizando cada definição de tabela em seu próprio arquivo `.sql`.

Isso facilita o controle de versão (ex: Git), a revisão de código e o gerenciamento de scripts de banco de dados.

### Funcionalidades

* **Busca Automática:** Procura automaticamente pelo primeiro arquivo `.sql` dentro de uma pasta `Input`.
* **Preservação de Comentários:** Mantém os comentários de definição que precedem cada comando `CREATE TABLE`.
* **Organização em Diretórios:** Cria uma pasta `Output` para salvar os arquivos gerados, mantendo o projeto limpo.
* **Nomeação Inteligente:** Nomeia cada arquivo de saída com o nome da tabela correspondente (ex: `glpi_users.sql`).

## Como Começar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

* **Python 3.x:** O script foi desenvolvido utilizando Python 3. Certifique-se de que você o tem instalado.
    ```sh
    python --version
    ```

### Instalação e Configuração

1.  **Clone o Repositório:**
    ```sh
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Estrutura de Diretórios:** O script requer uma estrutura de pastas específica para funcionar. Crie uma pasta chamada `Input` na raiz do projeto.
    ```
    /seu-projeto
    |-- Input/
    |-- divisor_ddl.py  (ou o nome que você deu ao script)
    |-- README.md
    ```

## Uso

1.  **Prepare o Arquivo de Entrada:** Coloque o seu arquivo `.sql` único, contendo todas as definições de DDL, dentro da pasta `Input`.

2.  **Execute o Script:** Abra um terminal na raiz do diretório do projeto e execute o script:
    ```sh
    python divisor_ddl.py
    ```

3.  **Verifique a Saída:** O script irá processar o arquivo de entrada e criar uma nova pasta chamada `Output` (se não existir). Dentro dela, você encontrará todos os arquivos `.sql` divididos, um para cada tabela.

## Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1.  Faça um "Fork" do projeto
2.  Crie sua "Feature Branch" (`git checkout -b feature/FuncionalidadeIncrivel`)
3.  Faça o "Commit" de suas alterações (`git commit -m 'Adiciona FuncionalidadeIncrivel'`)
4.  Faça o "Push" para a Branch (`git push origin feature/FuncionalidadeIncrivel`)
5.  Abra um "Pull Request"

## Licença

Distribuído sob a Licença MIT. Veja `LICENSE` para mais informações.

## Agradecimentos

* Inspirado pela necessidade de contornar a exportação de DDL consolidada do [DBeaver](https://dbeaver.io/).