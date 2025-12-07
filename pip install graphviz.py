from graphviz import Digraph

dot = Digraph('Mindmap', format='png')
dot.attr(rankdir='TB', bgcolor='white')

# Node style
style = {'shape': 'box', 'style': 'rounded,filled', 'color':'black', 'fillcolor':'#f2f2f2'}

dot.node("A", "1. Physical Model\nPorous fin, LTNE", **style)
dot.node("B", "2. Porous Flow Physics\nDarcy + Boussinesq", **style)
dot.node("C", "3. Energy Equations\nFluid + Solid", **style)
dot.node("D", "4. Radiation + Linearisation", **style)
dot.node("E", "5. Non-Dimensionalisation\nθ, Bi, Ra, κ, φ, Rd, R1, τ", **style)
dot.node("F", "6. LTNE ODE System\nCoupled ODEs + BCs", **style)
dot.node("G", "7. AGM Method\nTrial functions + collocation", **style)
dot.node("H", "8. Outputs\nθf, θs, Nu_f, Nu_s, Nu_t", **style)

# Connections
dot.edges([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "F"),
    ("A", "E"),
    ("E", "F"),
    ("F", "G"),
    ("G", "H")
])

dot.render("porous_fin_mindmap", view=True)
