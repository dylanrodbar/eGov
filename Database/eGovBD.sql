create database eGov
use eGov

create table UserType(
	
    Id int, 
    Name varchar(50),
    
    primary key(Id)
	

)

create table ProfilePicture(

	Id int,
    Path varchar(100),
    
    primary key(Id)


)
insert into ProfilePicture(Id, Path) values(1, 'path1');
insert into ProfilePicture(Id, Path) values(2, 'path2');



create table User(

	Id int,
    Name varchar(75),
    UserName varchar(25),
    Email varchar(75),
    Password varchar(200),
    Points int,
    FK_TipoUsuario int,
    FK_ProfilePicture int,
    
    primary key(Id),
    Foreign key(FK_TipoUsuario) references UserType(Id),
    Foreign key(FK_ProfilePicture) references ProfilePicture(Id)
    
    

)

create table Post(

	Id int,
    Title varchar(50),
    Description varchar(200),
    Content varchar(5000),
    Views int,
    Date date,
    FK_User int,
    
    primary key(Id),
    Foreign key(FK_User) references User(Id)



)

create table Image(

	Id int,
    Path varchar(100),
    FK_Post int,
	
    primary key(Id),
    Foreign key(FK_Post) references Post(Id)

)

create table Comment(

	Id int,
    Descripcion varchar(500),
    FK_User int,
    FK_Post int,
    
    primary key(Id),
    Foreign key(FK_User) references User(Id),
    Foreign key(FK_Post) references Post(Id)

)


create table Stadistic(

	Id int,
    Yes int,
    No int,
    Unknown int,
    FK_LawProject int,
    
    primary key(Id)
    


)

ALTER TABLE Stadistic ADD FOREIGN KEY (FK_LawProject) REFERENCES LawProject(FK_Post);

create table LawProject(

	FK_Post int,
    Link varchar(200),
    FK_Stadistics int,
    
    primary key(FK_Post),
    Foreign key(FK_Post) references Post(Id),
    Foreign key(FK_Stadistics) references Stadistic(Id)


)

create table Tag(

	Id int,
    Tag varchar(20),
    
    primary key(Id)

)

create table TagsXPost(

	id int,
    FK_Post int,
    FK_Tag int,
    
    primary key(Id),
    Foreign key(FK_Post) references Post(Id),
    Foreign key(FK_Tag) references Tag(Id)

)



