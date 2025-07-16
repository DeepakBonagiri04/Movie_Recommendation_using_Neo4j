CREATE (u1:User {userId: 1, name: 'Alice'}),
       (u2:User {userId: 2, name: 'Bob'}),
       (m1:Movie {movieId: 1, title: 'Inception', genre: 'Sci-Fi', year: 2010}),
       (m2:Movie {movieId: 2, title: 'The Matrix', genre: 'Sci-Fi', year: 1999}),
       (m3:Movie {movieId: 3, title: 'Titanic', genre: 'Romance', year: 1997}),
       (u1)-[:RATED {rating: 5}]->(m1),
       (u1)-[:RATED {rating: 3}]->(m3),
       (u2)-[:RATED {rating: 4}]->(m2),
       (u2)-[:RATED {rating: 2}]->(m3);