from pulp import *

machines = ["M0", "M1", "M2", "M3"]
jobs = ["J0", "J1", "J2", "J3"]
I = range(len(machines))
J = range(len(jobs))
Set_up_time = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
]

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Assignment Model", LpMinimize)

# Define decision variables
X = LpVariable.dicts('X', ((i, j) for i in I for j in J), cat='Binary')

# Define objective function
prob += lpSum(Set_up_time[i][j] * X[i, j] for i in I for j in J)

# Constraint-1
for i in I:
    prob += lpSum(X[i, j] for j in J) <= 1

# Constraint-2
for j in J:
    prob += lpSum(X[i, j] for i in I) >= 1

# Solve the problem
prob.solve()

# Print the optimized set up time
print("Optimized Set up Time:", value(prob.objective), "hours")

# Print the assignment of jobs to machines
for i in I:
    print("-" * 30)
    print("Machine:", machines[i])
    print("-" * 30)
    for j in J:
        print("Jobs", jobs[j], value(X[i, j]))
