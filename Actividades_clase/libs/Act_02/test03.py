
import random
import numpy as np
import math as mt
config_ = add_configurations()

import numpy as np

from ast import literal_eval
float_str = "0b100000000111011100100001111111111111111111111111111111111111111"
result = float(literal_eval(float_str))


try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "La salida debe ser un float ", \
                            type(2.0),\
                            type(number64("1111111")),\
                            "number64",\
                            False)
   
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Realizando prueba para un numero binario ", \
                            result,\
                            number64( '100000000111011100100001111111111111111111111111111111111111111'),\
                            "number64",\
                            True)
   


    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


