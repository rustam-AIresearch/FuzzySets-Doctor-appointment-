from juzzyPython.generic.Tuple import Tuple
import matplotlib.pyplot as plt
import math 
from juzzyPython.generic.Plot import Plot
from juzzyPython.intervalType2.sets.IntervalT2MF_Gaussian import IntervalT2MF_Gaussian
from juzzyPython.type1.sets.T1MF_Triangular import T1MF_Triangular
from juzzyPython.type1.sets.T1MF_Gaussian import T1MF_Gaussian
from juzzyPython.type1.sets.T1MF_Gauangle import T1MF_Gauangle
from juzzyPython.intervalType2.sets.IntervalT2MF_Triangular import IntervalT2MF_Triangular 
from juzzyPython.intervalType2.sets.IntervalT2MF_Trapezoidal import IntervalT2MF_Trapezoidal
from juzzyPython.intervalType2.sets.IntervalT2MF_Gauangle import IntervalT2MF_Gauangle
from juzzyPython.intervalType2.system.IT2_Antecedent import IT2_Antecedent
from juzzyPython.intervalType2.system.IT2_Consequent import IT2_Consequent
from juzzyPython.intervalType2.system.IT2_Rule import IT2_Rule
from juzzyPython.intervalType2.system.IT2_Rulebase import IT2_Rulebase
from juzzyPython.generic.Input import Input
from juzzyPython.generic.Output import Output
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal

# STUDENT NAME AND ID: Rustam Guliyev (20653127)


# Inputs
age_input = Input('Age', Tuple(0, 130))
urgency_output = Output('Urgency', Tuple(0, 100))
temperature_input = Input('Temperature', Tuple(0, 100))
headache_input = Input('Headache', Tuple(0, 10))

plot = Plot()
# Define Type-2 Membership Functions for Headache used for Type-1 

#headache['low'] = fuzz.gbellmf(headache.universe, 2, 2, 0) 
#headache['moderate'] = fuzz.gaussmf(headache.universe, 5, 1) 
#headache['severe'] = fuzz.gbellmf(headache.universe, 2, 2, 10)  

# Low Headache
headache_low_UMF = T1MF_Gauangle('Headache Low UMF', 0,0,3)
headache_low_LMF = T1MF_Gauangle('Headache Low LMF', 0,0,1) 
headache_low = IntervalT2MF_Gauangle('Headache Low', headache_low_UMF, headache_low_LMF)

# Moderate Headache
headache_moderate_UMF = T1MF_Gauangle('Headache Moderate UMF', 2,5,7)  
headache_moderate_LMF = T1MF_Gauangle('Headache Moderate LMF', 2,4,7)  
headache_moderate = IntervalT2MF_Gauangle('Headache Moderate', headache_moderate_UMF, headache_moderate_LMF)

# Severe Headache
headache_severe_UMF = T1MF_Gauangle('Headache Severe UMF', 6,10,10)  
headache_severe_LMF = T1MF_Gauangle('Headache Severe LMF', 7,10,10)  
headache_severe = IntervalT2MF_Gauangle('Headache Severe', headache_severe_UMF, headache_severe_LMF)


# Define Type 2 membership functions for temperature (Upper and lower boundaries) used for Type-1

#temperature['very low'] = fuzz.trapmf(temperature.universe, [30, 30, 35, 35.4]) 
#temperature['low'] = fuzz.trimf(temperature.universe, [35, 35.4, 36.6])
#temperature['normal'] = fuzz.trimf(temperature.universe, [35.4, 36.6, 38])
#temperature['high'] = fuzz.trimf(temperature.universe, [36.6, 38, 39]) 
#temperature['very high'] = fuzz.trapmf(temperature.universe, [38, 39, 45.0, 45.0]) 

# Very Low Temperature
temp_very_low_UMF = T1MF_Trapezoidal('Temperature Very Low UMF', [30, 30.0, 35.4, 35.6])  
temp_very_low_LMF = T1MF_Trapezoidal('Temperature Very Low LMF', [30.2, 30.5, 34.8, 35.2]) 
temp_very_low = IntervalT2MF_Trapezoidal('Temperature Very Low', temp_very_low_UMF, temp_very_low_LMF)

