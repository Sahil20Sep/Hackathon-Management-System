CREATE TABLE IF NOT EXISTS Participant
(
	Part_id bigint NOT NULL, 
	First_Name varchar NOT NULL, 
	Last_Name varchar NOT NULL, 
	Email_add char VARYING NOT NULL,
	DOB date NOT NULL,
	Student VARCHAR NOT NULL,
	College VARCHAR NOT NULL, 
	CPI FLOAT NOT NULL,
	PRIMARY KEY (Part_id)
)

COPY Participant FROM 'D:\DBMS_Table\All_Table\Participation_Table_1.csv' DELIMITER ',' CSV HEADER;
select * from Participant

CREATE TABLE IF NOT EXISTS Hackathon
(
	Hack_id bigint NOT NULL, 
	Hack_Name char VARYING NOT NULL, 
	Name_Type varchar NOT NULL,
	Date DATE NOT NULL,
	Time TIME NOT NULL,
	Duration bigint NOT NULL,
	PRIMARY KEY (Hack_id)
);

COPY "Hackathon" FROM 'D:\DBMS_Table\All_Table\Hackathon_1.csv' DELIMITER ',' CSV HEADER;
select * from "Hackathon"

select * from participant where cpi BETWEEN 7.2 and 8.6 order by cpi;


select * from participant where first_name like 'S%' or last_name like '%s' order by part_id;












