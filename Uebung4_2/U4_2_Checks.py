import check50
import check50.c

@check50.check()
def exists():
    """U4_2.c exists!"""
    check50.exists("U4_2.c")

@check50.check(exists)
def compiles():
    """U4_2.c compiles!"""
    check50.c.compile("U4_2.c")
    
@check50.check(compiles)
def Test_22_7_2002():
    """22_7_2002"""
    check50.run("./U4_2").stdin("22").stdin("7").stdin("2002").stdout("Montag\n").exit(0)
    
@check50.check(compiles)
def Test_30_12_2045():
    """30_12_2045"""
    check50.run("./U4_2").stdin("30").stdin("12").stdin("2045").stdout("Samstag\n").exit(0)
    
@check50.check(compiles)
def Test_15_5_1956():
    """22_7_2002"""
    check50.run("./U4_2").stdin("15").stdin("5").stdin("1956").stdout("Dienstag\n").exit(0)
