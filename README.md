# Diretório Nacional de Jornalistas

## Tecnologias Utilizadas

- Python Python 3.8.10
- Django 4.0.5
- postgres (PostgreSQL) 14.1 (Debian 14.1-1.pgdg110+1)
## Colaboradores

- Lucas Gonçalves 
- Tais Alves Oliveira - dtais@outlook.com.br

## Testes
## Instalação

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