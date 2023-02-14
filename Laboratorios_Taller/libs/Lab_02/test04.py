
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
                            
    
    


    ND = np.array([6, 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88])



   # ND = np.array([12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108 , 112, 114, 120])
    index = random.choice(range(len(ND)))
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                        f"Comprobando si el número {ND[index]} es abundantes   ", \
                        True,\
                        numeros_abundantes(ND[index]),\
                        "numeros_abundantes",\
                        False)

    NND = np.array([1,2,3,4,5,7,8,9,10,13,19,21,23,31,47])
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


