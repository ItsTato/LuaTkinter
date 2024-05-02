from lupa import LuaRuntime
from typing import Any
from os import getcwd, path

from . import LuaTk
from .LuaTk import Color, Element

def Run(file_name:str) -> None:
	luaRuntime:LuaRuntime = LuaRuntime(unpack_returned_tuples=True)

	def __import_or_import_from(_,parts_pname:str|dict,p_name:str=None) -> Any: # type: ignore
		if p_name is None:
			if isinstance(parts_pname,str):
				return __import__(parts_pname)
			if len(parts_pname) > 1:
				table:dict = {}
				for i in parts_pname:
					table[parts_pname[i]] = __import__(parts_pname[i])
				return table
		if not isinstance(parts_pname,str) and len(parts_pname) > 1:
			table:dict = {}
			for i in parts_pname:
				table[parts_pname[i]] = getattr(__import__(p_name),parts_pname[i])
			return table
		if not isinstance(parts_pname,str):
			return getattr(__import__(p_name),parts_pname[1])
		return getattr(__import__(p_name),parts_pname)
	
	def __new(name:str,parent:Element|None=None) -> Element:
		try:
			Object = getattr(LuaTk,name)
		except AttributeError:
			print(f"No class called \"{name}\" was found.")
			exit(1)
		return Object(parent)

	__python:dict = {
		"GetModule": __import_or_import_from,
		"GetPackage": __import_or_import_from,
		"GetModules": __import_or_import_from,
		"GetPackages": __import_or_import_from
	}

	luaRuntime.globals().python = __python

	luaRuntime.globals().new = __new

	luaRuntime.globals().Color = Color


	theoretical_location:str = path.join(getcwd(),file_name)
	if path.exists(theoretical_location):
		with open(theoretical_location,"r") as file:
			contents:str = file.read()
	else:
		print(f"BOI r u HIGH dat {theoretical_location} file u speak of dont exist\nsmh")
		exit(1)
	
	luaRuntime.execute(contents)

	return