temp_low_UMF = T1MF_Triangular('Temperature Low UMF', 34.5, 35.4, 36.9)  
temp_low_LMF = T1MF_Triangular('Temperature Low LMF', 35.2, 35.4, 36.4)  
temp_low = IntervalT2MF_Triangular('Temperature Low', temp_low_UMF, temp_low_LMF)

# Normal Temperature
temp_normal_UMF = T1MF_Triangular('Temperature Normal UMF', 35.2, 36.6, 38.8) 
temp_normal_LMF = T1MF_Triangular('Temperature Normal LMF', 35.6, 36.6, 37.8)  
temp_normal = IntervalT2MF_Triangular('Temperature Normal', temp_normal_UMF, temp_normal_LMF)

# High Temperature
temp_high_UMF = T1MF_Triangular('Temperature High UMF', 36.4, 38.0, 39.5)  
temp_high_LMF = T1MF_Triangular('Temperature High LMF', 36.8, 38.0, 39.0) 
temp_high = IntervalT2MF_Triangular('Temperature High', temp_high_UMF, temp_high_LMF)

# Very High Temperature
temp_very_high_UMF = T1MF_Trapezoidal('Temperature Very High UMF',[37.8,39.0,45,45])  
temp_very_high_LMF = T1MF_Trapezoidal('Temperature Very High LMF', [38.2, 39.2, 44,44])  
temp_very_high = IntervalT2MF_Trapezoidal('Temperature Very High', temp_very_high_UMF, temp_very_high_LMF)



# Define Type 2 membership functions for age (Upper and lower boundaries) used for Type-1

# age['baby'] = fuzz.trapmf(age.universe, [0, 0, 3, 4])  
# age['minors'] = fuzz.trapmf(age.universe, [2, 11, 17, 18])
# age['adults'] = fuzz.trimf(age.universe, [17,40,65])
# age['elderly'] = fuzz.trapmf(age.universe, [50, 65, 130, 130]) 

# Baby
baby_UMF = T1MF_Trapezoidal('Age Baby UMF', [0, 0, 4, 5])
baby_LMF = T1MF_Trapezoidal('Age Baby LMF', [0, 0, 3, 4])
baby = IntervalT2MF_Trapezoidal('Age Baby', baby_UMF, baby_LMF)

# Minors
minors_UMF = T1MF_Trapezoidal('Age Minors UMF', [2, 9, 17, 19])
minors_LMF = T1MF_Trapezoidal('Age Minors LMF', [3, 10, 16, 18])
minors = IntervalT2MF_Trapezoidal('Age Minors', minors_UMF, minors_LMF)

# Adults
adult_UMF = T1MF_Triangular('Age Adult UMF', 17, 41, 66)
adult_LMF = T1MF_Triangular('Age Adult LMF', 18, 40, 65)
adult = IntervalT2MF_Triangular('Age Adult', adult_UMF, adult_LMF)

# Old people
elderly_UMF = T1MF_Trapezoidal('Age Elderly UMF', [50, 65, 130, 130])
elderly_LMF = T1MF_Trapezoidal('Age Elderly LMF', [51, 66, 130, 130])
elderly = IntervalT2MF_Trapezoidal('Age Elderly', elderly_UMF, elderly_LMF)


# Urgency - Output Membership Functions

# Define fuzzy membership functions for urgency
# urgency['low'] = fuzz.gbellmf(urgency.universe, 30, 5, 0)
# urgency['moderate'] = fuzz.gaussmf(urgency.universe, 50, 10)
# urgency['high'] = fuzz.gbellmf(urgency.universe, 30, 5, 100)

urgency_low_UMF =T1MF_Gaussian('Urgency low UMF', 0,15)
urgency_low_LMF = T1MF_Gaussian('Urgency low LMF',0,12)
urgency_low = IntervalT2MF_Gauangle('Urgency low', urgency_low_UMF, urgency_low_LMF)

urgency_moderate_UMF = T1MF_Gaussian('Urgency moderate UMF', 50, 10)
urgency_moderate_LMF = T1MF_Gaussian('Urgency moderate LMF', 50, 8)
urgency_moderate = IntervalT2MF_Gaussian('Urgency delayed', urgency_moderate_UMF, urgency_moderate_LMF)

