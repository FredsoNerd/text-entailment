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
from delphin.predicate import split

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

def synonyms_or_hyperonyms(lemmaT, lemmaH):
    return True

# structure for simple Nodes acess from ID
dictT = dict()
dictH = dict()
def make_dict(dictX, edsX):
    dictX = {node.id:node for node in edsX.nodes}

def match_events_1(nodeT, nodeH):
    """
    Returns wether they represent the same lexeme
    with the same part-of-speech, or if both are verbs
    and Hevent is a synonym or hypernym of Tevent
    """

    if nodeT.predicate == nodeH.predicate: return True
    lpossT = split(nodeT.predicate)  # lemma, part-of-speech, sense
    lpossH = split(nodeH.predicate)  # lemma, part-of-speech, sense
    
    verbs = lpossT[1] == "v" and lpossH[1] == "v"
    s_or_h = synonyms_or_hyperonyms(lpossT[0], lpossH[0])
    
    return verbs and s_or_h

def match_events_2(nodeT, nodeH):
    # Two event relation arguments in the same
    # argument position match if:
    lemmaT, posT, senseT = split(nodeT.predicate)
    lemmaH, posH, senseH = split(nodeH.predicate)
    
    # they are the same or synonymous, or the
    # Hevent argument is a hypernym of the Tevent
    # argument, or
    if lemmaT == lemmaH: return True
    if synonyms_or_hyperonyms(lemmaT, lemmaH):
        return True

    # the argument in Tevent represents a noun
    # phrase and te argument in Hevent is an
    # underspecified pronoun like somebody, or
    pass # todo

    # the argument in Tevent is either a scopal
    # relation or a conjunction relation, and one
    # of its arguments matches that of Hevent, or
    pass # todo

    # the argument in Hevent is not expressed
    # (i.e., it matches the Tevent argument by
    # default)
    pass # todo

    return False

def match_predicate_events(nodeT, nodeH):
    """
    We use Lien and Kouylekov's two steps matching event relations.
    See reference in aclweb.org/anthology/S14-2125.pdf
    """

    # 1. they are the same lexeme and part-of-speech
    # or the same verbs synonyms or hiperonims
    if not match_events_1(nodeT, nodeH):
        return False

    # 2. all their arguments match.
    if len(nodeT.edges) != len(nodeH.edges):
        return False
    
    for key in nodeT.keys():
        if not match_events_2(dictT[key], dictH[key]):
            return False

    return True

def entail(textT, textH, grm = '../erg.dat'):
    """
    attemps to an unification algorithm to answer the problem of
    entailment between text_T and text_H. The unification has to
    consider reasoning and other kinds of generalizations.
    """

    # parse text_T into ERG graph format
    resT = ace.parse(grm, textT)
    mrsT = resT.result(0).mrs()
    edsT = eds.from_mrs(mrsT, unique_ids=True)
    make_dict(dictT, edsT)     # search for a better solution
    # parse text_H into ERG graph format
    resH = ace.parse(grm, textH)
    mrsH = resH.result(0).mrs()
    edsH = eds.from_mrs(mrsH, unique_ids=True)
    make_dict(dictH, edsH)     # search for a better solution

    # For each event relation Hevent in the
    # hypothesis the procedure tries to find
    # a matching relation Tevent among the
    # text event relations.

    # we use a naive algorithm to find and
    # try possile mathching relations
    for nodeH in edsH.nodes:
        if nodeH.type != "e": continue
        for nodeT in edsT.nodes:
            if nodeT.type != "e": continue
            # nodeH and nodeT are event edges
            if match_predicate_events(nodeT, nodeH):
                return True
    # case we cant find an entail
    return False

res = entail("A dog is running", "A dog is moving")
print(res)
