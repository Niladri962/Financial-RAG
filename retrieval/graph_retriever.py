from graph_db.neo4j_setup import driver

def graph_search():

    query = """
    MATCH (c:Company)-[:HAS_REVENUE]->(r)
    RETURN c.name,r.value
    """

    with driver.session() as session:

        result = session.run(query)

        return [
            record.data()
            for record in result
        ]