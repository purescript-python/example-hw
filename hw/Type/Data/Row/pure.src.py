from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_RProxy"
                        , block( define( "ps_RProxy"
                                       , [".this"]
                                       , block(var(".this")) )
                               , set_attr( var("ps_RProxy")
                                         , "value"
                                         , new(var("ps_RProxy")) )
                               , var("ps_RProxy") ) )
           , assign("exports", record(("RProxy", var("ps_RProxy")))) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\.spago\\prelude\\v4.1.1\\src\\Type\\Data\\Row.purs", name="hw.Type.Data.Row.pure")
