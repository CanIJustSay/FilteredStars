import pandas as pd

df = pd.read_csv("completeCSV.csv")

radius = df["Radius"].tolist()
mass = df["Mass"].tolist()
gravity = df["Gravity"].tolist()
distance = df["Distance"].tolist()


nRadius = []
nMass = []
nGravity = []
nDistance = []

for i in range(0, len(radius)):
    d = float(distance[i])
    r = float(radius[i])
    m = float(mass[i])
    g = float(gravity[i])

    if d <= 100 and (g < 350 and g > 150):
        nRadius.append(r)
        nMass.append(m)
        nGravity.append(g)
        nDistance.append(d)

newDF = pd.DataFrame({
    "Radius":nRadius,
    "nMass":nMass,
    "Gravity":nGravity,
    "Distance":nDistance
})

newDF.to_csv("filter.csv")