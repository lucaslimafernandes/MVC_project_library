# Projeto Library Flask - MVC

Projeto com o design pattern Model, View e Controller

## O que foi usado neste projeto?  

    - Python 3

    - Flask

    - MongoDB (running in a Docker container)

    - Oracle Cloud Infrastructure (Instância Linux Ubuntu 22.04)


## O que é o projeto?

O projeto é um sistema simples de biblioteca aberta ao público.

Possui as seguintes funções:

    - Exibir usuários

    - Adicionar usuário

    - Exibir livros

    - Adicionar livros

    - Vincular leitura de livro a usuário


Funções a adicionar:

    - Exibir livros lidos pelo usuário

    - Sistema de empréstimo de livros

    - Relacionamentos entre categorias de livros

    - Avalição dos livros pelos usuários

    - Recomendações de livros para os usuários


## Como executar

Os passos abaixos, foram todos executados em linux.

1. Clonar o repositório:

    > git clone https://github.com/lucaslimafernandes/MVC_project_library.git

2. Configurar a virtual environment(venv) Python:

        > python3 -m venv venv

        > source venv/bia/activate

        > python -m pip install --upgrade pip

        > pip install -r requirements.txt

3. Preencher o arquivo modelo_settings.py com seus dados e renomear para settings.py

4. Configurar o MongoDB:

    Obs.: Talvez necessário usar sudo para executar os comandos

    4.1. Criar um container Docker usando a imagem de mongo

        > docker container run --name mydatabase --publish 27017:27017 -d mongo
    
    4.2. Acessar:

        > docker container exec -it mydatabase bash

    4.3. Iniciar o mongo:

        > mongo ou talvez mongosh
    
    4.4. Criar a database:

        > use mydbone
    
    4.5 Criar o usuário de acesso:

        > db.createUser({ user: "username", pwd: "password", roles: [] })
    
    Para estes passos, foi utilizado o artigo no [medium de Anuradh](https://medium.com/@anuradhs/how-to-start-a-mongo-database-with-authentication-using-docker-container-8ce63da47a71)

5. Rodar o projeto localmente

        > flask --app main run

    Ainda não executado em um servidor, mas será o próximo passo



## Referências

https://medium.com/@anuradhs/how-to-start-a-mongo-database-with-authentication-using-docker-container-8ce63da47a71

