import numpy as np
import os
from commonroad.common.file_reader import CommonRoadFileReader
from commonroad.common.file_writer import CommonRoadFileWriter
from commonroad.geometry.shape import Rectangle
from commonroad.scenario.trajectory import InitialState
from commonroad.scenario.obstacle import ObstacleType, StaticObstacle, DynamicObstacle

from planner import Planner

# Load scenario
scenario, _ = CommonRoadFileReader(
    'scenario_building/DEU_Ffb-1_4_recreation.xml').open()

vehicle = scenario.obstacle_by_id(249624)
scenario.remove_obstacle(vehicle)

init_state = InitialState(position=np.array([76.6, 3.0]),
                   orientation=0.22,
                   velocity=10,
                   time_step=0)

planner = Planner(init_state,
                  goal_point=[190, -8],
                  reference_speed=10,
                  time_horizon=100)
trajectory_pred = planner.plan(scenario)

vehicle.initial_state = init_state
vehicle.prediction = trajectory_pred
scenario.add_objects(vehicle)


# Save scenario
scenario_folder = 'scenario_building'
if not os.path.isdir(scenario_folder):
    os.mkdir(scenario_folder)
CommonRoadFileWriter(scenario, set()).write_scenario_to_file(
    filename=os.path.join(scenario_folder, 'DEU_Ffb-1_4_hidden.xml'))
