import pulp

model = pulp.LpProblem("Максимізація_виробництва_напоїв", pulp.LpMaximize)

x1 = pulp.LpVariable("Лимонад", lowBound=0,cat='Integer')  
x2 = pulp.LpVariable("Фруктовий_сік", lowBound=0,cat='Integer')  

model += x1 + x2
model += 2 * x1 + 1 * x2 <= 100
model += 1 * x1 <= 50
model += 1 * x1 <= 30
model += 2 * x2 <= 40
model.solve()

print("Результати:")
print(f"Кількість лимонаду: {x1.varValue}")
print(f"Кількість фруктового соку: {x2.varValue}")