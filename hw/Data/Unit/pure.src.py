from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call(var('import_module'), "hw.ffi.Data.Unit") )
           , assign_star( "ps_Data_Show"
                        , call(var('import_module'), "hw.Data.Show.pure") )
           , assign_star( "ps_showUnit"
                        , new( get_item(var("ps_Data_Show"), "Show")
                             , define( None
                                     , ["ps_v"]
                                     , block( ret( metadata( 16
                                                           , 12
                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\.spago\\prelude\\v4.1.1\\src\\Data\\Unit.purs"
                                                           , "unit" ) ) ) ) ) )
           , assign( "exports"
                   , record( ("showUnit", var("ps_showUnit"))
                           , ("unit", get_item(var("$foreign"), "unit")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\v0.1\\hw\\.spago\\prelude\\v4.1.1\\src\\Data\\Unit.purs", name="hw.Data.Unit.pure")
