delimiter $$
create procedure login(UserName varchar(25), Password varchar(200))
begin
	
    select u.Id, ut.Name, ut.Id from Users u, UserTypes ut  
		where u.UserName = UserName and u.Password = Password and u.FK_UserType = ut.Id;
	
end $$

delimiter ;


delimiter $$
create procedure numCommentPost(Post int)
begin
	
    select p.Title, count(*) as NumeroComentarios
		from Comments c, Posts p
			where p.Id = Post and c.FK_Post = p.Id
				group by p.Id;
	
end $$

delimiter ;


delimiter $$
create procedure commentsPost(Post int)
begin
	select c.Description, u.Name, c.Date, pp.Path from Posts p, Comments c, Users u, ProfilePictures pp
		where p.Id = Post and p.Id = c.FK_Post and c.FK_User = u.Id and u.FK_ProfilePicture = pp.Id;
end $$

delimiter;

drop procedure commentsPost
delimiter $$
create procedure PostsXUser(User int)
begin
	select p.Title, p.Views, p.Id, p.State from Posts p
		where p.FK_User = User;
	
end $$

delimiter ;

delimiter $$
create procedure SignIn(Name varchar(75), LastName varchar(75), UserName varchar(25), Email varchar(75), Password varchar(200), ProfilePic int)
begin
	insert into Users(Name, LastName, UserName, Email, PassWord, Points, FK_UserType, FK_ProfilePicture) 
	values(Name, LastName, UserName, Email, Password, 0, 2, ProfilePic);
	
end $$

delimiter ;



delimiter $$
create procedure addViewPost(Post int)
begin
	Update Posts set views = views+1 where Posts.Id = Post;
	
end $$

delimiter ;


delimiter $$
create procedure UserData(User int)
begin
	select u.Name, u.LastName, u.Email, p.Path, u.Points from Users u, ProfilePictures p
		where u.Id = User and u.FK_ProfilePicture = p.Id;
	
end $$

delimiter ;


delimiter $$
create procedure deletePost(Post int)
begin
	delete from Posts where Id = Post;
	
end $$

delimiter ;

delimiter $$
CREATE PROCEDURE EInsertLawProject (
	Post int,
    Link varchar(3000))
BEGIN
	INSERT INTO LawProjects (FK_Post, Link, Yes, No, Unknown)
    VALUES (Post, Link, 0, 0, 0);
END $$
delimiter ;

delimiter $$
create procedure updatePost(Post int, title varchar(50), description varchar(200), content varchar(5000) )
begin
	
    update Posts set Title = title, Description = description, Content = content where Id = Post;
	
end $$

delimiter ;


delimiter $$
CREATE PROCEDURE selectLastPost ()
BEGIN
	Select p.Id from Posts p order by Id desc limit 1;
END $$
delimiter ;

delimiter $$

CREATE PROCEDURE selectLawProjects ()
BEGIN
	select p.title, p.description, p.content, lp.link, p.Date, lp.FK_Post from Posts p,  LawProjects lp where p.Id = lp.FK_Post;
END $$
delimiter ;
drop procedure selectLawProjects
call selectLawProjects()

delimiter $$
CREATE PROCEDURE selectNewsClient ()
BEGIN

	if not exists (select * from LawProjects) then
		select p.title, p.description, p.content, p.Date, p.Id from Posts p where p.State = 'Aceptado';
	else
		select p.title, p.description, p.content, p.Date, p.Id from Posts p,  LawProjects lp where p.Id not in
			(select FK_Post from LawProjects) and p.State = 'Aceptado'
		group by p.Id;
	end if;
END $$
delimiter ;

delimiter $$
CREATE PROCEDURE selectNewsAdmin ()
BEGIN
	if not exists (select * from LawProjects) then

		select p.title, p.description, p.content, p.Date, p.Id from Posts p where p.State = 'Pendiente';
	
    else
		select p.title, p.description, p.content, p.Date, p.Id from Posts p,  LawProjects lp where p.Id not in
			(select FK_Post from LawProjects) and p.State = 'Pendiente'
		group by p.Id;
	end if;
END $$
delimiter ;




