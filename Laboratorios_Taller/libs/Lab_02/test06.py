
import random
import numpy as np
import math as mt
config_ = add_configurations()



try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Números abundantes, la variable debe ser booleana  ", \
                            type(True),\
                            type(numeros_abundantes(8)),\
                            "numeros_abundantes",\
                            False)
                            
    
    




    ND = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])

   
    index = random.choice(range(len(ND)))
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                        f"Comprobando si el número {ND[index]} es abundantes   ", \
                        True,\
                        numeros_abundantes(ND[index]),\
                        "numeros_abundantes",\
                        False)

    NND = np.array([1,6,8,12,24,36,42,50])
    index_ = random.choice(range(len(NND)))

    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            f"Comprobando si el {NND[index_]} es un número  abundantes   ", \
                            False,\
                            numeros_abundantes(NND[index_]),\
                            "numeros_abundantes",\
                            False)



    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


