CREATE TABLE Jogador (  
  	ID_jogador SERIAL PRIMARY KEY,
	nome_jogador VARCHAR(100),
  	mao_dominante VARCHAR(10),
  	altura INT,
  	COI VARCHAR(10)
 );
 
CREATE TABLE Ranking (  
  	ID_jogador INT,
	ID_Torneio INT,
  	pontos INT,
	PRIMARY KEY(ID_jogador, ID_Torneio),
	FOREIGN KEY(ID_jogador) REFERENCES Jogador(ID_jogador)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY(ID_Torneio) REFERENCES Torneio(ID_Torneio)
		ON UPDATE CASCADE
		ON DELETE CASCADE
 );
 
CREATE TABLE Torneio (  
  	ID_Torneio SERIAL PRIMARY KEY,
	nome_torneio VARCHAR(100),
  	categoria VARCHAR(10),
  	ano INT
 );

 INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI) VALUES( 'Ana', 'R', 156, 'BRA');
 INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI) VALUES( 'Bruno', 'L', 189, 'JPN');
 INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI) VALUES( 'Laura', 'R', 174, 'MEX');
 INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI) VALUES( 'Kaue', 'R', 194, 'ITA');
 INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI) VALUES( 'Lara', 'R', 162, 'FRA');

 select * from jogador

 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Sydney', 'A', 2000);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Rio de Janeiro', 'A', 2001);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'São Paulo', 'A', 2002);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Buenos Aires', 'A', 2003);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Kyoto', 'A', 2004);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Orlando', 'A', 2005);
 INSERT INTO Torneio (nome_torneio, categoria, ano) VALUES( 'Barcelona', 'A', 2006);

 select * from torneio

 INSERT INTO Ranking VALUES(1, 1, 127);
 INSERT INTO Ranking VALUES(1, 2, 50);
 INSERT INTO Ranking VALUES(1, 3, 134);
 INSERT INTO Ranking VALUES(1, 4, 100);
 INSERT INTO Ranking VALUES(1, 5, 98);
 INSERT INTO Ranking VALUES(1, 6, 107);
 INSERT INTO Ranking VALUES(1, 7, 78);

 INSERT INTO Ranking VALUES(2, 1, 10);
 INSERT INTO Ranking VALUES(2, 2, 53);
 INSERT INTO Ranking VALUES(2, 3, 23);
 INSERT INTO Ranking VALUES(2, 4, 60);
 INSERT INTO Ranking VALUES(2, 5, 32);
 INSERT INTO Ranking VALUES(2, 6, 42);
 INSERT INTO Ranking VALUES(2, 7, 67);
 
 INSERT INTO Ranking VALUES(3, 1, 47);
 INSERT INTO Ranking VALUES(3, 2, 59);
 INSERT INTO Ranking VALUES(3, 3, 68);
 INSERT INTO Ranking VALUES(3, 4, 35);
 INSERT INTO Ranking VALUES(3, 5, 46);
 INSERT INTO Ranking VALUES(3, 6, 74);
 INSERT INTO Ranking VALUES(3, 7, 67);
 
 INSERT INTO Ranking VALUES(4, 1, 100);
 INSERT INTO Ranking VALUES(4, 2, 200);
 INSERT INTO Ranking VALUES(4, 3, 134);
 INSERT INTO Ranking VALUES(4, 4, 234);
 INSERT INTO Ranking VALUES(4, 5, 165);
 INSERT INTO Ranking VALUES(4, 6, 124);
 INSERT INTO Ranking VALUES(4, 7, 213);

INSERT INTO Ranking VALUES(5, 1, 10);
 INSERT INTO Ranking VALUES(5, 2, 20);
 INSERT INTO Ranking VALUES(5, 3, 14);
 INSERT INTO Ranking VALUES(5, 4, 34);
 INSERT INTO Ranking VALUES(5, 5, 16);
 INSERT INTO Ranking VALUES(5, 6, 34);
 INSERT INTO Ranking VALUES(5, 7, 50);

  select * from ranking