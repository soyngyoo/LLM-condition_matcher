import random

# Similarity (c1) prompts (5 variations each)


# c1_values = [0.0005, 0.005, 0.05, 0.5, 5]; % Similarity (0.0005 <= c1 <= 5) # 5 levels
'''
0.0005 (새로 추가): 가장 극단적이고 혁신적인 디자인을 설명합니다.
0.005 (새로 추가): 매우 비전통적이고 대담한 디자인을 설명합니다.
0.05 (기존): 약간 수정하여 더 혁신적인 느낌을 강조했습니다.
0.5 (기존): 거의 그대로 유지했습니다.
5 (기존): 가장 전통적인 디자인을 설명하도록 약간 수정했습니다.

'''

c1_descriptions = {
    0.0005: ["an extremely radical design that completely breaks all conventions.",
             "a groundbreaking design that redefines wheel aesthetics.",
             "an avant-garde concept that challenges all preconceptions of wheel design.",
             "a futuristic design that's barely recognizable as a traditional wheel.",
             "an ultra-innovative approach that revolutionizes wheel design principles."],
    0.005: ["a highly unconventional design that pushes boundaries significantly.",
            "an audacious design that dramatically departs from traditional norms.",
            "a cutting-edge style that's far removed from typical wheel designs.",
            "an exceptionally creative design that stands out boldly.",
            "a pioneering design that introduces radical new concepts."],
    0.05: ["a highly varied design that significantly deviates from traditional styles.",
           "a bold design that breaks away from conventional norms.",
           "an innovative and original style, clearly different from typical wheels.",
           "a creative design that stands out from mainstream wheel designs.",
           "a distinctive design, incorporating many non-traditional elements."],
    0.5: ["a moderately original design with noticeable updates from traditional wheels.",
          "a balanced blend of traditional and modern elements, with clear changes.",
          "a creative interpretation of traditional designs with visible improvements.",
          "a redesign of classic styles with a modern twist.",
          "a balanced mix of old and new elements, creating a distinctive design."],
    5: ["a design that closely matches traditional wheels with minor changes.",
        "a traditional style with minimal modifications for a fresh look.",
        "a design that stays true to the original while adding small unique elements.",
        "a nearly identical design to conventional wheels with slight differences.",
        "an updated version of classic wheel design with subtle improvements."]
}

#c2_values = [0.0, 0.1, 0.2, 0.3, 0.4]  # LoadRatio (0 <= c2 <= 0.4) # 5 levels

'''
이제 5개 레벨의 load ratio 설명이 준비되었습니다. 각 레벨에 대한 주요 특징은 다음과 같습니다:

0.0: 오직 normal force만을 고려한 가장 단순하고 안정적인 디자인을 설명합니다.
0.1: 주로 normal force에 중점을 둔 디자인을 설명합니다. 이전 버전의 0.05 설명을 약간 수정했습니다.
0.2: normal force와 shear force가 균형을 이루는 디자인을 설명합니다. 기존 설명을 유지했습니다.
0.3 (새로 추가): shear force의 영향이 더 커진 디자인을 설명합니다.
0.4: shear force가 지배적인 가장 역동적이고 창의적인 디자인을 설명합니다. 기존 설명을 유지했습니다.

이렇게 하면 0.0부터 0.4까지 5개의 레벨로 점진적으로 변화하는 디자인 설명을 얻을 수 있습니다. 각 레벨은 이전 레벨보다 shear force의 영향이 더 강해지는 디자인을 나타냅니다.

'''

