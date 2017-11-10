  _____       ______             
 |  __ \     |  ____|            
 | |__) |   _| |__ _   _ ________
 |  ___/ | | |  __| | | |_  /_  /
 | |   | |_| | |  | |_| |/ / / / 
 |_|    \__, |_|   \__,_/___/___|
         __/ |                   
        |___/                    

README

NB: THIS PROJECT IS NOT COMPATIBLE WITH PYTHON3!

Pyfuzz is a fuzzy rule based system implamented in Python 2.7 for the 2017 Computational Inteligence practical assessment at the University of Aberdeen. It makes use of text parsing to extract data from text files, basic fuzzy logic, an inference engine and the use of weighted averages for defuzzification.

Text file containing must be structed in the following way:

For the rulebase:

<RuleBaseName>

Rule 1: if <variable1> is <value1> [and|or] [<variablen> is <valuen>] then <variablei> is <valuej>
Rule 2: if <variable2> is <value2> [and|or] [<variablen> is <valuen>] then <variablei> is <valuej>
Rule 3: if <variable3> is <value3> [and|or] [<variablen> is <valuen>] then <variablei> is <valuej>
Rule 4: if <variable4> is <value4> [and|or] [<variablen> is <valuen>] then <variablei> is <valuej>
...


For setting up the fuzzy sets for each variable:
<variableName1>
<valueName1> <4Tuple1>
<valueName2> <4Tuple2>
...

And for the measurements:
<variableName1> = <RealValue1>
<variableNamen> = <RealValue2>

NB: THIS PROJECT IS NOT COMPATIBLE WITH PYTHON3!

CONTACT

If there are any issues do not hesitate to contact me on my student email: j.nicol.16@aberdeen.ac.uk






