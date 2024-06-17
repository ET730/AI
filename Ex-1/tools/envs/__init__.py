"""
OpenAI Gym environments designed for the AI lab course
"""

from gym.envs.registration import register
from envs.road_env import *

register(
    id='RoadEnv-v0',
    entry_point='envs:RoadEnv')