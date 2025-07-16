from neo4j import GraphDatabase

# ✅ Define credentials first
uri = "neo4j+s://bcd6ca54.databases.neo4j.io"
user = "neo4j"
password = "IYUO0QlrFDzzK42RvzCQ2OqRwQ2o-4HeUyMBQtDvVi0"

# ✅ Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# ✅ Function to get recommendations
def get_recommendations(tx, username):
    query = """
    MATCH (u:User {name: $username})-[:RATED]->(:Movie)<-[:RATED]-(other:User)-[:RATED]->(rec:Movie)
    WHERE NOT (u)-[:RATED]->(rec)
    RETURN rec.title AS RecommendedMovie, COUNT(*) AS score
    ORDER BY score DESC
    LIMIT 5;
    """
    result = tx.run(query, username=username)
    return [record["RecommendedMovie"] for record in result]

# ✅ Run the query and print results
with driver.session() as session:
    recommendations = session.execute_read(get_recommendations, "Alice")
    print(f"Recommended movies for Alice: {recommendations}")

# ✅ Close the connection
driver.close()