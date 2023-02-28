
import random
import numpy as np
import math as mt
config_ = add_configurations()




try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "La salida debe ser un string ", \
                            type("hola"),\
                            type(mybin(200)),\
                            "mybin",\
                            False)
   
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "La longitud del string debe ser de 8 ", \
                            len("11111111"),\
                            len(mybin(200)),\
                            "mybin",\
                            True)
    x = random.randint(0,255)
    y = bin(x)[2:].rjust(8, "0")
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            f"Para el número {x} su representacion es {y} ", \
                            y,\
                            len(mybin(200)),\
                            "mybin",\
                            False)
  


    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


