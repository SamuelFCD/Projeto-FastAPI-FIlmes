INSERT INTO autor (nome, nacionalidade) VALUES
('Anthony Russo', 'Americano'),
('Jon Watts', 'Americano'),
('Christopher Nolan', 'Britânico'),
('Francis Ford Coppola', 'Americano'),
('Bong Joon-ho', 'Sul-coreano'),
('Lana Wachowski', 'Americana'),
('Fernando Meirelles', 'Brasileiro');

INSERT INTO generos (nome) VALUES
('Ação'),
('Ficção Científica'),
('Drama'),
('Suspense');

INSERT INTO filmes (titulo, ano, duracao_min, autor_id) VALUES
('Vingadores: Ultimato', 2019, 181, 1),
('Homem-Aranha: Sem Volta Para Casa', 2021, 148, 2),
('Interestelar', 2014, 169, 3),
('O Poderoso Chefão', 1972, 175, 4),
('Parasita', 2019, 132, 5),
('Matrix', 1999, 136, 6),
('Cidade de Deus', 2002, 130, 7);

INSERT INTO filme_genero (filme_id, genero_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(6, 2),
(7, 3);