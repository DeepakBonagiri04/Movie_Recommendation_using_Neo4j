# 🎬 Neo4j Movie Recommender

A beginner-friendly movie recommender system using Neo4j Aura Free Tier and Python.

## 📌 What it does

- Stores users, movies, and ratings as a graph.
- Recommends movies to users based on other users with similar tastes (collaborative filtering).
- Uses Neo4j Aura Cloud + Neo4j Python Driver.

---

## 🚀 How to Use

### Step 1: Create the Graph in Neo4j

1. Go to [Neo4j Browser](https://browser.neo4j.io/)
2. Connect using your Aura credentials.
3. Paste and run the contents of `movie_data.cypher`.

### Step 2: Run the Python Script

1. Install the Neo4j driver:

```bash
pip install neo4j

---

Run it:

python recommend.py
