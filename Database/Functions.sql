USE eGov;
DROP FUNCTION IF EXISTS EGF_SplitString;

DELIMITER //

CREATE FUNCTION EGF_SplitString (
	x VARCHAR(500), 
    delim VARCHAR(3), 
    pos INT)
RETURNS VARCHAR(100) DETERMINISTIC
BEGIN 
    RETURN REPLACE(SUBSTRING(SUBSTRING_INDEX(x, delim, pos),
									  LENGTH(SUBSTRING_INDEX(x, delim, pos -1)) + 1),
                                      delim, '');
END
//

DELIMITER ;