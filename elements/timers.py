import pygame
from ..noinit import _NoInit
"""
Contains the timers classes.
"""

class TimerManager(_NoInit):
    """Simple class that contains the timers and automatically updates them in the main loop"""
    timers = dict()
    
    @classmethod
    def Add(cls,name,timer,activate_on_end):
        cls.timers[name] =(timer,activate_on_end)
        
    @classmethod
    def Get(cls,name):
        return cls.timers[name][0]
    
    @classmethod
    def _update(cls):
        for t in cls.timers.values():
            t[0].Update(t[1])

# TIMERS
class CooldownTimer():
	"""
	A timer, based on a cooldown. Not recommended.
	"""
	def __init__(self,cooldown:int,step=1):

		self.cooldown = cooldown
		self.timer = cooldown
		self.finished = False
		self.step = step

	def Update(self,dt:float=1.0)->None:
		"""
		Update the timer.
		"""
		# decrease timer value
		self.timer -= self.step*dt
		if self.timer <= 0:
		# set the status finished to true
			self.finished = True
			self.timer = 0

	def Reset(self)->None:
		"""
		Reset the timer.
		"""
		# reset the variables
		self.timer = self.cooldown
		self.finished = False

class Timer:
	"""
	A timer based on game ticks.
	"""
	def __init__(self,duration:int,func = None,start_active=False):
		self.duration = duration 
		self.func = func
		self.start_time = 0
		self.active = False
		if start_active:
			self.Activate()

	def Activate(self)->None:
		"""
		Activate the timer.
		"""
		self.active = True
		self.start_time = pygame.time.get_ticks()

	def Deactivate(self)->None:
		"""
		Deactivate the timer.
		"""
		self.active = False
		self.start_time = 0

	def Update(self,activate_on_end=False)->None:
		"""
		Update the timer.
		"""
		current_time = pygame.time.get_ticks()
		if current_time - self.start_time> self.duration:
			if self.func and self.start_time != 0:
				self.func()
			self.Deactivate()
			if activate_on_end:
				self.Activate()