c2_descriptions = {
    0.0: ["spokes designed exclusively for normal force distribution, resulting in a perfectly clean and solid appearance.",
          "an extremely simple and highly stable design focusing solely on normal force distribution.",
          "a remarkably clean and solid spoke design optimized purely for handling normal forces.",
          "perfectly straight and extremely stable spokes that exclusively absorb normal loads.",
          "an elementary spoke design with perfect normal force distribution, ensuring maximum stability."],
    0.1: ["spokes primarily designed for normal force distribution, creating a clean and solid appearance.",
          "a simple and stable design focusing mainly on normal force distribution.",
          "a clean and solid spoke design optimized for handling mostly normal forces.",
          "a straight and stable spoke design that primarily absorbs normal loads.",
          "a simple spoke design with balanced normal force distribution, ensuring high stability."],
    0.2: ["a balanced mix of normal and shear forces, creating spokes with moderate windmill-like patterns.",
          "a balanced design that combines both normal and shear forces for a dynamic look.",
          "a blend of normal and shear forces resulting in slightly curved spokes.",
          "spokes with an equal mix of normal and shear forces, forming smooth curves.",
          "a combination of shear and normal forces that creates a dynamic and balanced spoke design."],
    0.3: ["a design with more emphasis on shear forces, resulting in pronounced windmill-like patterns.",
          "spokes shaped by increased shear forces, creating a more dynamic windmill-style pattern.",
          "a creative design driven by dominant shear forces, forming noticeable twisted spoke patterns.",
          "spokes that clearly twist and curve under increased shear forces, showing a distinct windmill-like structure.",
          "a dynamic spoke design where shear forces play a major role, creating an artistic and energetic pattern."],
    0.4: ["shear-force dominant spokes, creating a strong windmill-like effect for a highly dynamic and creative design.",
          "spokes shaped by strong shear forces, resulting in an intricate and pronounced windmill-style pattern.",
          "a bold and creative design driven by dominant shear forces, creating complex twisted spoke patterns.",
          "spokes that dramatically twist and curve under strong shear forces, forming a distinct windmill-like structure.",
          "a highly dynamic spoke design where shear forces clearly dominate, creating an artistic and energetic pattern."]
}
# Volume Ratio (c3) prompts (5 variations each)
#c3_values = [0.6, 0.7, 0.8, 0.9]; %VolumeRatio  # 4 levels
'''
c3 = 0.6 (가장 얇은 스포크):

현대적이고 가벼운 디자인을 강조합니다.
슬림하고 세련된 외관을 가진 얇은 스포크를 설명합니다.
미니멀리즘, 경량성, 속도감을 강조합니다.


c3 = 0.7 (중간 얇은 스포크):

내구성과 스타일의 균형을 강조합니다.
강도와 미학 사이의 완벽한 균형을 달성한 스포크를 설명합니다.
내구성과 세련된 외관을 결합합니다.


c3 = 0.8 (중간 두꺼운 스포크):

강도와 내구성을 강조하는 두껍고 대담한 스포크를 설명합니다.
고성능과 강도를 위해 설계된 스포크를 나타냅니다.
견고하고 강력한 인상을 주는 디자인을 강조합니다.


c3 = 0.9 (가장 두꺼운 스포크):

매우 두꺼운 스포크로 산업적이고 중장비 같은 외관을 강조합니다.
과도한 두께로 강력한 모습을 나타내는 산업 스타일의 스포크를 설명합니다.
거친 느낌과 극도의 내구성을 강조합니다.

'''

c3_descriptions = {
    0.6: ["delicate, slim spokes that highlight a modern, lightweight design.",
          "thin spokes that provide a sleek and lightweight appearance.",
          "minimalistic design with slim spokes that emphasize lightness.",
          "sleek and lightweight spokes that create a modern and agile look.",
          "slim spokes that emphasize flexibility and speed, giving the wheel a lightweight aesthetic."],
    0.7: ["balanced spokes that offer both durability and a stylish appearance.",
          "sturdy yet stylish spokes that achieve a perfect balance between strength and aesthetics.",
          "spokes that combine durability with a refined and fashionable look.",
          "moderately thick spokes that offer a balance between durability and style.",
          "spokes that blend strength and elegance, providing a durable and sleek design."],
    0.8: ["thick, bold spokes that emphasize strength and durability.",
          "robust spokes designed for maximum strength and durability.",
          "thick, powerful spokes that create a strong and durable look.",
          "heavy-duty spokes designed for high performance and strength.",
          "bold and thick spokes that give the wheel a solid and powerful impression."],
    0.9: ["extra-thick spokes, giving the wheel a heavy-duty, industrial appearance.",
          "industrial-style spokes with excessive thickness for a powerful look.",
          "extra-large spokes that give the wheel a rugged and durable exterior.",
          "oversized spokes that highlight strength and a heavy, robust feel.",
          "thick, heavy spokes that provide a durable and stable appearance for the wheel."]
}

# Radial Segments (pp) prompts (5 variations each) # 3 levels
'''
4개의 스포크 (pp = 4):

가장 단순한 디자인을 나타냅니다.
미니멀리즘과 간결함을 강조합니다.
균형 잡힌 모습과 단순한 외관을 제공합니다.


5개의 스포크 (pp = 5):

균형과 대칭을 강조합니다.
더 역동적인 모습을 제공합니다.
시각적으로 안정적이고 조화로운 패턴을 만듭니다.
클래식한 휠 디자인으로 묘사됩니다.


6개의 스포크 (pp = 6):

더 복잡하고 정교한 디자인을 나타냅니다.
시각적 깊이와 복잡성을 추가합니다.
세련되고 정교한 패턴을 만듭니다.

'''

pp_values = [4, 5, 6];
pp_descriptions = {
    4: ["a simple design with evenly spaced spokes.",
        "4-spoke design for a minimalist look.",
        "4 spokes create a clean and straightforward pattern.",
        "a basic design with 4 spokes, focusing on simplicity.",
        "a design with 4 spokes, giving it a balanced yet simple appearance."],
    
    5: ["a balanced design with 5 spokes, offering symmetry.",
        "5-spoke design for a more balanced and dynamic look.",
        "5 spokes create a visually stable and well-proportioned design.",
        "a classic wheel design with 5 spokes, providing a harmonious pattern.",
        "5 evenly spaced spokes offer a refined and balanced appearance."],
    
    6: ["a more intricate design with 6 spokes for added complexity.",
        "6-spoke design for a complex and detailed look.",
        "6 spokes create a visually rich and sophisticated pattern.",
        "a refined design with 6 spokes, adding depth and complexity.",
        "a detailed and intricate pattern with 6 spokes, offering visual depth and complexity."]
}
