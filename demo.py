
from rdflib import ConjunctiveGraph, URIRef, Namespace
import pprint

# https://rdflib.readthedocs.io/en/stable/index.html

data = open("demo.nq", "rb")

g = ConjunctiveGraph()
g.parse(data, format="nquads")

graphs = [x for x in g.store.contexts()]

for s in graphs[0]:
    pprint.pprint(s)
