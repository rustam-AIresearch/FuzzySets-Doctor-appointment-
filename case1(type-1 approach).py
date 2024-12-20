import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# STUDENT NAME AND ID : Rustam Guliyev (20653127)

headache = ctrl.Antecedent(np.arange(0, 11, 0.1), 'headache')
temperature = ctrl.Antecedent(np.arange(30, 45, 0.1), 'temperature')
age = ctrl.Antecedent(np.arange(0, 130, 0.1), 'age')
urgency = ctrl.Consequent(np.arange(0, 101, 0.1), 'urgency')

headache['low'] = fuzz.gbellmf(headache.universe, 2, 2, 0) 
headache['moderate'] = fuzz.gaussmf(headache.universe, 5, 1) 
headache['severe'] = fuzz.gbellmf(headache.universe, 2, 2, 10)  

age['baby'] = fuzz.trapmf(age.universe, [0, 0, 3, 4])  
age['minors'] = fuzz.trapmf(age.universe, [2, 11, 17, 18])
age['adults'] = fuzz.trimf(age.universe, [17,40,65])
age['elderly'] = fuzz.trapmf(age.universe, [50, 65, 130, 130]) 


# Define the membership functions
temperature['very low'] = fuzz.trapmf(temperature.universe, [30, 30, 35, 35.4]) 
temperature['low'] = fuzz.trimf(temperature.universe, [35, 35.4, 36.6])
temperature['normal'] = fuzz.trimf(temperature.universe, [35.4, 36.6, 38])
temperature['high'] = fuzz.trimf(temperature.universe, [36.6, 38, 39]) 
temperature['very high'] = fuzz.trapmf(temperature.universe, [38, 39, 45.0, 45.0]) 

# Define fuzzy membership functions for urgency
urgency['low'] = fuzz.gbellmf(urgency.universe, 30, 5, 0)
urgency['moderate'] = fuzz.gaussmf(urgency.universe, 50, 10)
urgency['high'] = fuzz.gbellmf(urgency.universe, 30, 5, 100)

#Visualizing graphs
temperature.view() 
age.view() 
headache.view()


rules = [
    # High Rules
    ctrl.Rule(temperature['very high'] | temperature['very low'], urgency['high']),
    ctrl.Rule(headache['severe'], urgency['high']),
    ctrl.Rule(antecedent=(age['baby'] | age['elderly']) & (headache['moderate'] | temperature['high'] | temperature['low']), consequent=urgency['high']),
    ctrl.Rule(antecedent=(age['minors'] | age['adults']) & headache['moderate'] & (temperature['high'] | temperature['low']), consequent=urgency['high']),

    #Moderate Rules
    ctrl.Rule(age['baby'] | age['elderly'], urgency['moderate']),
    ctrl.Rule(antecedent=age['minors'] & headache['low'] & (temperature['high'] | temperature['low']), consequent=urgency['moderate']),
    ctrl.Rule(antecedent=(age['minors'] | age['adults']) & headache['moderate'] & temperature['normal'], consequent=urgency['moderate']),

    #Low Rules
    ctrl.Rule(antecedent=(age['minors'] | age['adults']) & headache['low'] & temperature['normal'], consequent=urgency['low']),
    ctrl.Rule(antecedent=age['adults'] & headache['low'] & (temperature['high'] | temperature['low']), consequent=urgency['low']),
]

#Setting the control system
urgency_control = ctrl.ControlSystem(rules)
urgency_simulation = ctrl.ControlSystemSimulation(urgency_control)


#Inputs boundaries
while True:
    headache=int(input("Headache from 0 to 10: "))
    if 0<=headache<=10:
        break
    print("Wrong input for headache")
while True:
    temperature=float(input("Input temperature from 30 to 45: "))
    if 30<=temperature<=45:
        break
    print("Wrong input for temperature")
while True:
    age=int(input("Input age from 0 to 130: "))
    if 0<=age<=130:
        break
    print("Wrong input for age")
     

#Simulation
urgency_simulation.input['headache'] = headache
urgency_simulation.input['temperature'] = temperature
urgency_simulation.input['age'] = age
urgency_simulation.compute()

#Outputs
print("Age:", age)
print("Headache:", headache)
print("Temperature:", temperature)
print(urgency_simulation.output['urgency'])
urgency.view(sim=urgency_simulation)
plt.show()


headache_range = np.arange(0, 11, 1)  
temperature_range = np.arange(30, 45, 1)  
age_ranges = np.arange(0, 131, 10)  

X, Y = np.meshgrid(headache_range, temperature_range)

# Function to compute overall urgency in a 3D surface 
def compute_overall_urgency():
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            overall_urgency = 0
            for age_level in age_ranges:
                urgency_simulation.input['headache'] = X[i, j]
                urgency_simulation.input['temperature'] = Y[i, j]
                urgency_simulation.input['age'] = age_level
                urgency_simulation.compute()
                overall_urgency += urgency_simulation.output['urgency'] * (1 / len(age_ranges)) 
            Z[i, j] = overall_urgency
    return Z

# Compute the overall urgency surface
Z = compute_overall_urgency()

# Plot the overall 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("Overall Urgency Surface")
ax.set_xlabel('Headache')
ax.set_ylabel('Temperature')
ax.set_zlabel('Urgency')
ax.view_init(30, 210)

plt.tight_layout()
plt.show() 

