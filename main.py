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

def main():
    # we use pydelphin for ERG parser as web client
    from delphin.web import client
    response = client.parse('Abrams chased Browne', params={'mrs': 'json'})
    m = response.result(0).mrs()

    # Kouylekov and Oepen (2014) map different types
    # of meaning representations, including the EDSs
    # used in our work, to RDF graphs, stored in off-
    # the-shelf RDF triple stores, and searched using
    # SPARQL queries:
    # At: https://www.aclweb.org/anthology/C14-2.pdf

#-----------------------------------------------------
if __name__ == '__main__': main()
