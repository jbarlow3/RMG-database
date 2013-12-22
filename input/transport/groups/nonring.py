#!/usr/bin/env python
# encoding: utf-8

"""
Note the Pc contributions are all the negative of what is in Table 3 of Joback's thesis.
The Tb contributions are from table 13.
"""

entry(
    index = 0, # another 0!!
    label = "R",
    group =
"""
1 * R {0,1,2}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> made up this empty entry."""),    ],
)

entry(
    index = 0, # another 0!!
    label = "C_centered",
    group =
"""
1 * C {0,1,2}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> made up this empty entry."""),    ],
)

entry(
    index = 0, # another 0!!
    label = "O_centered",
    group =
"""
1 * O {0,1}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> made up this empty entry."""),    ],
)
entry(
    index = 0, # another 0!!
    label = "S_centered",
    group =
"""
1 * S {0,1}
""",
    transportGroup = None,
    shortDesc = u"""Dummy node for head of tree""",
    longDesc = u"""""",
    history = [
        ("2013/03/14 12:53:03","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> made up this empty entry."""),    ],
)

entry(
    index = 1,
    label = "CsH3R",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0141,
        Pc = -0.0012,
        Vc = 65,
        Tb = 23.58,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsH3R""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 2,
    label = "CsH2R2",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0189,
        Pc = 0,
        Vc = 56,
        Tb = 22.88,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsH2R2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 3,
    label = "CsHR3",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
5 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0164,
        Pc = 0.0020,
        Vc = 41,
        Tb = 21.74,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsHR3""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 4,
    label = "CsR4",
    group =
"""
1 * C 0 {2,S} {3,S} {4,S} {5,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
5 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0067,
        Pc = 0.0043,
        Vc = 27,
        Tb = 18.25,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CsR4""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 5,
    label = "CdH2R",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 R!H 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0113,
        Pc = -0.0028,
        Vc = 56,
        Tb = 18.18,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdH2R""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 6,
    label = "CdHR2",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 R!H 0 {1,D}
3 R!H 0 {1,S}
4 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0129,
        Pc = -0.0006,
        Vc = 46,
        Tb = 24.96,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdHR2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 7,
    label = "CdR3",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 R!H 0 {1,D}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0117,
        Pc = 0.0011,
        Vc = 38,
        Tb = 24.14,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for CdR3""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 8,
    label = "CddR2",
    group =
"""
1 * C 0 {2,D} {3,D}
2 R!H 0 {1,D}
3 R!H 0 {1,D}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0026,
        Pc = 0.0028,
        Vc = 36,
        Tb = 26.15,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CddR2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 9,
    label = "CtHR",
    group =
"""
1 * C 0 {2,T} {3,S}
2 R!H 0 {1,T}
3 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0027,
        Pc = -0.0008,
        Vc = 46,
        Tb = 9.20,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CtHR""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 10,
    label = "CtR2",
    group =
"""
1 * C 0 {2,T} {3,S}
2 R!H 0 {1,T}
3 R!H 0 {1,S}

""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0020,
        Pc = 0.0016,
        Vc = 37,
        Tb = 27.38,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for CtR2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 11,
    label = "Alcohol",
    group =
"""
1 * O 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0741,
        Pc = 0.0112,
        Vc = 28,
        Tb = 92.88,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Alcohol""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 12,
    label = "Phenol",
    group =
"""
1 * O 0 {2,S} {3,S}
2 Cb 0 {1,S}
3 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0240,
        Pc = 0.0184,
        Vc = -25,
        Tb = 76.34,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Phenol""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 13,
    label = "Ether",
    group =
"""
1 * O 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0168,
        Pc = 0.0015,
        Vc = 18,
        Tb = 22.42,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ether""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 14,
    label = "Ketone_Ccentered",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 R!H 0 {1,S}
4 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0380,
        Pc = 0.0031,
        Vc = 62,
        Tb = 76.75,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ketone_Ccentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 15,
    label = "Ketone_Ocentered",
    group =
"""
1 * O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 R!H 0 {2,S}
4 R!H 0 {2,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ketone_Ocentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 16,
    label = "Aldehyde_Ccentered",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 R!H 0 {1,S}
4 H 0 {1,S}

""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0379,
        Pc = 0.0030,
        Vc = 82,
        Tb = 72.24,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Aldehyde_Ccentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 17,
    label = "Aldehyde_Ocentered",
    group =
"""
1 * O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 R!H 0 {2,S}
4 H 0 {2,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Aldehyde_Ocentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 18,
    label = "Acid_Ccentered",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S} {5,S}
4 R!H 0 {1,S}
5 H 0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0791,
        Pc = 0.0077,
        Vc = 89,
        Tb = 169.09,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ccentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 19,
    label = "Acid_Ocentered1",
    group =
"""
1 * O 0 {2,S} {3,S}
2 H 0 {1,S}
3 C 0 {1,S} {4,D} {5,S}
4 O 0 {3,D}
5 R!H 0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ocentered1""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 20,
    label = "Acid_Ocentered2",
    group =
"""
1 * O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 R!H 0 {2,S}
4 O 0 {2,S} {5,S}
5 H 0 {4,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Acid_Ocentered2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 21,
    label = "Ester_Ccentered",
    group =
"""
1 * C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S} {5,S}
4 R!H 0 {1,S}
5 R!H 0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0481,
        Pc = 0.0005,
        Vc = 82,
        Tb = 81.10,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ccentered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 22,
    label = "Ester_Ocentered1",
    group =
"""
1 * O 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 C 0 {1,S} {4,D} {5,S}
4 O 0 {3,D}
5 R!H 0 {3,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ocentered1""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 23,
    label = "Ester_Ocentered2",
    group =
"""
1 * O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 R!H 0 {2,S}
4 O 0 {2,S} {5,S}
5 R!H 0 {4,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ester_Ocentered2""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 24,
    label = "Od",
    group =
"""
1 * O 0 {2,D}
2 R!H 0 {1,D}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0143,
        Pc = 0.0101,
        Vc = 36,
        Tb = -10.50,
        structureIndex = 0,
    ),
    shortDesc = u"""nonring_library value for Od""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 25,
    label = "Thiol",
    group =
"""
1 * S 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0031,
        Pc = 0.0084,
        Vc = 63,
        Tb = 63.56,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Thiol""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 26,
    label = "Thioether",
    group =
"""
1 * S 0 {2,S} {3,S}
2 R!H 0 {1,S}
3 R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0119,
        Pc = 0.0049,
        Vc = 54,
        Tb = 68.78,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Thioether""",
    longDesc = 
u"""

""",
    history = [
        ("2013/03/14 12:15:49","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),    ],
)

entry(
    index = 27,
    label = "Ct-HN3t",
    group =
"""
1 * C 0 {2,T} {3,S}
2 N 0 {1,T}
3 H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0496,
        Pc = -0.0101,
        Vc = 91,
        Tb = 125.66,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for Ct-HN3t""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 28,
    label = "N_centered",
    group =
"""
1 * N {0,1,2}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N_centered""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 29,
    label = "N2d",
    group =
"""
1 * N2d {0,1,2}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N2d""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 30,
    label = "N3s",
    group =
"""
1 * N3s {0,1,2}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N3s""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 31,
    label = "N3s-RHH",
    group =
"""
1 * N3s  0  {2,S} {3,S} {4,S}
2   R!H  0  {1,S}
3   H    0  {1,S}
3   H    0  {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0243,
        Pc = 0.0109,
        Vc = 38,
        Tb = 73.23,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N3s-RHH""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 32,
    label = "N3s-RRH",
    group =
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   H   0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0130,
        Pc = 0.0114,
        Vc = 29,
        Tb = 50.17,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N3s-RRH""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 33,
    label = "N3s-RRR",
    group =
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0169,
        Pc = 0.0074,
        Vc = 9,
        Tb = 11.74,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N3s-RRR""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 34,
    label = "N3d",
    group =
"""
1 * N3d {0,1}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0255,
        Pc = -0.0099,
        Vc = 0, #no value in Joback
        Tb = 74.60,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N3d""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 35,
    label = "N5d",
    group =
"""
1 * N5d {0,1,2}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0,
        Pc = 0,
        Vc = 0,
        Tb = 0,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N5d""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

entry(
    index = 36,
    label = "N5d-OdOsR",
    group =
"""
1 * N5d 0 {2,D} {3,S} {4,S}
2   Od  0 {1,D}
3   Os  0 {1,S}
4   R   0 {1,S}
""",
    transportGroup = CriticalPointGroupContribution(
        Tc = 0.0437,
        Pc = 0.0064,
        Vc = 91,
        Tb = 152.54,
        structureIndex = 1,
    ),
    shortDesc = u"""nonring_library value for N5d-OdOsR""",
    longDesc = 
u"""

""",
    history = [
        ("2013/12/09 11:07:00","Jake Barlow <barlow.ja@husky.neu.edu>","action",
        """Jake Barlow <barlow.ja@husky.neu.edu> added entry from Joback's thesis."""),    ],
)

tree(
"""
L0: R
    L1: C_centered
        L2: CsH3R
        L2: CsH2R2
        L2: CsHR3
        L2: CsR4
        L2: CdH2R
        L2: CdR3
            L3: Ketone_Ccentered
            L3: Acid_Ccentered
            L3: Ester_Ccentered
        L2: CdHR2
            L3: Aldehyde_Ccentered
        L2: CddR2
        L2: CtHR
            L3: Ct-HN3t
        L2: CtR2
        
    L1: O_centered
        L2: Alcohol
            L3: Phenol
            L3: Acid_Ocentered1
        L2: Ether
            L3: Ester_Ocentered1
        L2: Od
            L3: Ketone_Ocentered
            L3: Aldehyde_Ocentered
            L3: Acid_Ocentered2
            L3: Ester_Ocentered2
                
    L1: S_centered
        L2: Thiol
        L2: Thioether
        
    L1: N_centered
        L2: N2d
        L2: N3s
            L3: N3s-RHH
            L3: N3s-RRH
            L3: N3s-RRR
        L2: N3d
        L2: N5d
            L3: N5d-OdOdR
"""
)