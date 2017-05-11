insert into UserTypes(Name) values ('Administrador')
insert into UserTypes(Name) values ('Cliente')


insert into ProfilePictures(Path) values('path1');
insert into ProfilePictures(Path) values('path2');
insert into ProfilePictures(Path) values('path3');
insert into ProfilePictures(Path) values('path4');
insert into ProfilePictures(Path) values('path5');
insert into ProfilePictures(Path) values('path6');
insert into ProfilePictures(Path) values('path7');
insert into ProfilePictures(Path) values('path8');
insert into ProfilePictures(Path) values('path9');
insert into ProfilePictures(Path) values('path10');


insert into Users(ID, Name, UserName, Email, PassWord, Points, FK_UserType, FK_ProfilePicture) 
values(1, 'Dylan', 'dylanrodbar', 'dylanrodbar97@gmail.com', '1', 0, 2, 1)
insert into Users(ID, Name, UserName, Email, PassWord, Points, FK_UserType, FK_ProfilePicture) 
values(2, 'Alberto', 'albertorodbar', 'albertorodbar97@gmail.com', '2', 0, 1, 1)

insert into Posts(Title, Description, Content, Views, Date, FK_User) 
values ('Primer post', 'Esta es una descripcion', 'Contenido', 0, '2017-05-15', 1)

insert into Posts(Title, Description, Content, Views, Date, FK_User) 
values ('Segundo post', 'Esta es una descripcion2', 'Contenido2', 0, '2017-05-15', 2)

insert into Posts(Title, Description, Content, Views, Date, FK_User) 
values ('Tercer post', 'Esta es una descripcion3', 'Contenido3', 0, '2017-05-15', 1)

insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario1', 1, 1, '2017-03-12')
insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario2', 2, 1, '2017-04-19')
insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario3', 2, 1, '2017-05-14')
insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario4', 1, 1, '2017-01-09')

insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario1', 1, 2, '2017-02-25')
insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario2', 2, 2, '2017-09-24')
insert into Comments(Description, FK_User, FK_Post, Date) values ('Comentario3', 2, 2, '2017-06-10')