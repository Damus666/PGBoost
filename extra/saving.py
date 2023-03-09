from typing import Type, Any
from noinit import _NoInit

class Saving(_NoInit):
	"""Contains object-JSON conversion methods"""
 
 
	@staticmethod
	def ConvertObjectJSON(obj: Any, attributes_rules: dict[Type, list[str]]) -> dict:
		"""
		Convert an object in to a json-serializable dictionary, following the specified rules.

		You must specify the rules for every other type inside the main object.
		"""
		empty = {}
		if not type(obj) in attributes_rules.keys():
			raise ValueError("Missing rule for "+obj.__class__.__name__)
		for attr in attributes_rules[type(obj)]:
			value = getattr(obj, attr)
			if isinstance(value, (str, int, float, set, bool)) or value == None:
				empty[attr] = value
			elif isinstance(value, list):
				empty[attr] = Saving.ConvertListJSON(
					value, attributes_rules)
			elif isinstance(value, tuple):
				empty[attr] = Saving.ConvertTupleJSON(
					value, attributes_rules)
			elif isinstance(value, dict):
				empty[attr] = Saving.ConvertDictJSON(
					value, attributes_rules)
			else:
				empty[attr] = Saving.ConvertObjectJSON(
					value, attributes_rules)
		return empty

	@staticmethod
	def ConvertListJSON(obj: list[Any], attributes_rules: dict[Type, list[str]]) -> list:
		"""
		Replace every non-json-serializable object inside a list to a dictionary, following the specified rules.
		"""
		new = []
		for e in obj:
			if isinstance(e, (str, int, float, set, bool)) or e == None:
				new.append(e)
			elif isinstance(e, list):
				new.append(Saving.ConvertListJSON(e, attributes_rules))
			elif isinstance(e, tuple):
				new.append(Saving.ConvertTupleJSON(e, attributes_rules))
			elif isinstance(e, dict):
				new.append(Saving.ConvertDictJSON(e, attributes_rules))
			else:
				new.append(Saving.ConvertObjectJSON(e, attributes_rules))
		return new

	@staticmethod
	def ConvertTupleJSON(obj: tuple, attributes_rules: dict[Type, list[str]]) -> tuple:
		"""
		Replace every non-json-serializable object inside a tuple to a dictionary, following the specified rules.
		"""
		new = []
		for e in obj:
			if isinstance(e, (str, int, float, set, bool)) or e == None:
				new.append(e)
			elif isinstance(e, list):
				new.append(Saving.ConvertListJSON(e, attributes_rules))
			elif isinstance(e, tuple):
				new.append(Saving.ConvertTupleJSON(e, attributes_rules))
			elif isinstance(e, dict):
				new.append(Saving.ConvertDictJSON(e, attributes_rules))
			else:
				new.append(Saving.ConvertObjectJSON(e, attributes_rules))
		return tuple(new)

	@staticmethod
	def ConvertDictJSON(obj: dict[Any, Any], attributes_rules: dict[Type, list[str]]) -> dict:
		"""
		Replace every non-json-serializable object inside a dictionary to a dictionary, following the specified rules.
		"""
		new = {}
		for key in obj.keys():
			if not (isinstance(key, (str, int, float, set, list, tuple, dict, bool)) or key == None):
				raise ValueError(
					"A dictionary key cannot be json serialized if it's an object.")
			value = obj[key]
			if isinstance(value, (str, int, float, set)) or value == None:
				new[key] = value
			elif isinstance(value, list):
				new[key] = Saving.ConvertListJSON(value, attributes_rules)
			elif isinstance(value, tuple):
				new[key] = Saving.ConvertTupleJSON(value, attributes_rules)
			elif isinstance(value, dict):
				new[key] = Saving.ConvertDictJSON(value, attributes_rules)
			else:
				new[key] = Saving.ConvertObjectJSON(
					value, attributes_rules)
		return new
