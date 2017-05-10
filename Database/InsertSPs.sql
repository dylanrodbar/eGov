USE eGov;

DROP PROCEDURE IF EXISTS EGSP_InsertUserType;
DROP PROCEDURE IF EXISTS EGSP_InsertTag;
DROP PROCEDURE IF EXISTS EGSP_InsertUser;
DROP PROCEDURE IF EXISTS EGSP_InsertPost;
DROP PROCEDURE IF EXISTS EGSP_InsertLawProject;
DROP PROCEDURE IF EXISTS EGSP_InsertComment;

DELIMITER //

CREATE PROCEDURE EGSP_InsertUserType (
	pName VARCHAR(50))
BEGIN
	INSERT INTO UserTypes (Name)
	VALUES (pName);
END
//

CREATE PROCEDURE EGSP_InsertTag (
	pTag VARCHAR(20))
BEGIN
	INSERT INTO Tags (Tag)
	VALUES (pTag);
END
//

CREATE PROCEDURE EGSP_InsertUser (
	pID INT,
	pName VARCHAR(75),
	pUserName VARCHAR(25),
	pEmail VARCHAR(75),
	pPassword VARCHAR(200),
	pUserType INT,
	pPicturePath VARCHAR(100))
BEGIN
	INSERT INTO ProfilePictures(Path)
	VALUES (pPicturePath);
	
	INSERT INTO Users (ID, Name, UserName, Email, Password, Points, FK_UserType, FK_ProfilePicture)
	VALUES (pID, pName, pUserName, pEmail, pPassword, 0, pUserType, LAST_INSERT_ID());
END
//

CREATE PROCEDURE EGSP_InsertPost (
	pTitle VARCHAR(50),
    pDescription VARCHAR(200),
    pContent VARCHAR(5000),
    pUser INT,
    pImages VARCHAR(1000),
    pTags VARCHAR(500),
    OUT postID INT)
BEGIN
    DECLARE pos INT;
    DECLARE len INT;
    DECLARE idTag INT;
    DECLARE imagePath VARCHAR(100);
    
    INSERT INTO Posts (Title, Description, Content, Views, Date, FK_User)
    VALUES (pTitle, pDescription, pContent, 0, CURDATE(), pUser);
    
    SET postID = LAST_INSERT_ID();
    SET pos = 1;
    SET len = LENGTH(pTags) - LENGTH( REPLACE(pTags, ',', '') ) + 1;
    
    WHILE (pos <= len)
    DO
		SET idTag = CAST (EGF_SplitString (pTags, ',', pos));
        
        INSERT INTO TagsXPost (FK_Post, FK_Tag)
        VALUES (postID, idTag);
        
        SET pos = pos + 1;
	END WHILE;
    
    
    SET pos = 1;
    SET len = LENGTH(pImages) - LENGTH( REPLACE(pImages, ',', '') ) + 1;
    
    WHILE (pos <= len)
    DO
		SET imagePath = EGF_SplitString (pImages, ',', pos);
        
        INSERT INTO Images (FK_Post, Path)
        VALUES (postID, imagesPath);
        
        SET pos = pos + 1;
	END WHILE;
END
//

CREATE PROCEDURE EGSP_InsertLawProject (
	pTitle VARCHAR(50),
    pDescription VARCHAR(200),
    pContent VARCHAR(5000),
    pLink VARCHAR(200),
    pUser INT,
    pImages VARCHAR(1000),
    pTags VARCHAR(500))
BEGIN
	DECLARE postID INT;
    
    CALL EGSP_InsertPost (pTitle, pDescription, pContent, pUser, pImages, pTags, postID);
    
    INSERT INTO Stadistics (Yes, No, Unknown)
    VALUES (0, 0, 0);
    
    INSERT INTO LawProjects (FK_Post, Link, FK_Stadistics)
    VALUES (postID, pLink, LAST_INSERT_ID());
END
//

CREATE PROCEDURE EGSP_InsertComment (
	pDescription VARCHAR(500),
    pUser INT,
    pPost INT)
BEGIN
	INSERT INTO Comments (Description, FK_User, FK_Post)
    VALUES (pDescription, pUser, pPost);
END
//

DELIMITER ;