USE eGov;

DROP PROCEDURE IF EXISTS EGSP_UpdateUser;
DROP PROCEDURE IF EXISTS EGSP_UpdateUserPoints;
DROP PROCEDURE IF EXISTS EGSP_UpdateYesOnProject;
DROP PROCEDURE IF EXISTS EGSP_UpdateNoOnProject;
DROP PROCEDURE IF EXISTS EGSP_UpdateUnknownOnProject;

DELIMITER //

CREATE PROCEDURE EGSP_UpdateUser (
	pID INT,
	pName VARCHAR(75),
	pUserName VARCHAR(25),
	pEmail VARCHAR(75),
	pPassword VARCHAR(200),
	pUserType INT)
BEGIN
	UPDATE Users
			SET Name = pName,
					UserName = pUserName,
                    Email = pEmail,
                    Password = pPassword,
                    UserType = pUserType
    WHERE ID = pID;
END
//

CREATE PROCEDURE EGSP_UpdateUserPoints (
	pID INT)
BEGIN
	UPDATE Users
			SET Points = Points + 1
    WHERE ID = pID;
END
//

CREATE PROCEDURE EGSP_UpdateYesOnProject (
	pPostID INT)
BEGIN
	UPDATE Stadistics S
	JOIN LawProjects LP
		ON  S.ID = LP.FK_Stadistics
			SET S.Yes = S.Yes + 1
	WHERE LP.FK_Post = pPostID;
END
//

CREATE PROCEDURE EGSP_UpdateNoOnProject (
	pPostID INT)
BEGIN
	UPDATE Stadistics S
	JOIN LawProjects LP
		ON  S.ID = LP.FK_Stadistics
			SET S.No = S.No + 1
	WHERE LP.FK_Post = pPostID;
END
//

CREATE PROCEDURE EGSP_UpdateUnknownOnProject (
	pPostID INT)
BEGIN
	UPDATE Stadistics S
	JOIN LawProjects LP
		ON  S.ID = LP.FK_Stadistics
			SET S.Unknown = S.Unknown + 1
	WHERE LP.FK_Post = pPostID;
END
//