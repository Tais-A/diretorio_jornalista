from .localidade import *
from .rede_social import RedeSocial
from .veiculo_de_comunicacao import VeiculoDeComunicacao

OPCOES_CIDADE = Cidades()

OPCOES_ESTADO = Estados()

OPCOES_GENERO = {
    (1, 'Femino'),
    (2, 'Masculino'),
    (3, 'Não Binário')
}

OPCOES_ETNIA = {
    (1, 'Preta'),
    (2, 'Branca'),
    (3, 'Amarela (Origem Asiática/Oriental)'),
    (4, 'Parda'),
    (5, 'Indígena'),
    (6, 'Não Declarado')
}

OPCOES_ESTADO_CIVIL = {
    (1, 'Solteiro'),
    (2, 'Casado'),
    (3, 'Divorciado'),
    (4, 'Viúvo'),
    (5, 'União Estável'),
}

OPCOES_TIPO_PUBLICACAO = {
    (1, 'Artigo'),
    (2, 'Entrevista'),
    (3, 'Coluna'),
    (4, 'Notícia'),
    (5, 'Ensaio Fotográfico'),
    (6, 'Reportagem'), 
    (7, 'Editorial'),
    (8, 'Crônica')
}