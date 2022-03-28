def getGameMap(task, map_number):

    if task == "task4":
        return task4[map_number], None

    if task == "task6":
        return task6[map_number], None


# Maps for task 4
task4 = [
# Map 0
"""\
BBEBBBBBBBBBBBBBBBB
B  B   B   B   B  B
B      B          B
BB BB BBB BBBBBBB B
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B   B      B
B BB BBBBBBBBB BBBB
B  B   B   B      B
B  B       B   B  B
B  B   B   B   B  B
B BBBBBBBBBBBBBBB B
B  B   B   B   B  B
B      B       B  B
B  B   B   B   B  B
BBBB BBBB BBB BBB B
B  B   B   B   B  B
B        P B      B
BBBBBBBBBBBBBBBBBBB""",
"""\
BBBBBEBBBBBBBBBBBBB
B  B   B   B      B
B        P B   B  B
B BB BBBBB BBBBB BB
B  B   B   B      B
B  B   B   B   B  B
B  B   B       B  B
B BB BBBBBBBBBBBBBB
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B          B
BB BBB BBBBBBBBB BB
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B       B  B
B BBBB BBB B BBBB B
B  B   B   B   B  B
B  B       B      B
BBBBBBBBBBBBBBBBBBB""",
"""\
BBBBBBBBBEBBBBBBBBB
B      B       B  B
B  B       B      B
BBBBBBBBBBBB BBB BB
B  B   B   B   B  B
B          B   B  B
B  B   B   B   B  B
B BBBBBBBB BBB B BB
B  B   B   B   B  B
B  B   B   B   B  B
B  B   B   B   B  B
B BB BBBBBBBBBBBB B
B  B       B   B  B
B  B   B          B
B      B   B P B  B
BBBBBBBBBBBBBBBB BB
B  B              B
B      B   B   B  B
BBBBBBBBBBBBBBBBBBB""",
"""\
BBBBBBBBBBBBBBBBBBB
B B       B       B
B B BBB B BBB BBBBB
B   B   B     B   B
B BBB BBB BBBBB B B
B B   B B B  P  B B
B B BBB B B BBBBB B
B B B     B B   B B
B B BBBBBBB B BBB B
B B     B   B     B
B BBBBB BBBBB BBBBB
B   B   B     B   B
BBB B B B BBBBBBB B
B B B B B B     B B
B B B BBB B BBB B B
B B B   B B   B   B
B B BBB B BBB BBB B
E     B       B   B
BBBBBBBBBBBBBBBBBBB"""
]

# Maps for task 6
task6 = [
# Map 0
"""\
BBBBBBBBBBBBBBBBBBB
B B       B       B
B B BBB B BBB BBBBB
B   B   B     B   B
B BBB BBB BBBBB B B
B B   B B B  P  B B
B B BBB B B BBBBB B
B B B     B B   B B
B B BBBBBBB B BBB B
B B     B   B     B
B BBBBB BBBBB BBBBB
B   B   B     B   B
BBB B B B BBBBBBB B
B B B B B B     B B
B B B BBB B BBB B B
B B B   B B   B   B
B B BBB B BBB BBB B
E     B       B   B
BBBBBBBBBBBBBBBBBBB"""]

