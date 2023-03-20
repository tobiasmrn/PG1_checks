import check50
import check50.c

@check50.check()
def exists():
    """U4_3.c exists!"""
    check50.exists("U4_3.c")

@check50.check(exists)
def compiles():
    """U4_3.c compiles!"""
    check50.c.compile("U4_3.c")

@check50.check(compiles)
def negative():
    """negative ERROR"""
    check50.run("./U4_3").stdin("-5").stdin("5").stdout("Das Ergebnis ist: 48\n").exit(0)

@check50.check(compiles)
def Test_1295():
    """1295"""
    check50.run("./U4_3").stdin("34").stdout("Das Ergebnis ist: 1295\n").exit(0)
    
@check50.check(compiles)
def Test_69():
    """69"""
    check50.run("./U4_3").stdin("69").stdout("Das Ergebnis ist: 5040\n").exit(0)
    
    
@check50.check(compiles)
def Test_420():
    """420"""
    check50.run("./U4_3").stdin("420").stdout("Das Ergebnis ist: 178083\n").exit(0)
