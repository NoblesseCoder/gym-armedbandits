from gym.envs.registration import register

register(
    id='armedbandits-v0',
    entry_point='gym_armedbandits.envs:ArmedBanditsEnv',
)