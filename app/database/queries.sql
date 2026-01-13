SELECT * FROM autor

SELECT * FROM filmes

SELECT * FROM filme_genero

SELECT * FROM generos

SELECT
    f.titulo,
    STRING_AGG(g.nome, ', ') AS generos
FROM filmes f
JOIN filme_genero fg ON fg.filme_id = f.filme_id
JOIN generos g ON g.genero_id = fg.genero_id
GROUP BY f.filme_id, f.titulo;