# from rdflib import ConjunctiveGraph, URIRef, Namespace
from rdflib import ConjunctiveGraph
import pprint
import sys
sys.setrecursionlimit(2000)

# https://rdflib.readthedocs.io/en/stable/index.html

def rdfterm_to_str(x):
    return x.n3()

def entail(graphH, graphT):
    """
    parse indetifiers in graphT into valid RDF triples
    and mount the SPARQL query to be queried in graphH
    """
    rdf = """"""
    for s,p,o in graphT:
        rdf += rdfterm_to_str(s) + " "
        rdf += rdfterm_to_str(p) + " "
        rdf += rdfterm_to_str(o) + " .\n"

    sparql_query = "ask{" + rdf + "}"

    return bool(graphH.query(sparql_query))

data = open("demos/3.nq", "rb")

g = ConjunctiveGraph()
g.parse(data, format="nquads")
graphs = [x for x in g.store.contexts()]

# the graphs 0 and 1 were generated separtely
# for same phrase "Two dogs are fighting"
res = entail(graphs[0], graphs[1])
print("Entail value: ", res) # false

## we entail each phrase with itself
# for i in range(98):
    # res = entail(graphs[i-1], graphs[i-1])
    # print("Graph {} entail value: ".format(i+1), res)