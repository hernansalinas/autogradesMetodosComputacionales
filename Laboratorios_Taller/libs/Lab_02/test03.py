
import random
import numpy as np
import math as mt
config_ = add_configurations()




try:
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Números abundates, la variable debe ser booleana  ", \
                            type(True),\
                            type(numeros_semiperfectos(8)),\
                            "numeros_semiperfectos",\
                            False)
                            
    
    
    ND = np.array([12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108 , 112, 114, 120])
    index = random.choice(range(len(ND)))
    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                        f"Comprobando si el número {ND[index]} es abundate   ", \
                        True,\
                        numeros_semiperfectos(ND[index]),\
                        "numeros_semiperfectos",\
                        False)

    NND = np.array([1,2,3,4,5,6,7,8,9,10,11,13,19,21,23])
    index_ = random.choice(range(len(NND)))

    config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Comprobando si el 6 es un número es abundante   ", \
                            False,\
                            numeros_semiperfectos(NND[index_]),\
                            "numeros_semiperfectos",\
                            False)



    runTest_v1(config_)


except:
  print("La función no ha sido definda o el numero de argumento no es el adecuado")
  
  #runTest_v1(config_)


