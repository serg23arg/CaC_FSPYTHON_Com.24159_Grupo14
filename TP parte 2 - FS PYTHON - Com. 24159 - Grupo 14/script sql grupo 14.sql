create database grupo14_db;
use grupo14_db;

create table form_contacto(
	Id int(4) primary key auto_increment,
    Fecha date,
    Motivo ENUM('Publicar un aviso', 'Opinar sobre un servicio', 'Hacer una consulta'),
    Nombre VARCHAR(20),
    Apellido VARCHAR(20),
    E_mail VARCHAR (30),
    Whatsapp INT(15),
    Mensaje VARCHAR(500),
    Adjunto ENUM('SI', 'NO'),
    TC ENUM('SI', 'NO'),
    Observaciones VARCHAR(100)
);

insert into form_contacto (Fecha, Motivo, Nombre, Apellido, E_mail, Whatsapp, Mensaje, Adjunto, TC, Observaciones) 
values(20240629,'Hacer una consulta', 'Sergio', 'Plaza', 'sergio@gmail.com',1155552222,'Hola buenas tardes, quería saber que costo tiene publicar un aviso en su página. Saludos','NO','SI','');

select * from form_contacto;