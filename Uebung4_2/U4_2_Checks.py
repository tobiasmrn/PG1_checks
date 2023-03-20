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
