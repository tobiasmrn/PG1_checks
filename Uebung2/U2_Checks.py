import check50
import check50.c

@check50.check()
def exists():
    """U2.c exists!"""
    check50.exists("U2.c")

@check50.check(exists)
def compiles():
    """U2.c compiles!"""
    check50.c.compile("U2.c")

@check50.check(compiles)
def Test_00_plus_00():
    """00 + 00 = Uebertrag: 0 , Ergebnis: 00"""
    check50.run("./U2").stdout("Uebertrag: 0, Ergebnis: 00\n").exit(0)

@check50.check(compiles)
def Test_10_plus_01():
    """10 + 01 = Uebertrag: 0 , Ergebnis: 11"""
    check50.run("./U2").stdout("Uebertrag: 0, Ergebnis: 11\n").exit(0)
    
@check50.check(compiles)
def Test_11_plus_01():
    """11 + 01 = Uebertrag: 1 , Ergebnis: 00"""
    check50.run("./U2").stdout("Uebertrag: 1, Ergebnis: 00\n").exit(0)
    
@check50.check(compiles)
def Test_11_plus_11():
    """11 + 11 = Uebertrag: 1 , Ergebnis: 10"""
    check50.run("./U2").stdout("Uebertrag: 1, Ergebnis: 10\n").exit(0)


