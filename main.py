import gym
from agent import Agent
import sys


def run(render):
    env = gym.make('CartPole-v0')
    obs = env.reset()
    agent = Agent(env)

    for _ in range(3000):
        if render:
            env.render()
        a = agent.act(obs)
        (obs, reward, done, _info) = env.step(a)
        agent.learn(obs, reward)

if __name__=="__main__":
    run("render" in sys.argv)