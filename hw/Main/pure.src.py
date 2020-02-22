from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Effect_Console"
                        , call(var('import_module'), "hw.Effect.Console.pure") )
           , assign_star( "ps_main"
                        , call( get_item(var("ps_Effect_Console"), "log")
                              , metadata( 10
                                        , 7
                                        , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\src\\Main.purs"
                                        , "🍝" ) ) )
           , assign("exports", record(("main", var("ps_main")))) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\src\\Main.purs", name="hw.Main.pure")
