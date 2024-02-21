# Lists with parameters for each snap-hook

snap_hook_parameters = [
    "Material",
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "α' (Retraction Angle)"
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
    "r (Radius at base)",
    "Q (Deflection Magnification Factor)"
]

parameters_sh_rectangular_improved = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "α' (Retraction Angle)",
    "Q (Deflection Magnification Factor)"
]

parameters_sh_rectangular_classic = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "α' (Retraction Angle)"
]

parameters_sh_trapezoid = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "a (base) (Big base - Trapezoidal)",
    "b (base) (Small base - Trapezoidal)",
    "α' (Retraction Angle)"
]

parameters_sh_ring_segment = [
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
    "α' (Retraction Angle)"
]

parameters_sh_irregular = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "L (Length of Latch)",
    "α (Engagement Angle)",
    "ε (Strain)",
    "μ (Friction Coefficient)",
    "c (Distance outer fiber - neutral axis)",
    "Z (Section Modulus)",
    "α' (Retraction Angle)"
]

parameters_sh_l_shaped = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "ε (Strain)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "R (Radius at neutral axis)",
]

parameters_sh_u_shaped_c1 = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "ε (Strain)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "R (Radius at neutral axis)",
]

parameters_sh_u_shaped_c2 = [
    "E (Flexural Modulus)",
    "b (Base Width)",
    "t/h (Wall Thickness)",
    "ε (Strain)",
    "L1 (Length of slot)",
    "L2 (Length of support [1])",
    "L3 (Length of support [2])",
    "R (Radius at neutral axis)",
]

# Definition of snap-hook types
snap_hooks = [
    {
        "name": "Improved - Rectangular - Type 1",
        "type": "A1 - 1",
        "characteristic": "Rectangle",
        "image_path": "media/Uniform1Beam.jpg",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 2",
        "type": "A1 - 2",
        "characteristic": "Rectangle",
        "image_path": "media/Uniform2Beam.jpg",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 3",
        "type": "A1 - 3",
        "characteristic": "Rectangle",
        "image_path": "media/Uniform3Beam.jpg",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 4",
        "type": "A1 - 4",
        "characteristic": "Rectangle",
        "image_path": "media/Uniform4Beam.jpg",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 5",
        "type": "A1 - 5",
        "characteristic": "Rectangle",
        "image_path": "media/Uniform5Beam.jpg",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 2T",
        "type": "A2T",
        "characteristic": "Rectangle",
        "image_path": "media/Tapered2Beam.jpg",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "Improved - Rectangular - Type 5T",
        "type": "A5T",
        "characteristic": "Rectangle",
        "image_path": "media/Tapered5Beam.jpg",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "L Beam",
        "type": "L-shaped",
        "characteristic": "Rectangle",
        "image_path": "media/LBeam.jpg",
        "section_image_path": "media/LB.jpg"
    },
    {
        "name": "U Beam Case1",
        "type": "U-shaped Case 1",
        "characteristic": "Rectangle",
        "image_path": "media/UBeamCase1.jpg",
        "section_image_path": "media/UBCase1.jpg"
    },
    {
        "name": "U Beam Case2",
        "type": "U-shaped Case 2",
        "characteristic": "Rectangle",
        "image_path": "media/UBeamCase2.jpg",
        "section_image_path": "media/UBCase2.jpg"
    },
    {
        "name": "Classic - Rectangular - Constant",
        "type": "A1 - Constant",
        "characteristic": "Rectangle",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Classic - Rectangular - Decrease 1/2 - Y",
        "type": "A2 - Decrease 1/2",
        "characteristic": "Rectangle",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Rectangular - Decrease 1/4 - Z",
        "type": "A3 - Decrease 1/4",
        "characteristic": "Trapezoid",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/QuarterDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Trapezoid - Constant",
        "type": "B1 - Constant",
        "characteristic": "Trapezoid",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Classic - Trapezoid - Decrease 1/2 - Y",
        "type": "B2 - Decrease 1/2",
        "characteristic": "Trapezoid",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Trapezoid - Decrease 1/4 - Z",
        "type": "B3 - Decrease 1/4",
        "characteristic": "Trapezoid",
        "image_path": "media/Trapezoid1Beam.png",
        "section_image_path": "media/QuarterDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Ring segment - Constant",
        "type": "C1 - Constant",
        "characteristic": "Ring segment",
        "image_path": "media/Ring1Beam.png",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Classic - Ring segment - Decrease 1/2 - Y",
        "type": "C2 - Decrease 1/2",
        "characteristic": "Ring segment",
        "image_path": "media/Ring1Beam.png",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Ring segment - Decrease 1/4 - Z",
        "type": "C3 - Decrease 1/4",
        "characteristic": "Ring segment",
        "image_path": "media/Ring1Beam.png",
        "section_image_path": "media/QuarterDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Irregular - Constant",
        "type": "D1 - Constant",
        "characteristic": "Irregular",
        "image_path": "media/Irregular1Beam.png",
        "section_image_path": "media/ConstantSectionCase.png"
    },
    {
        "name": "Classic - Irregular - Decrease 1/2 - Y",
        "type": "D2 - Decrease 1/2",
        "characteristic": "Irregular",
        "image_path": "media/Irregular1Beam.png",
        "section_image_path": "media/HalfDecreaseSectionCase.png"
    },
    {
        "name": "Classic - Irregular - Decrease 1/4 - Z",
        "type": "D3 - Decrease 1/4",
        "characteristic": "Irregular",
        "image_path": "media/Irregular1Beam.png",
        "section_image_path": "media/QuarterDecreaseSectionCase.png"
    }
]

# Adding the parameters list to each dictionary
for snap_hook in snap_hooks:
    if snap_hook["name"] in ["Improved - Rectangular - Type 1", "Improved - Rectangular - Type 2",
                             "Improved - Rectangular - Type 3", "Improved - Rectangular - Type 4",
                             "Improved - Rectangular - Type 5", "Improved - Rectangular - Type 2T",
                             "Improved - Rectangular - Type 5T"]:
        snap_hook["fields"] = parameters_sh_rectangular_improved
    elif snap_hook["name"] in ["L Beam"]:
        snap_hook["fields"] = parameters_sh_l_shaped
    elif snap_hook["name"] in ["U Beam Case1"]:
        snap_hook["fields"] = parameters_sh_u_shaped_c1
    elif snap_hook["name"] in ["U Beam Case2"]:
        snap_hook["fields"] = parameters_sh_u_shaped_c2
    elif snap_hook["name"] in ["Classic - Rectangular - Constant", "Classic - Rectangular - Decrease 1/2 - Y",
                               "Classic - Rectangular - Decrease 1/4 - Z"]:
        snap_hook["fields"] = parameters_sh_rectangular_classic
    elif snap_hook["name"] in ["Classic - Trapezoid - Constant", "Classic - Trapezoid - Decrease 1/2 - Y",
                               "Classic - Trapezoid - Decrease 1/4 - Z"]:
        snap_hook["fields"] = parameters_sh_trapezoid
    elif snap_hook["name"] in ["Classic - Ring segment - Constant", "Classic - Ring segment - Decrease 1/2 - Y",
                               "Classic - Ring segment - Decrease 1/4 - Z"]:
        snap_hook["fields"] = parameters_sh_ring_segment
    elif snap_hook["name"] in ["Classic - Irregular - Constant", "Classic - Irregular - Decrease 1/2 - Y",
                               "Classic - Irregular - Decrease 1/4 - Z"]:
        snap_hook["fields"] = parameters_sh_irregular
