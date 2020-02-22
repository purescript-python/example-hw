from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_otherwise"
                        , metadata( 10
                                  , 13
                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\.spago\\prelude\\v4.1.1\\src\\Data\\Boolean.purs"
                                  , True ) )
           , assign("exports", record(("otherwise", var("ps_otherwise")))) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\.spago\\prelude\\v4.1.1\\src\\Data\\Boolean.purs", name="hw.Data.Boolean.pure")
