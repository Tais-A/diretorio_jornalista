# Diretório Nacional de Jornalistas

## Tecnologias Utilizadas

- Python Python 3.8.10
- Django 4.0.5
- postgres (PostgreSQL) 14.1 (Debian 14.1-1.pgdg110+1)
## Testes

## Execução (Windows)

1. Criar e ativar o ambiente virtual:

    ```python -m venv nome_do_ambiente```

    ```nome_do_ambiente\Scripts\activate ```

2. Crie um arquivo chamado ".env" de acordo com o template localizado em /aplicacao/autenticacao/.env.template.

    É necessário ter o postgresql instalado e um banco de dados criado.

3. Instalar as dependências no ambiente:

    ```pip install -r requirements.txt```

4. Rode a migração dos dados.

    ```python manage.py makemigrations```

    ```python manage.py migrate```

5. Execute o projeto

    ```python manage.py runserver```


###### No docker
- Necessário configurar o arquivo `.env` a partir do arquivo exemplo `env.example`
- Necessário configurar os dados de acesso do banco de dados postgres no `.env` 
- `docker-compose up -d`

###### Localmente
- Necessário configurar o arquivo `.env` a partir do arquivo exemplo `env.example`
- Necessário configurar os dados de acesso do banco de dados postgres no .env 
- Instalar `venv` com python Python 3.8.10
- Instalar requirements
  - `pip install -r requirements.txt`
- Executar migrações
  - `python manage.py migrate`
- executar o projeto com `python manage.py runserver`


## Usage
## Support

## Roadmap
## Contributing
## Authors and acknowledgment
## License

## Project status
=======
# Diretório Piloto de Jornalistas no Brasil.

## Sprint 1

Durante a disciplina de Jornalismo Digital foi feito:

* Prototipação no Figma da página inicial, página de cadastro de jornalista e página do revisor. [Link do Figma](https://www.figma.com/file/4ap6riA5XxfGb6byJmM5Pe/APJOR?node-id=466%3A251)
* Implementação do glossário na tela inicial.
* Implementação da página de cadastro e de telas secundárias, porém não está sendo adicionado no banco de dados.


