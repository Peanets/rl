import gym
env = gym.make('AirRaid-ram-v0')
env.reset()
agent = Agent(env.action_space)

for _ in range(3000):
    env.render()
    a = agent.act(obs)
    (ob, reward, done, _info) = env.step(a)