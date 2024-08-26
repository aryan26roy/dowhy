import pytest

from pywhy_graphs import MAG, PAG

from dowhy.causal_identifier.complete_adjustment import CompleteAdjustment

def test_complete_adjsutment():
    
    # DAGs

    G = MAG()
    G.add_edge("Z", "X", G.directed_edge_name)
    G.add_edge("Z", "Y", G.directed_edge_name)
    G.add_edge("X", "Y", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"X"}, {"Y"})

    assert cad.adjustable()


    G = MAG()
    G.add_edge("X", "Z", G.directed_edge_name)
    G.add_edge("X", "Y", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"X"}, {"Y"})

    assert cad.adjustable()


    G = MAG()
    G.add_edge("X", "Z", G.directed_edge_name)
    G.add_edge("Z", "Y", G.directed_edge_name)
    G.add_edge("U", "X", G.directed_edge_name)
    G.add_edge("U", "Y", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"X"}, {"Y"})

    assert not cad.adjustable()


    #  CPDAGs

    G = PAG()
    G.add_edge("I", "X", G.directed_edge_name)
    G.add_edge("Z", "X", G.directed_edge_name)
    G.add_edge("A", "X", G.directed_edge_name)
    G.add_edge("X", "Y", G.directed_edge_name)
    G.add_edge("Z", "Y", G.directed_edge_name)
    G.add_edge("B", "Y", G.directed_edge_name)
    G.add_edge("B", "Z", G.circle_edge_name)
    G.add_edge("Z", "B", G.circle_edge_name)
    G.add_edge("A", "B", G.circle_edge_name)
    G.add_edge("B", "A", G.circle_edge_name)
    G.add_edge("A", "Z", G.circle_edge_name)
    G.add_edge("Z", "A", G.circle_edge_name)
    G.add_edge("A", "I", G.circle_edge_name)
    G.add_edge("I", "A", G.circle_edge_name)

    cad = CompleteAdjustment(G, {"X"},{"Y"})

    assert cad.adjustable()

    # MAG

    G = MAG()
    G.add_edge("A", "B", G.directed_edge_name)
    G.add_edge("B", "C", G.directed_edge_name)
    G.add_edge("C", "D", G.directed_edge_name)
    G.add_edge("D", "E", G.directed_edge_name)
    G.add_edge("A", "E", G.directed_edge_name)
    G.add_edge("F", "C", G.directed_edge_name)
    G.add_edge("F", "E", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"A", "D"}, {"E","F"})

    assert cad.adjustable()

    G = MAG()
    G.add_edge("A", "B", G.directed_edge_name)
    G.add_edge("B", "C", G.directed_edge_name)
    G.add_edge("C", "D", G.directed_edge_name)
    G.add_edge("D", "E", G.directed_edge_name)
    G.add_edge("A", "E", G.directed_edge_name)
    G.add_edge("F", "C", G.directed_edge_name)
    G.add_edge("F", "E", G.directed_edge_name)
    G.add_edge("A", "F", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"A", "D"}, {"E","F"} )

    assert not cad.adjustable()


    G = MAG()
    G.add_edge("A", "B", G.directed_edge_name)
    G.add_edge("B", "C", G.directed_edge_name)
    G.add_edge("C", "D", G.directed_edge_name)
    G.add_edge("D", "E", G.directed_edge_name)
    G.add_edge("A", "F", G.directed_edge_name)
    G.add_edge("F", "E", G.directed_edge_name)
    G.add_edge("G", "F", G.directed_edge_name)
    G.add_edge("G", "C", G.directed_edge_name)
    G.add_edge("H", "A", G.directed_edge_name)
    G.add_edge("I", "A", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"A", "D"}, {"E"} )

    assert cad.adjustable()

    G = MAG()
    G.add_edge("B", "A", G.directed_edge_name)
    G.add_edge("C", "B", G.directed_edge_name)
    G.add_edge("C", "D", G.directed_edge_name)
    G.add_edge("E", "D", G.directed_edge_name)
    G.add_edge("E", "F", G.directed_edge_name)
    G.add_edge("F", "A", G.directed_edge_name)
    G.add_edge("A", "D", G.directed_edge_name)

    cad = CompleteAdjustment(G, {"A", "C"}, {"D"})

    assert not cad.adjustable()

    # PAG

    G = PAG()
    G.add_edge("A", "B", G.directed_edge_name)
    G.add_edge("B", "C", G.directed_edge_name)
    G.add_edge("C", "D", G.directed_edge_name)
    G.add_edge("D", "E", G.directed_edge_name)
    G.add_edge("A", "F", G.directed_edge_name)
    G.add_edge("F", "E", G.directed_edge_name)
    G.add_edge("F", "C", G.bidirected_edge_name)
    G.add_edge("H", "A", G.directed_edge_name)
    G.add_edge("I", "A", G.directed_edge_name)
    G.add_edge("A", "H", G.circle_edge_name)
    G.add_edge("A", "I", G.circle_edge_name)

    cad = CompleteAdjustment(G, {"A", "D"}, {"E"} )

    assert cad.adjustable()



