import check50
import check50.c

@check50.check()
def exists():
    """U3.c exists!"""
    check50.exists("U3.c")

@check50.check(exists)
def compiles():
    """U3.c compiles!"""
    check50.c.compile("U3.c")

@check50.check(compiles)
def Test_50_10():
    """50 Euro - 10 Cent"""
    check50.run("./U3").stdin("50").stdin("10").stdout("Sie bekommen für Ihre 50 Euro 500 Münzen je 10 Cent!\n").exit(0)
    
@check50.check(compiles)
def Test_5_20():
    """5 Euro - 20 Cent"""
    check50.run("./U3").stdin("5").stdin("20").stdout("Sie bekommen für Ihre 5 Euro 25 Münzen je 20 Cent!\n").exit(0)
    
@check50.check(compiles)
def Test_50_10():
    """20 Euro - 50 Cent"""
    check50.run("./U3").stdin("20").stdin("50").stdout("Sie bekommen für Ihre 20 Euro 40 Münzen je 50 Cent!\n").exit(0)
    
@check50.check(compiles)
def Test_negative():
    """-100 - ERROR"""
    check50.run("./U3").stdin("-100").stdout("FEHLER: Falscher Betrag!\n").exit(1)
    
@check50.check(compiles)
def Test_30_Cent():
    """30 Cent - ERROR"""
    check50.run("./U3").stdin("10").stdin("30").stdout("FEHLER: Falsche Muenzart!\n").exit(1)

