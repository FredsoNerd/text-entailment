# from rdflib import ConjunctiveGraph, URIRef, Namespace
from rdflib import ConjunctiveGraph
import pprint
import sys
sys.setrecursionlimit(2000)

# https://rdflib.readthedocs.io/en/stable/index.html

def rdfterm_to_str(x, prefix):
    """
    return the correct query term to mount an sparql
    query. Terms of form "<[prefix](x|e)[n][suffix]>"
    are formed as free terms like "?(x|e)[n][suffix]"
    """
    
    if x.startswith(prefix): return "?"+x[len(prefix)::]
    return x.n3()

def make_pre_sparql(graphH):
    """
    parse indetifiers in graphT into triples and mount
    a pre-SPARQL query to be queried in ASK or SELECT

    returns: a pre-SPARQL query format of graphT like:
        <URI> <URI> ?var1 .
        <URI> ?var2 <URI> .
        ...
        ?varn ?var1 <URI> .
    """

    pre_sparql = """"""
    prefix = "http://example.com/"
    for s,p,o in graphH:
        pre_sparql += rdfterm_to_str(s, prefix) + " "
        pre_sparql += rdfterm_to_str(p, prefix) + " "
        pre_sparql += rdfterm_to_str(o, prefix) + " .\n"

    return pre_sparql

def entail_model(graphH, graphT):
    """
    receives a pair of HIPOTESIS and TEXT in RDF format
    and try finding a model showing graphT as a subgraph
    of graphH, i.e., T => H

    returns: a ResultRow containing a list of models
    """

    pre_sparql = make_pre_sparql(graphH)
    sparql = "select * where {" + pre_sparql +"}"

    res = graphT.query(sparql)
    print("Found {} models.".format(len(res)))
    return res

def entail_ask(graphH, graphT):
    """
    receives a pair of HIPOTESIS and TEXT in RDF format
    and try finding a model showing graphT as a subgraph
    of graphH; in this case, returns true

    returns: true (entail) or false (not entail)
    """

    pre_sparql = make_pre_sparql(graphH)
    sparql = "ask {" + pre_sparql +"}"

    res = graphT.query(sparql)
    return bool(res)

#############################################
# the graphs 0 and 1 were generated separtely
# for the same phrase "Two dogs are fighting"
# graphs are represented differently in 3.nq

data = open("demos/3.nq", "rb")

g = ConjunctiveGraph()
g.parse(data, format="nquads")
graphs = [x for x in g.store.contexts()]

# ask if there is a model
res = entail_ask(graphs[0], graphs[1])
print("Entail: ", res)
# ask for model granting entail
res = entail_model(graphs[0], graphs[1])
print("Model: ", res)
# iter over entail model showing model
for model in res: pprint.pprint(model)