urgency_high_UMF = T1MF_Gaussian('Urgency high UMF',  100,15)
urgency_high_LMF = T1MF_Gaussian('Urgency high LMF',  100,12)
urgency_high = IntervalT2MF_Gauangle('Urgency high', urgency_high_UMF, urgency_high_LMF)


# Create Antecedents for temperature, headache, and age
# Antecedents headache
headache_low_antecedent = IT2_Antecedent(headache_low, headache_input, 'low')
headache_moderate_antecedent = IT2_Antecedent(headache_moderate, headache_input, 'moderate')
headache_severe_antecedent = IT2_Antecedent(headache_severe, headache_input, 'severe')

# Antecedents temperature 
temp_very_low_antecedent = IT2_Antecedent(temp_very_low, temperature_input, 'very low')
temp_low_antecedent = IT2_Antecedent(temp_low, temperature_input, 'low')
temp_normal_antecedent = IT2_Antecedent(temp_normal, temperature_input, 'normal')
temp_high_antecedent = IT2_Antecedent(temp_high, temperature_input, 'high')
temp_very_high_antecedent = IT2_Antecedent(temp_very_high, temperature_input, 'very high')

# Antecedents age
baby_antecedent = IT2_Antecedent(baby, age_input, 'baby')
minors_antecedent = IT2_Antecedent(minors, age_input, 'minors')
adults_antecedent = IT2_Antecedent(adult, age_input, 'adults')
elderly_antecedent = IT2_Antecedent(elderly, age_input, 'elderly')

# Consequent urgency 
urgency_low_consequent = IT2_Consequent(urgency_low, urgency_output, 'low')  
urgency_moderate_consequent = IT2_Consequent(urgency_moderate, urgency_output, 'moderate')
urgency_high_consequent = IT2_Consequent(urgency_high, urgency_output, 'high')


# General Rules (General Priority for Extreme Temperatures and Severe Headache)
rule1 = IT2_Rule([temp_very_high_antecedent], consequent=urgency_high_consequent)
rule2 = IT2_Rule([temp_very_low_antecedent], consequent=urgency_high_consequent)
rule3 = IT2_Rule([headache_severe_antecedent], consequent=urgency_high_consequent)

