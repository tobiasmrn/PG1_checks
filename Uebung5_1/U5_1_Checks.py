import check50
import check50.c

@check50.check()
def exists():
    """U5.c exists!"""
    check50.exists("U5_[].c", regex = True)

@check50.check(exists)
def compiles():
    """U5.c compiles!"""
    check50.c.compile("U5.c")

@check50.check(compiles)
def Steuerfrei():
    """500 Euro Einkommen -> Steuerfrei"""
    check50.run("./U5").stdin("500").stdout("Steuerfrei!\n").exit(0)

@check50.check(compiles)
def Test_10450():
    """10450 Euro Einkommen -> 23.1"""
    from re import match

    expected = "Sie müssen 23.1 Euro Steuern bezahlen!\n"
    actual = check50.run("./U5").stdin("10450").stdout()
    if not match(expected, actual):
        help = None
        if actual == "Sie müssen 23.10 Euro Steuern bezahlen!\n" :
            help = "Es soll auf eine Nachkommastelle gerundet werden! (%.1f))"
        elif actual == "Sie müssen 23.1 Euro Steuern bezahlen!" :
            help = "Eventuell fehlt ein Zeilenumbruch am Ende der Ausgabe! (\\n)"
        raise check50.Mismatch(expected, actual, help=help)

    
@check50.check(Test_10450)
def Test_33444():
    """33444 Euro Einkommen -> 3896.9"""
    check50.run("./U5").stdin("33444").stdout("Sie müssen 3896.9 Euro Steuern bezahlen!\n").exit(0)
