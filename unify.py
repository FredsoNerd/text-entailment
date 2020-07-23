# References of this project are the papers from Lien and Kouylekov:
# Using Minimal Recursion Semantics for Entailment Recognition, and
# UIO-Lien: Entailment Recognition using Minimal Recursion Semantics
# wich are avaliale at:
#   aclweb.org/anthology/E14-3009.pdf
#   aclweb.org/anthology/S14-2125.pdf

# Here, the idea is to recognize the entail through unification with
# reasoning betwen textT's and textH's nodes erg-representation
# For unification, reference: eli.thegreenplace.net/2018/unification

from delphin import ace
from delphin import eds
from delphin.codecs import eds as edsnative

def unify_reasoning(edsT, edsH, uniH):
    # this will be usefull in future, when using resoning
    """
    we try using reasoning to infer predicates over a node, or nodes,
    in eds_H using predicates in eds_T as axioms. We also assuming an
    unification hipotesis in uni_H.
    
    In case of inferring fail, we discard the unification hipotesis.
    In case of success, we keep the unification hipotesis uni_H.
    """
    
    return True

def match_events_1(edgT, egjH):
    return True

def match_events_2(edgT, egjH):
    # Two event relation arguments in the same
    # argument position match if:
    
    # they are the same or synonymous, or the
    # Hevent argument is a hypernym of the Tevent
    # argument, or

    # the argument in Tevent represents a noun
    # phrase and the argument in Hevent is an
    # underspecified pronoun like somebody, or

    # the argument in Tevent is either a scopal
    # relation or a conjunction relation, and one
    # of its arguments matches that of Hevent, or

    # the argument in Hevent is not expressed
    # (i.e., it matches the Tevent argument by
    # default)

    return True

def match_predicate_events(edgT, egjH):
    """
    We use Lien and Kouylekov's two steps matching event relations.
    See reference in aclweb.org/anthology/S14-2125.pdf
    """

    # 1. they represent the same lexeme with the
    # same part-of-speech, or if both are verbs and
    # Hevent is a synonym or hypernym of Tevent
    match_1 = match_events_1(edgT, egjH)

    # 2. all their arguments match.
    match_2 = match_events_2(edgT, egjH)

    return match_1 and match_2


def entail(textT, textH, grm = '../erg.dat'):
    """
    attemps to an unification algorithm to answer the problem of
    entailment between text_T and text_H. The unification has to
    consider reasoning and other kinds of generalizations.
    """

    # parse text_T into ERG graph format
    resT = ace.parse(grm, textT)
    mrsT = resT.result(0).mrs()
    edsT = eds.from_mrs(mrsT)
    # parse text_H into ERG graph format
    resH = ace.parse(grm, textH)
    mrsH = resH.result(0).mrs()
    edsH = eds.from_mrs(mrsH)

    # For each event relation Hevent in the
    # hypothesis the procedure tries to find
    # a matching relation Tevent among the
    # text event relations.

    # we use a naive algorithm to find and
    # try possile mathching relations
    for edgH in edsH.nodes:
        if edgH.type != "e": continue
        for edgT in edsT.nodes:
            if edgT.type != "e": continue
            # edgH and edgT are event edges
            if match_predicate_events(edgT, edgH):
                return True
    # case we cant find an entail
    return False

res = entail("A dog is running", "A dog is moving")
print(res)