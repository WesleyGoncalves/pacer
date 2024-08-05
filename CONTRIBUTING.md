# CONTRIBUTING

## Requisitos Adicionais

Além dos requisitos para executar a aplicação (veja [README](./README.md)), você precisará das seguintes programas instalados:

- [NodeJS](https://nodejs.org/en) com NPM

## Instalação

Siga os passos em [README](./README.md) com os passos adicionais abaixo:

1. No passo de Instalação das dependências, execute:

     ```sh
     npm install
     ```

2. No passo de Configuração das Variáveis de Ambiente, edite as variáveis para ativar o modo de desenvolvimento.

    ```sh
    FLASK_ENV=developement
    FLASK_DEBUG=1
    ```

---

npm run watch   # will watch the sass files for changes. The CSS files will also be compiled and minimized
