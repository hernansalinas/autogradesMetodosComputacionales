
Libreries description in bin folder


To realized the unit test of any function, variable or result we need instance the object add_configuration, and use the follow methods:

- add_configuration.append_(nameClass.nameMethod, "name of questions", variable, dependence, hint)

      Example:

      - config_.append_("testVariable.test_Equalfloat","x es un float", "x", False)


- add_configuration.append_(nameClass.nameMethod, "name of questions", ("name_function1",[params]),("name_function2",[params]), dependence, hint)

      Example:

      - config_.append_function("testOneOneFunction.test_Equalfunctions",\
                        "Crear una funcion que sume dos numeros", \
                        ("sum_expected",[1,1]),\
                        ("sum_test8",[1,1]) ,\
                        True, "Esto es un ayuda")


- add_configuration.append_(nameClass.nameMethod, "name of questions", expected value,("name_function2",[params]), dependence, hint)

      Example:

      - config_.append_function_values("testOneValuesFunction".test_Expectedvalue",\
                        "Test de la funcion f", \
                        [2,1],\
                        ("sum_test",[1,1]) ,\
                        True)




where:

    - nameClass.nameMethod: This class is inheritance from the object  unittest.TestCase in the libraries the this program.
    - "name of question": Comentary for the user for show in the box html.
    -  "variable" : Define the name of variable as sting.
    - "dependence": depende is true if the question has dependence of before  question, or false if doesn't have dependence
     - "hint": If the user want define help for the unit test. It is no necessary define.
     
     - The function can be define as tuple with 2 in, the first value is a string with the name of function and the second is list with the input params of the functions
     - the expect value can be define as a constant, list, tuple, dictionary etc.


Diferent method can be used if you add new methods for follows class:

  - testVariable
  - testOneOneFunction
  - testOneValuesFunction

You can use the documentation https://docs.python.org/3/library/unittest.html for employing assert functions of define you own comparative methods.


# List and short description of class used:
### Class

- testVariable: This class has the methods for indentify the variables is define, is string or  float. 
- testOneOneFunction: This calss has the medthods for realized the comparison between two functions 
- testOneValuesFunction: This class has the mehthods for realized the comparison with some  expected value and the evaluation of the function in some value

- StatePointsV1(): Define the state of each test that you realized
- add_configurations: Define the configuration for the runtest_v1 class
- html_generation: Generations of html

### Functions
- extract_message: extract one part of the  error in the unit test 
- runTest_v1: run unit test, 



Arquitectura recomendada para los archivos.


```Markdown

Test_labs
--------libUnitTest1.py
--------Labs
        -----Lab01
             --Lib_test1.py
             --test_1.py # se recomienda encriptar
         -----Lab01 
             --Lib_test2.py
             --test_2.py # se recomienda encriptar

Labs_student/
--------Labs01/notebook.ipynb 
--------Labs02
--------Labs03
--------Labs04
--------Labs05
--------Labs06

%run test_labs/libUnitTest1.py
%run test_labs/Labs/Lab01/Lab_test1py
````
