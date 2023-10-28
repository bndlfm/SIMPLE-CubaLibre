import gym
from gym.envs.registration import register

register(
    id='Cuba_Libre-v0',
    entry_point='classes.envs:CubaLibreEnv',
)

