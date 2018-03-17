import re
line = (" A Turing machine is a device that manipulates "
            "symbols on a strip of tape according to a table "
            "of rules. Despite its simplicity, a Turing machine "
            "can be adapted to simulate the logic of any computer "
            "algorithm, and is particularly useful in explaining "
            "the functions of a CPU inside a computer. The 'Turing'"
            " machine was described by Alan Turing in 1936, who "
            "called it an""a(utomatic)-machine"". The Turing "
            "machine is not intended as a practical computing "
            "technology, but rather as a hypothetical device "
            "representing a computing machine. Turing machines "
            "help computer scientists understandthe limits of "
            "mechanical computation.")
print (line)
print ()
count = len(re.findall(r'\.', line))
print ("The number of lines in this paragraph:", count)