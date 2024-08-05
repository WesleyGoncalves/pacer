# PACER

*Avaliação PACER de maneira ágil e descomplicada*.

Esta ferramenta visa tornar a autoavaliação PACER uma tarefa simples e fácil de ser executada, garantindo que você e seu time possam identificar pontos fortes e oportunidades de crescimento nos princípios de Proatividade, Autonomia, Colaboração e Entrega de Resultados.

## Requisitos

Você precisará das seguintes programas instalados:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/WesleyGoncalves/pacer.git
    ```

2. Navegue até o projeto

    ```sh
    cd pacer
    ```

3. Indicamos o uso de um ambiente virtual, como o [venv](https://docs.python.org/3/library/venv.html)

    ```sh
    python -m venv venv

    # Windows - ative o ambiente
    source venv/Scripts/activate

    # Linux - ative o ambiente
    . venv/bin/activate

    # Mac - ative o ambiente
    source venv/bin/activate
    ```

4. Instale as dependências

    ```sh
    pip install -r requirements.txt
    ```

5. Configure as variáveis de ambiente

    ```sh
    cp .env.template .env
    ```

    Abra o arquivo `.env` e edite as credenciais de conexão com o banco de dados.

    ```sh
    # ...
    DB_HOST=   # database host
    DB_USER=   # database user
    DB_PASS=   # database password
    DB_NAME=   # database name

    ```

   1. Configura o token que será usado pelo sistema de Autenticação de Usuários.

      ```sh
      # Session secret key for Authentication system
      python -c 'import secrets; print(secrets.token_hex())'
      ```

      Copie o token mostrado e preencha na variável `FLASK_SECRET_KEY` no arquivo `.env`.

6. Crie o banco de dados e as tabelas automaticamente rodando o script em `database_create.py`

    ```sh
   python database_create.py
    ```

   1. Opcionalmente, você pode executar os comandos SQL em `database_seed.sql` diretamente no Banco de Dados para testes

7. Execute o servidor Flask

    ```sh
    flask run
    ```

8. Abra em um navegador: [http://localhost:5000](http://localhost:5000)
