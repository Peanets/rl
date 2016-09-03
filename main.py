import gym
from agent import Agent
env = gym.make('CartPole-v0')
obs = env.reset()
agent = Agent(env)

for _ in range(3000):
    env.render()
    a = agent.act(obs)
    (obs, reward, done, _info) = env.step(a)