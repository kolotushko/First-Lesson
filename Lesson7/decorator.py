class Checker:
    def Check(self, *exc_types):
     def Check1(function):
        def Check2(*args, **kwargs):
            try:
                print(function(*args, **kwargs))
            except Exception as ex:
                print(ex)
                return Check2
            return Check1
    @Check(NameError, TypeError, ZeroDivisionError, Exception)
    def Calculate(self, expresion):

