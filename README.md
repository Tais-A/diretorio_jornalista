# Diretório Nacional de Jornalistas

## Execução

```sh

#backend_api
cd diretorio_jornalistas/backend/api
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

# Tecnologias Utilizadas

```

Usuários e permissões:

Admin: possui permissão em todas as áreas do sistema,
Revisor: Poderá editar dados de jornalistas, e desativar temporariamente contas
Jornalista: poderá adicionar e editar dados próprios
Usuário: pode contatar jornalista e registrar manifestações
Visitante: poderá visualizar os dados dos jornalistas
