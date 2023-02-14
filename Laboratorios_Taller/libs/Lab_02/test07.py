
import random
import numpy as np
import math as mt
config_ = add_configurations()




try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Números amigos, la variable debe ser booleana  ", \
                            type(True),\
                            type(numeros_amigos(220,284)),\
                            "numeros_amigos",\
                            False)
                            
    
    
    NA=[(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416), (63020, 76084) , (66928, 66992)]
    index = random.choice(range(len(NA)))
    
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                        f"Comprobando si los números {NA[index]} son amigos   ", \
                        True,\
                        numeros_amigos(*NA[index]),\
                        "numeros_amigos",\
                        False)

    NND=[(22, 24), (118, 110), (620, 292), (520, 564), (622, 68), (144, 156), (170, 196), (62, 50), (152, 64), (83, 52)]
    index_ = random.choice(range(len(NND)))

    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            f"Comprobando si  {NND[index_]} no es un número amigo   ", \
                            False,\
                            numeros_amigos(*NND[index_]),\
                            "numeros_amigos",\
                            False)



    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


