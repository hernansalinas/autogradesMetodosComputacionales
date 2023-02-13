
import numpy as np
import math as mt
config_ = add_configurations()




try:
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Calcular  el  factorial de un número entero ", \
                            mt.factorial(8),\
                            factorial(8),\
                            "factorial",\
                            False)
                            

  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "Prueba para valores negativos ", \
                          type("a"),\
                          type(factorial(-1)),\
                          "factorial",\
                          True)


  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "Prueba para valores reales ", \
                          type("a"),\
                          type(factorial(1.2)),\
                          "factorial",\
                          True)


  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "Prueba para el factorial de 0 ", \
                          mt.factorial(0),\
                          factorial(0),\
                          "factorial",\
                          True)




  runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


