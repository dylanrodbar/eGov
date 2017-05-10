USE eGov;

DROP PROCEDURE IF EXISTS EGSP_SelectUserTypes;
DROP PROCEDURE IF EXISTS EGSP_SelectTags;
DROP PROCEDURE IF EXISTS EGSP_SelectAllPosts;
DROP PROCEDURE IF EXISTS EGSP_SelectPost;
DROP PROCEDURE IF EXISTS EGSP_SelectImagesXPost;
DROP PROCEDURE IF EXISTS EGSP_SelectCommentsXPost;
DROP PROCEDURE IF EXISTS EGSP_SelectUserFromLogIn;
DROP PROCEDURE IF EXISTS EGSP_SelecLawProjectStadistics;

DELIMITER //

CREATE PROCEDURE EGSP_SelectUserTypes ()
BEGIN
	SELECT UT.ID, UT.Name
    FROM UserTypes UT;
END
//

CREATE PROCEDURE EGSP_SelectTags()
BEGIN
	SELECT T.ID, T.Tag
    FROM Tags T;
END
//

/* Para la presentacion de los posts a modo resumen */
CREATE PROCEDURE EGSP_SelectAllPosts ()
BEGIN
	SELECT P.ID, P.Title, P.Description, P.Date
    FROM Posts P
	ORDER BY P.Views DESC;
END
//

CREATE PROCEDURE EGSP_SelectPost (
	pPostID INT)
BEGIN
	SELECT P.ID, P.Title, P.Description, P.Content, P.Views, LP.Link, P.Date, U.UserName
    FROM Posts P
    JOIN Users U
		ON U.ID = P.FK_User
	LEFT JOIN LawProject LP
		ON P.ID = LP.FK_Post
	WHERE P.ID = pPostID;
END
//

CREATE PROCEDURE EGSP_SelectImagesXPost (
	pPostID INT)
BEGIN
	SELECT I.Path
    FROM Images I
    WHERE I.FK_Post = pPostID;
END
//

CREATE PROCEDURE EGSP_SelectCommentsXPost (
	pPostID INT)
BEGIN
	SELECT C.Description, U.UserName
    FROM Comments C
	JOIN Users U
		ON U.ID = C.FK_User
	WHERE C.FK_Post = pPostID;
END
//

CREATE PROCEDURE EGSP_SelectUserFromLogIn (
	pUserName VARCHAR(25),
    pPassword VARCHAR(200))
BEGIN
	SELECT U.ID, U.Name, U.UserName, U.Email, U.Points, UT.Name, PP.Path
    FROM Users U
    JOIN UserTypes UT
		ON UT.ID = U.FK_UserType
	JOIN ProfilePictures PP
		ON PP.ID = U.FK_ProfilePicture
	WHERE
		U.UserName = pUserName AND U.Password = pPassword;
END
//

CREATE PROCEDURE EGSP_SelecLawProjectStadistics (
	pPostID INT)
BEGIN
	SELECT S.Yes, S.No, S.Unknown
    FROM Stadistics S
    JOIN LawProjects LP
		ON S.ID = LP.FK_Stadistics
	WHERE LP.FK_Post = pPostID;
END
//

DELIMITER ;