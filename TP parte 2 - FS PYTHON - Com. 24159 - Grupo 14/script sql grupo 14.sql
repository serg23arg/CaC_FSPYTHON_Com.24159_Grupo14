create database grupo14_db;
use grupo14_db;

create table form_contacto(
	Id int(4) primary key auto_increment,
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Motivo ENUM('Publicar un aviso', 'Opinar sobre un servicio', 'Hacer una consulta'),
    Nombre VARCHAR(20),
    Apellido VARCHAR(20),
    E_mail VARCHAR (30),
    Whatsapp INT(15),
    Mensaje VARCHAR(500),
    Adjunto ENUM('SI', 'NO'),
    TC ENUM('SI', 'NO'),
    Observaciones VARCHAR(100) DEFAULT ""
);

select * from form_contacto;
