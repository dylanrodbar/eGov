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