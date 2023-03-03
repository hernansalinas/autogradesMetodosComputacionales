
import random
import numpy as np
import math as mt
config_ = add_configurations()

import numpy as np

from ast import literal_eval
float_str = "0b100000000111011100100001111111111111111111111111111111111111111"
result = float(literal_eval(float_str))


try:
    b="0011111110001000000000000000000000000000000000000000000000000000"
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "La salida debe ser un float ", \
                            type(2.0),\
                            type(number64(b)),\
                            "number64",\
                            False)
   
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Realizando prueba para un numero binario ", \
                            0.01171875,\
                            number64(b)),\
                            "number64",\
                            True)
   


    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


