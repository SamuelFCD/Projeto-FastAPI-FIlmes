CREATE TABLE autor (
    autor_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    nacionalidade VARCHAR(50)
);

CREATE TABLE generos (
    genero_id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT
);

CREATE TABLE filmes (
    filme_id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    ano INTEGER NOT NULL,
    duracao_min INTEGER,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor_id INTEGER REFERENCES autor(autor_id)
);

CREATE TABLE filme_genero (
    filme_id INTEGER REFERENCES filmes(filme_id),
    genero_id INTEGER REFERENCES generos(genero_id),
    PRIMARY KEY (filme_id, genero_id)
);