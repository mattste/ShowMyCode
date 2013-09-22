import inspect
import importlib
import sys
import types
import runpy
import json

class FunctAction(object):

	def __init__(self, isBegin, modName, name, ret, *args, **kwargs):
		self.modName = modName
		self.isBegin = isBegin
		self.name = name
		self.args = args
		self.kwargs = kwargs
		if isBegin == True:
			print "starting function: " + name
			print "args: " + str(args) + " kwargs: " + str(kwargs)
		else:
			self.ret = ret
			print "finished function: " + name
			print "returned: " + str(ret)

class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		if not isinstance(obj, FunctAction):
			return super(MyEncoder, self).default(obj)

		return obj.__dict__


class RuntimeRecorder(object):

	actions = []

	class FunctionWrapper(object):
		def __init__(self, parent, callable):
			self.parent = parent
			self.callable = callable

		def __call__(self, *args, **kwargs):
			self.parent.calledFunction(self.callable.__name__, *args, **kwargs)
			ret = self.callable(*args, **kwargs)
			self.parent.functReturned(self.callable.__name__, ret, *args, **kwargs)
			return ret

	def setupRecording(self, modName):
		self.mod = importlib.import_module(modName)
		attributes = dir(self.mod)

		for attName in attributes:
			#ignore __name__ style methods
			if attName[0:2] == "__":
				continue

			attr = getattr(self.mod, attName)

			if hasattr(attr, "__call__"):
				# attribute is a method
				newMeth = self.FunctionWrapper(self, attr)
				setattr(self.mod, attName, newMeth)

	def start(self):
		self.mod.main()

	def calledFunction(self, name, *args, **kwargs):
		call = FunctAction(True, self.mod.__name__, name, None, *args, **kwargs)
		self.actions.append(call)

	def functReturned(self, name, ret, *args, **kwargs):
		ret = FunctAction(False, self.mod.__name__, name, ret, *args, **kwargs)
		self.actions.append(ret)

rr = RuntimeRecorder()
rr.setupRecording(sys.argv[1])
rr.start()

def getActions():
	temp = rr.actions
	#rr.actions[:] = []

	return temp