#High rules for Baby
rule4 = IT2_Rule([baby_antecedent, temp_high_antecedent], consequent=urgency_high_consequent)
rule5 = IT2_Rule([baby_antecedent, temp_low_antecedent], consequent=urgency_high_consequent)
rule5 = IT2_Rule([baby_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)

#High rules for Elderly
rule6 = IT2_Rule([elderly_antecedent, temp_high_antecedent], consequent=urgency_high_consequent)
rule7 = IT2_Rule([elderly_antecedent, temp_low_antecedent], consequent=urgency_high_consequent)
rule8 = IT2_Rule([elderly_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)

#High rules for Minors
rule9 = IT2_Rule([minors_antecedent, temp_high_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)
rule10 = IT2_Rule([minors_antecedent, temp_low_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)

#High rules for Adults
rule11 = IT2_Rule([adults_antecedent, temp_high_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)
rule12 = IT2_Rule([adults_antecedent, temp_low_antecedent, headache_moderate_antecedent], consequent=urgency_high_consequent)

# Rules for moderate urgency
rule13 = IT2_Rule([baby_antecedent], consequent=urgency_moderate_consequent)
rule14 = IT2_Rule([elderly_antecedent], consequent=urgency_moderate_consequent)

#Moderate Rules for Minors
rule15 = IT2_Rule([minors_antecedent, headache_low_antecedent, temp_high_antecedent], consequent=urgency_moderate_consequent)
rule16 = IT2_Rule([minors_antecedent, headache_low_antecedent, temp_low_antecedent], consequent=urgency_moderate_consequent)
rule17 = IT2_Rule([minors_antecedent, headache_moderate_antecedent, temp_normal_antecedent], consequent=urgency_moderate_consequent)

#Moderate Rules for Adults
rule18 = IT2_Rule([adults_antecedent, headache_moderate_antecedent, temp_normal_antecedent], consequent=urgency_moderate_consequent)

#Low rules for minors
rule19 = IT2_Rule([minors_antecedent, headache_low_antecedent, temp_normal_antecedent], consequent=urgency_low_consequent)

#Low rules for Adults
rule20 = IT2_Rule([adults_antecedent, headache_low_antecedent, temp_normal_antecedent], consequent=urgency_low_consequent)
rule21 = IT2_Rule([adults_antecedent, headache_low_antecedent, temp_high_antecedent], consequent=urgency_low_consequent)
rule22 = IT2_Rule([adults_antecedent, headache_low_antecedent, temp_low_antecedent], consequent=urgency_low_consequent)

rulebase = IT2_Rulebase()
# Adding All Rules to Rulebase
rules = [
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
    rule20, rule21,rule22,
]
#Adding rulebase to our system
for rule in rules:
    rulebase.addRule(rule)


#Plot for MFs
def plotMFs(name, sets, discretizationLevel):
    
    if not sets or discretizationLevel <= 0:
        raise ValueError("Invalid sets or discretizationLevel")

    plt.figure()
    plt.title(name)

    for i in range(len(sets)):
        plot.plotMF2(name.replace("Membership Functions",""),sets[i].getName(),sets[i],discretizationLevel,True)
    
    plt.legend()
    plt.show()


#Creating Surface Plot
def SurfacePlot(useCentroidDefuzz,input1Discs,input2Discs,unit = False) -> None:
        if unit:
            test = []
        temp_range = Tuple(34,45)
        incrX = temp_range.getSize()/(input1Discs-1.0)
        incrY = headache_input.getDomain().getSize()/(input2Discs-1.0)
        x = []
        y = []
        z = [ [0]*input1Discs for i in range(input2Discs)]

        for i in range(input1Discs):
            x.append(temp_range.getLeft() + i*incrX)
        for i in range(input2Discs):
            y.append(i*incrY)
        
        for x_ in range(input1Discs):
            temperature_input.setInput(x[x_])
            for y_ in range(input2Discs):
                headache_input.setInput(y[y_])
                if useCentroidDefuzz:
                    out = rulebase.evaluate(1).get(urgency_output)
                else:
                    out = rulebase.evaluate(0).get(urgency_output)
                if out == None or math.isnan(out):
                    z[y_][x_] = 0.0
                    if unit:
                        test.append(0.0)
                else:
                    z[y_][x_] = out
                    if unit:
                        test.append(out)
        if unit:
            return test
        plot.plotControlSurface(x,y,z,temperature_input.getName(),headache_input.getName(),urgency_output.getName())
        
# Evaluate Centroid and Type Reducing
def output_interval(age_lower, age_upper, headache_lower, headache_upper, temp_lower, temp_upper, red_t = 0):
    # Validate input parameters 
    if any(param < 0 for param in [age_lower, age_upper, headache_lower, headache_upper, temp_lower, temp_upper]):
        raise ValueError("Input parameters cannot be negative")
    
    
    age_input.setInputMF(T1MF_Trapezoidal("AgeMF", [age_lower, age_lower, age_upper, age_upper]))
    headache_input.setInputMF(T1MF_Gauangle("HeadacheMF", headache_lower, (headache_lower + headache_upper) / 2, headache_upper))
    temperature_input.setInputMF(T1MF_Gauangle("TempMF", temp_lower, (temp_lower + temp_upper)/2, temp_upper))
    
   
    # Evaluate the rulebase
    try:
        urgency_value = rulebase.evaluate(1).get(urgency_output)
    except Exception as e:
        raise RuntimeError(f"Error in rulebase evaluation: {e}")

    return urgency_value  


def test():
    plotMFs("Temperature Membership Functions", [temp_very_low, temp_low, temp_normal, temp_high,temp_very_high], 130)
    plotMFs("Age Membership Functions", [baby, minors, adult,elderly], 130)
    plotMFs("Headache Membership Functions", [headache_low, headache_moderate, headache_severe], 10)
    plotMFs("Urgency Membership Functions", [urgency_low,urgency_moderate, urgency_high], 100)
    #We have added the code for generating the control suface however it doesn't seem to work in VSC
    SurfacePlot(False,100,100)
    print(f"Urgency output: {output_interval(float(input("Please enter lower age: ")),float(input("Please enter upper age: ")),float(input("Please enter lower headache: ")),float(input("Please enter upper headache: ")),float(input("Please enter lower temperature: ")),float(input("Please enter upper temperature: ")),0)}")
    #If you want to see the rules which were added to this system,please uncomment the next line
    #print(rulebase.toString())


test()
