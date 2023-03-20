import check50
import check50.c

@check50.check()
def exists():
    """U4_1.c exists!"""
    check50.exists("U4_1.c")

@check50.check(exists)
def compiles():
    """U4.c compiles!"""
    check50.c.compile("U4_1.c")

@check50.check(compiles)
def Test_2():
    """2 Stueck"""
    check50.run("./U4_1").stdin("2").stdout("Gesamtpreis: 1.60\n").exit(0)
    
@check50.check(compiles)
def Test_3():
    """3 Stueck"""
    check50.run("./U4_1").stdin("3").stdout("Gesamtpreis: 2.40\n").exit(0)
    
@check50.check(compiles)
def Test_9():
    """9 Stueck"""
    check50.run("./U4_1").stdin("9").stdout("Gesamtpreis: 7.20\n").exit(0)
    
@check50.check(compiles)
def Test_49():
    """49 Stueck"""
    check50.run("./U4_1").stdin("49").stdout("Gesamtpreis: 38.00\n").exit(0)
    
@check50.check(compiles)
def Test_50():
    """50 Stueck"""
    check50.run("./U4_1").stdin("50").stdout("Gesamtpreis: 38.00\n").exit(0)
    
@check50.check(compiles)
def Test_72():
    """72 Stueck"""
    check50.run("./U4_1").stdin("72").stdout("Gesamtpreis: 54.70\n").exit(0)
    
@check50.check(compiles)
def Test_72():
    """123 Stueck"""
    check50.run("./U4_1").stdin("123").stdout("Gesamtpreis: 90.50\n").exit(0)
