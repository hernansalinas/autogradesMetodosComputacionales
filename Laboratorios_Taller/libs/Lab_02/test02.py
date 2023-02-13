
import random
import numpy as np
import math as mt
config_ = add_configurations()




try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Números defectivos, la variable debe ser booleana  ", \
                            type(True),\
                            type(numeros_defectivos(8)),\
                            "numeros_defectivos",\
                            False)
                            
    
    
    ND = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27, 29, 31, 32 , 33, 34, 35, 37, 38, 39, 41, 43, 44, 45, 46, 47, 49, 50])
    index = random.choice(range(len(ND)))
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                        f"Comprobando si el número {ND[index]} es defectivo   ", \
                        True,\
                        numeros_defectivos(ND[index]),\
                        "numeros_defectivos",\
                        False)

    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Comprobando si el 6 es un número es defectivo   ", \
                            False,\
                            numeros_defectivos(6),\
                            "numeros_defectivos",\
                            False)



    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


