from JackOfHeartsModel import JackOfHeartsModel

def agent_portyal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r":1}
    if agent.isJackOfHeart == True:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "lightgrey"
        portrayal["Layer"] = 2
    return portrayal



grid = CanvasGrid(
    agent_portrayal,
    30,
    30,
    800,
    800)

chart = ChartModule(
    [
        {'Label': 'Gini','Color': 'Black'}
    ],
    data_collector_name='datacollector')

server = ModularServer(
    JackOfHeartsModel,
    [grid, chart],
    "Jack Of Hearts Model",
    {"N":20, "width":30,"height":30}
    )
server.port = 8521 # Any non-80 port to appease replit
server.launch()
