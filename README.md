# gym-karmedbandits
A simple gym environment implementing the **Multiple Armed Bandits (MAB)** problem as described in chapter-2 in  [Reinforcement Learning: An Introduction, Richard S. Sutton & Andrew G. Barto](https://mitpress.mit.edu/books/reinforcement-learning-second-edition).

### Installation

```bash
git clone git@github.com:NoblesseCoder/gym-karmedbandits.git
cd gym-karmedbandits
pip install -e .
```

### Imports

```bash
import gym
import gym_karmedbandits
env = gym.make('KArmedBandits-v0') #useage
```

### References

[1] https://stackoverflow.com/questions/45068568/how-to-create-a-new-gym-environment-in-openai

[2] https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa

[3] Reinforcement Learning: An Introduction, Richard S. Sutton & Andrew G. Barto