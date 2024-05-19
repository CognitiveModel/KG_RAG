from neo4j import GraphDatabase
import pandas as pd


NEO4J_URL = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
NEO4J_DATABASE = "neo4j"

driver = GraphDatabase.driver(NEO4J_URL, database=NEO4J_DATABASE, auth=(NEO4J_USER, NEO4J_PASSWORD))

ingest_cypher = '''

CALL apoc.load.json("file:///my_data.json") YIELD value
MERGE (n1:Node {content: value.node_1, embedding:value.node1_embedding})
MERGE (n2:Node {content: value.node_2, embedding:value.node2_embedding}) 
MERGE (n1)-[:Edge {content: value.edge, embedding: value.edge_embedding}]->(n2)

'''


# ingest

with driver.session() as session:
    session.run(ingest_cypher)

        


#create edge vector (relationship) index
edge_cypher = '''

CREATE VECTOR INDEX `edge-embedding`

FOR ()-[r:Edge]-() ON (r.embedding) 

OPTIONS {indexConfig: { 

 `vector.dimensions`: 384, 

 `vector.similarity_function`: 'cosine' 

}} 

'''

with driver.session() as session:
    session.run(edge_cypher)



#create node vector index
node_cypher = '''
CALL db.index.vector.createNodeIndex('node-embedding', 'Node', 'embedding', 384, 'COSINE')
'''

with driver.session() as session:
    session.run(node_cypher)


