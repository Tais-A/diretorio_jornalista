create table Usuario (
    nome varchar(65) primary key,
	data_nascimento date not null,
	raça_etnia varchar (45) not null,
	genero varchar (30),
	estado_civil varchar (15),
	cidade varchar (30),
	estado varchar (15),
	funcao varchar (30)
)

drop table Usuario


create table experiencia_profissional(
    locais_de_trabalho varchar (500) primary key,
    titulos varchar (100),
    outros_aspectos_profissionais varchar(100)
 )
 
drop table experiencia_profissional 


create table locais_de_trabalho(
    nome_profisinal varchar (65) primary key,
	foto oid,
	registro_profissional varchar (65),
	empresa_instituicao varchar (65),
	contato_do_jornalista varchar (65) not null
 )
 
drop table locais_de_trabalho


create table formacao (
    tema varchar (65)primary key,
	instituicao varchar (65) not null,
	ano_conclusao date not null,
	nivel_graduacao varchar (15)
	
 )
 
drop table formacao


create table manifestacao (
    idmanifestacao int primary key,
	descricao varchar (1000) not null
 )
 
drop table manifestacao
 
create table denuncia (
    iddenuncia int primary key,
	descricao varchar (1000) not null
 )
 
drop table denuncia


create table questionamento (
    idquestionamento int primary key,
	descricao varchar (1000) not null
 )
 
drop table questionamento

 
create table admin_geral (
    idaminis_geral int primary key,
	nome_adm varchar(65),
	funcao varchar (30)
 )
 
drop table admin_geral