delimiter $$
create procedure getStadisticsProject(Post int)
begin
	Declare resultYes decimal;
    Declare resultNo decimal;
	Declare resultUnknown decimal;
	
    Declare yes int;
    Declare no int;
    Declare unknown int;
    Declare total int;
    
    
    set resultYes = 0;
    set ResultNo = 0;
    set ResultUnknown = 0;
    
    select lp.Yes from LawProjects lp where lp.FK_Post = Post into yes;
    select lp.No from LawProjects lp where lp.FK_Post = Post into no;
    select lp.Unknown from LawProjects lp where lp.FK_Post = Post into unknown;
	
    set total = yes+no+unknown;
    
    if total <> 0 then
		
		set resultYes = (yes*100)/(total);
		set resultNo = (no*100)/(total);
		set resultUnknown = (unknown*100)/(total);
	end if;
		
    select resultYes as 'Yes', resultNo as 'No', resultUnknown as 'Unknown';
    
end $$

delimiter ;
drop procedure getStadisticsProject 
use eGov
select * from LawProjects
call getStadisticsProject(19)
call login('gaga', 'gaga')



delimiter $$
create procedure addYesProject(Post int)
begin
	Update LawProjects set Yes = Yes+1 where LawProjects.FK_Post = Post;
	
end $$

delimiter ;

delimiter $$
create procedure addNoProject(Post int)
begin
	Update LawProjects set No = No+1 where LawProjects.FK_Post = Post;
	
end $$

delimiter ;

delimiter $$
create procedure addUnknownProject(Post int)
begin
	Update LawProjects set Unknown = Unknown+1 where LawProjects.FK_Post = Post;
	
end $$

delimiter ;



delimiter $$
create procedure acceptNew(Post int)
begin
	Update Posts set State = 'Aceptado' where Id = Post;
	
end $$

delimiter ;

delimiter $$
create procedure rejectNew(Post int)
begin
	Update Posts set State = 'Rechazado' where Id = Post;
	
end $$

delimiter ;


delimiter $$
create procedure EInsertPost(pTitle VARCHAR(50),
    pDescription VARCHAR(200),
    pContent VARCHAR(5000),
    pUser INT)
begin
	insert into Posts(Title, Description, Content, FK_User, State, Date, Views) values(pTitle, pDescription, pContent, pUser, 'Pendiente', CURDATE(), 0);
end $$
delimiter ;

delimiter $$
create procedure EInsertPostAdmin(pTitle VARCHAR(50),
    pDescription VARCHAR(200),
    pContent VARCHAR(5000),
    pUser INT)
begin
	insert into Posts(Title, Description, Content, FK_User, State, Date, Views) values(pTitle, pDescription, pContent, pUser, 'Aceptado', CURDATE(), 0);
end $$
delimiter ;


DELIMITER //

CREATE PROCEDURE EGSP_UpdateUser (
	pID INT,
	pUserName VARCHAR(25),
	pName VARCHAR(75),
    pEmail VARCHAR(75),
	pPassword VARCHAR(200),
	pUserType INT)
BEGIN
	UPDATE Users
			SET 
					UserName = pUserName,
                    LastName = pName,
                    Email = pEmail,
                    Password = pPassword,
                    FK_UserType = pUserType
    WHERE ID = pID;
END
//

DELIMITER //

CREATE PROCEDURE EGSP_InsertComment (
	pDescription VARCHAR(500),
    pUser INT,
    pPost INT)
BEGIN
	INSERT INTO Comments (Description, FK_User, FK_Post, Date)
    VALUES (pDescription, pUser, pPost, CURDATE());
END
//

DELIMITER ;

delimiter $$
create procedure addPointUser(User int)
begin
	Update Users set points = points + 1 where Id = User;
end $$
delimiter ;
call addPointUser(1)
select * from Users


delimiter $$
create procedure InsertPointPost(User int, Post int)
begin
	insert into PointsPost(FK_User, FK_Post) values(User, Post);
end $$
delimiter ;

delimiter $$
create procedure InsertVotePost(User int, Post int)
begin
	insert into VotesPost(FK_User, FK_Post) values(User, Post);
end $$
delimiter ;

delimiter $$
create procedure getPointPost(User int, Post int)
begin
	select * from PointsPost pp where pp.FK_User = User and pp.FK_Post = Post;
end $$
delimiter ;


delimiter $$
create procedure getVotePost(User int, Post int)
begin
	select * from VotesPost vp where vp.FK_User = User and vp.FK_Post = Post;
end $$
delimiter ;

delimiter $$
create procedure getUserPost(Post int)
begin
	select u.Id, u.Name, u.Points, u.UserName from Users u, Posts p where p.Id = Post and p.FK_User = u.Id;
end $$
delimiter ;

delimiter $$
create procedure getLinkLawProject(Post int)
begin
	select lp.Link from LawProjects lp where lp.FK_Post = Post;
end $$
delimiter ;
