from src.SimTool import Model

model = Model.load('model.csv')
model.run(random_state=0)