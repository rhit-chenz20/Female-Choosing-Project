import mesa

from .model import FemaleMatingModel
from .agent import Female


COP_COLOR = "#000000"
AGENT_QUIET_COLOR = "#0066CC"
AGENT_REBEL_COLOR = "#CC0000"
JAIL_COLOR = "#757575"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Filled": "true",
    }

    # if type(agent) is Citizen:
    #     color = (
    #         AGENT_QUIET_COLOR if agent.condition == "Quiescent" else AGENT_REBEL_COLOR
    #     )
    #     color = JAIL_COLOR if agent.jail_sentence else color
    #     portrayal["Color"] = color
    #     portrayal["r"] = 0.8
    #     portrayal["Layer"] = 0

    # elif type(agent) is Cop:
    #     portrayal["Color"] = COP_COLOR
    #     portrayal["r"] = 0.5
    #     portrayal["Layer"] = 1
    return portrayal


model_params = dict(
    femaleSize = 100,
    matingLength = 20,
    maleMu = 10,
    maleSigma = 10,
    maleSize = 1000,
    mutationMu = 10,
    generations = 10,
    startingRange = 3
)

# canvas_element = mesa.visualization.CanvasGrid(citizen_cop_portrayal, 40, 40, 480, 480)
server = mesa.visualization.ModularServer(
    FemaleMatingModel, [], "Epstein Civil Violence", model_params
)
server.port = 8521