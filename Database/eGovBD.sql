create database eGov;
use eGov;

create table UserTypes
(
	ID int auto_increment,
	Name varchar(50),
	primary key (ID)
);

create table ProfilePictures
(
	ID int auto_increment,
	Path varchar(100),
	primary key (ID)
);

create table Users
(
	ID int auto_increment,
	Name varchar(75),
    LastName varchar(75),
	UserName varchar(25) unique,
	Email varchar(75) unique,
	Password varchar(200),
	Points int,
	FK_UserType int,
	FK_ProfilePicture int,
	primary key (ID),
	foreign key (FK_UserType) references UserTypes (ID) on delete cascade,
	foreign key (FK_ProfilePicture) references ProfilePictures (ID) on delete cascade
);

insert into ProfilePictures(Path) values('C:/Users/user/Documents/GitHub/eGov/eGov/home/static/home/img/profile.jpg')

insert into Users(Name, LastName, UserName, Email, Password, Points, FK_UserType, FK_ProfilePicture)
values('Dylan', 'Rodríguez', 'dylanrodbar', 'dylanrodbar@gmail.com', '1', 0, 1, 1)

create table Posts
(
	ID int auto_increment,
	Title varchar(50),
	Description varchar(200),
	Content varchar(5000),
	Views int,
	Date date,
    State varchar(20),
	FK_User int,
	primary key (ID),
	foreign key (FK_User) references Users (ID) on delete cascade
);



create table Comments
(
	ID int auto_increment,
	Description varchar(500),
	Date date, 
	FK_User int,
	FK_Post int,
	primary key (ID),
	foreign key (FK_User) references Users (ID) on delete cascade,
	foreign key (FK_Post) references Posts (ID) on delete cascade
);

create table Images
(
	ID int auto_increment,
	Path varchar(100),
	FK_Post int,
	primary key (ID),
	foreign key (FK_Post) references Posts (ID) on delete cascade
);

create table Tags
(
	ID int auto_increment,
	Tag varchar(20),
	primary key (ID)
);

create table TagsXPost
(
	ID int auto_increment,
	FK_Post int,
	FK_Tag int,
	primary key (ID),
	foreign key (FK_Post) references Posts (ID) on delete cascade,
	foreign key (FK_Tag) references Tags (ID) on delete cascade
);

create table Stadistics
(
	ID int auto_increment,
	Yes int,
	No int,
	Unknown int,
	primary key (ID) 
);

create table LawProjects
(
	FK_Post int,
	Link varchar(2000),
    Yes int,
    No int,
    Unknown int,
	primary key (FK_Post),
	foreign key (FK_Post) references Posts (ID) on delete cascade
);

create table PointsPost(
	FK_Post int,
    FK_User int,
    
	foreign key (FK_Post) references Posts (ID) on delete cascade,
    foreign key (FK_User) references Users (ID) on delete cascade


)

create table VotesPost(
	FK_Post int,
    FK_User int,
    
	foreign key (FK_Post) references Posts (ID) on delete cascade,
    foreign key (FK_User) references Users (ID) on delete cascade


)

