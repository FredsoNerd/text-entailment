# the reference of this project is the paper
# Semantic Parsing for Textual Entailment,
# Lien and Kouylekov, wich is avaliale at:
# www.aclweb.org/anthology/W15-2205.pdf

# 1. The text T and hypothesis H are analyzed with the ERG parser.
# 2. The EDSs for T and H are converted into RDF triples.
# 3. H is enriched using the SWRL rules and converted into a SPARQL
# query query h in which the query statements are the conjunction
# of all of the triples in the RDF representation of H.
# 4. The RDF triples of T and the SWRL rules for expanding T are
# given as the input to the reasoner.
# 5. If the query h is matched into the inferred model for T, the
# entailment relation is assigned to the pair.

from delphin import ace
from delphin import eds
from delphin.codecs import eds as edsnative

grm = 'erg.dat'
for x in ['The garden dog tried not to bark','Two dogs are fighting']:
    response = ace.parse(grm, x)
    m = response.result(0).mrs()
    print(list(m.variables))
    e = eds.from_mrs(m)
    print(edsnative.encode(e, indent=True))

