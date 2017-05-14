delimiter $$
create procedure login(UserName varchar(25), Password varchar(200))
begin
	
    select u.Id, ut.Name from User u, UserType ut  
		where u.UserName = UserName and u.Password = Password and u.FK_TipoUsuario = ut.Id;
	
end $$

delimiter ;
drop procedure login;
call login('albertorodbar', '2');


delimiter $$
create procedure numCommentPost(Post int)
begin
	
    select p.Title, count(*) as NumeroComentarios
		from Comment c, Post p
			where p.Id = Post and c.FK_Post = p.Id
				group by p.Id;
	
end $$

delimiter ;

drop procedure numCommentPost;
call numCommentPost(1);
call numCommentPost(2);

delimiter $$
create procedure commentsPost(Post int)
begin
	select c.Descripcion, u.Name, c.Date from Post p, Comment c, User u
		where p.Id = Post and p.Id = c.FK_Post and c.FK_User = u.Id;
end $$

delimiter;
call commentsPost(1);
drop procedure commentsPost


delimiter $$
create procedure PostsXUser(User int)
begin
	select p.Title, p.Views, p.Id from Posts p
		where p.FK_User = User;
	
end $$

delimiter ;
drop procedure PostsXUser
call PostsXUser(2)

delimiter $$
create procedure SignIn(Name varchar(75), LastName varchar(75), UserName varchar(25), Email varchar(75), Password varchar(200))
begin
	insert into Users(Name, LastName, UserName, Email, PassWord, Points, FK_UserType, FK_ProfilePicture) 
	values(Name, LastName, UserName, Email, Password, 0, 1, 1);
	
end $$

delimiter ;

drop procedure SignIn
call SignIn('Joanne', 'Germanotta', 'joanne123', 'joanne@gmail.com', 'joanne123')

delimiter $$
create procedure addViewPost(Post int)
begin
	Update Posts set views = views+1 where Posts.Id = Post;
	
end $$

delimiter ;

drop procedure addViewPost
call addViewPost(2)

delimiter $$
create procedure UserData(User int)
begin
	select u.Name, u.LastName, u.Email, p.Path, u.Points from Users u, ProfilePictures p
		where u.Id = User and u.FK_ProfilePicture = p.Id;
	
end $$

delimiter ;

drop procedure UserData
call UserData(2)

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
drop procedure selectLastPost
call selectLastPost()


CREATE PROCEDURE selectLawProjects ()
BEGIN
	select p.title, p.description, p.content, lp.link, p.Date, lp.FK_Post from Posts p,  LawProjects lp where p.Id = lp.FK_Post;
END $$
delimiter ;
drop procedure selectLawProjects
call selectLawProjects()

delimiter $$
CREATE PROCEDURE selectNews ()
BEGIN
	select p.title, p.description, p.content, p.Date, p.Id from Posts p,  LawProjects lp where p.Id not in
		(select FK_Post from LawProjects)
    group by p.Id;
END $$
delimiter ;
drop procedure selectNews
call selectNews()