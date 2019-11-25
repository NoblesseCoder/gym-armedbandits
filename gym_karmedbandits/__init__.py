from gym.envs.registration import register

register(
    id='KArmedBandits-v0',
    entry_point='gym_karmedbandits.envs:KArmedBanditsEnv',
)
