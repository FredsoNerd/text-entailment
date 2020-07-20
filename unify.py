# References of this project are the papers from Lien and Kouylekov:
# Using Minimal Recursion Semantics for Entailment Recognition, and
# UIO-Lien: Entailment Recognition using Minimal Recursion Semantics
# wich are avaliale at:
#   aclweb.org/anthology/E14-3009.pdf
#   aclweb.org/anthology/S14-2125.pdf

# Here, the idea is to recognize the entail through unification with
# reasoning betwen textT's and textH's nodes erg-representation

from delphin import ace
from delphin import eds
from delphin.codecs import eds as edsnative

def unify_reasoning(eds_T, eds_H, uni_H):
    """
    we try using reasoning to infer predicates over a node, or nodes,
    in eds_H using predicates in eds_T as axioms. We also assuming an
    unification hipotesis in uni_H.
    
    In case of inferring fail, we discard the unification hipotesis.
    In case of success, we keep the unification hipotesis uni_H.
    """

    return True

def entail(text_T, text_H, grm = '../erg.dat'):
    """
    attemps to an unification algorithm to answer the problem of
    entailment between text_T and text_H. The unification has to
    consider reasoning and other kinds of generalizations.
    """

    # parse text_T into ERG graph format
    res_T = ace.parse(grm, text_T)
    mrs_T = res_T.result(0).mrs()
    eds_T = eds.from_mrs(mrs_T)
    # parse text_H into ERG graph format
    res_H = ace.parse(grm, text_H)
    mrs_H = res_H.result(0).mrs()
    eds_H = eds.from_mrs(mrs_H)

    print(eds_T.top, eds_H.top)
    print(edsnative.encode(eds_T, indent=True))
    print(edsnative.encode(eds_H, indent=True))


entail("A dog is running", "A dog is moving")