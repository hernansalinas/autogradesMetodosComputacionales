
import random
import numpy as np
import math as mt
config_ = add_configurations()

import numpy as np
def number32_(BIN):
    b_inverted=np.array(list(BIN)[::-1]).astype(int)    
    s=b_inverted[31]    
    be=b_inverted[23:31]
    i=np.arange(be.size)
    e=(be*(2**i)).sum()    
    bf=b_inverted[0:23]
    i_inverted=np.arange(1,bf.size+1)[::-1]
    numero=( (-1)**s/2**(127-e)  )*( 1 + (bf/2**i_inverted).sum() ) 
    return numero


try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "La salida debe ser un float ", \
                            type(2.0),\
                            type(number32("1111111")),\
                            "number32",\
                            False)
   
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Realizando prueba para un numero binario ", \
                            number32_("00111110001000000000000100010000"),\
                            number32( '00111110001000000000000100010000'),\
                            "number32",\
                            True)
   


    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


