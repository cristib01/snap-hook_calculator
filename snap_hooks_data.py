# Liste cu parametrii pentru fiecare snap-hook

parametrii_snap_hook = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "K (Geometric Factor)",
    "Z (Section Modulus)",
    "a (base) (Big base - Trapezoidal)",
    "b (base) (Small base - Trapezoidal)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "L3 (Length of support [2])",
    "r1 (Inner radius for circular)",
    "r2 (Outer radius for circular)",
    "R (Radius at neutral axis)",
    "c (Distance outer fiber - neutral axis)",
    "I (Moment of Inertia - Latch)",
    "r (Radius at base)"
]

parametrii_sh_rectangular = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
]

parametrii_sh_trapezoid = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "a (base) (Big base - Trapezoidal)",
    "b (base) (Small base - Trapezoidal)",
]

parametrii_sh_ring_segment = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "r1 (Inner radius for circular)",
    "r2 (Outer radius for circular)",
    "K (Geometric Factor)",
    "Z (Section Modulus)",
]

parametrii_sh_irregular = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "c (Distance outer fiber - neutral axis)",
    "Z (Section Modulus)",
]

parametrii_sh_l_shaped = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "ε (Strain)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "L3 (Length of support [2])",
    "R (Radius at neutral axis)",
]

parametrii_sh_u_shaped = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "ε (Strain)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "L3 (Length of support [2])",
    "R (Radius at neutral axis)",
]

# Definirea tipurilor de snap-hook-uri
snap_hooks = [
    {
        "nume": "A1 - 1",
        "tip": "Type 1",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA11T1.jpg"
    },
    {
        "nume": "A1 - 2",
        "tip": "Type 2",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA12T2.jpg"
    },
    {
        "nume": "A1 - 3",
        "tip": "Type 3",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA13T3.jpg"
    },
    {
        "nume": "A1 - 4",
        "tip": "Type 4",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA14T4.jpg"
    },
    {
        "nume": "A1 - 5",
        "tip": "Type 5",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA15T5.jpg"
    },
    {
        "nume": "A2T",
        "tip": "Type 2T",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA2T2T.jpg"
    },
    {
        "nume": "A5T",
        "tip": "Type 5T",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/rectangleA5T5T.jpg"
    },
    {
        "nume": "B1",
        "tip": "Constant",
        "caracteristica": "Trapezoid",
        "cale_imagine": "media/trapezoidB1constant.png"
    },
    {
        "nume": "B2",
        "tip": "Decrease 1/2",
        "caracteristica": "Trapezoid",
        "cale_imagine": "media/trapezoidB2decreasehalf.png"
    },
    {
        "nume": "B3",
        "tip": "Decrease 1/4",
        "caracteristica": "Trapezoid",
        "cale_imagine": "media/trapezoidB3decreasequarter.png"
    },
    {
        "nume": "C1",
        "tip": "Constant",
        "caracteristica": "Ring segment",
        "cale_imagine": "media/ringsegmentC1constant.png"
    },
    {
        "nume": "C2",
        "tip": "Decrease 1/2",
        "caracteristica": "Ring segment",
        "cale_imagine": "media/ringsegmentC2decreasehalf.png"
    },
    {
        "nume": "C3",
        "tip": "Decrease 1/4",
        "caracteristica": "Ring segment",
        "cale_imagine": "media/ringsegmentC3decreasequarter.png"
    },
    {
        "nume": "D1",
        "tip": "Constant",
        "caracteristica": "Irregular",
        "cale_imagine": "media/irregularD1constant.png"
    },
    {
        "nume": "D2",
        "tip": "Decrease 1/2",
        "caracteristica": "Irregular",
        "cale_imagine": "media/irregularD2decreasehalf.png"
    },
    {
        "nume": "D3",
        "tip": "Decrease 1/4",
        "caracteristica": "Irregular",
        "cale_imagine": "media/irregularD3decreasequarter.png"
    },
    {
        "nume": "L",
        "tip": "L-shaped",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/L-Shaped.jpg"
    },
    {
        "nume": "U 1",
        "tip": "U-shaped Case 1",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/UshapedC1.jpg"
    },
    {
        "nume": "U 2",
        "tip": "U-shaped Case 2",
        "caracteristica": "Rectangle",
        "cale_imagine": "media/UshapedC2.jpg"
    },
]

# Adaugarea listei de parametrii in fiecare dicționar
for snap_hook in snap_hooks:
    if snap_hook["nume"] in ["A1 - 1", "A1 - 2", "A1 - 3", "A1 - 4", "A1 - 5", "A2T", "A5T"]:
        snap_hook["campuri"] = parametrii_sh_rectangular
    elif snap_hook["nume"] in ["B1", "B2", "B3"]:
        snap_hook["campuri"] = parametrii_sh_trapezoid
    elif snap_hook["nume"] in ["C1", "C2", "C3"]:
        snap_hook["campuri"] = parametrii_sh_ring_segment
    elif snap_hook["nume"] in ["D1", "D2", "D3"]:
        snap_hook["campuri"] = parametrii_sh_irregular
    elif snap_hook["nume"] in ["L"]:
        snap_hook["campuri"] = parametrii_sh_l_shaped
    elif snap_hook["nume"] in ["U 1", "U 2"]:
        snap_hook["campuri"] = parametrii_sh_u_shaped
