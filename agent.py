import numpy as np

class Agent(object):

	def __init__(self, env):
		self.env = env

	def act(self, observation):
		return self.env.action_space.sample()

	def learn(self, observation, reward):
		pass
		