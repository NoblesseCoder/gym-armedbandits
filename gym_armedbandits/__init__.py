from gym.envs.registration import register

register(
    id='ArmedBandits-v0',
    entry_point='gym_armedbandits.envs:ArmedBanditsEnv',
)
