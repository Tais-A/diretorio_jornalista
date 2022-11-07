# Diretório Piloto de Jornalistas no Brasil.

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


## Sprint 1

Durante a disciplina de Jornalismo Digital foi feito:

* Prototipação no Figma da página inicial, página de cadastro de jornalista e página do revisor. [Link do Figma](https://www.figma.com/file/4ap6riA5XxfGb6byJmM5Pe/APJOR?node-id=466%3A251)
* Implementação do glossário na tela inicial.
* Implementação da página de cadastro e de telas secundárias, porém não está sendo adicionado no banco de dados.



