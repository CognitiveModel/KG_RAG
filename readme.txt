step1: Dependencies installation:
run Pip install -r requirements.txt



step2: add groq api to .env file


step3: Knowledge Graph creation in json format:

- run extract_graph.py; input data_dir and loader variable


step4: Ingest data to neo4j:

- create and run database in neo4j and run ingest.py by adding credentials


step5: retrival:

- run retreivel.py for retrievel depending on the query