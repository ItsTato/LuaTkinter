from lupa import LuaRuntime
from typing import Any, Callable
from os import getcwd, path
from platform import system

from . import LuaTk

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
	
	def __new(name:str,parent:LuaTk.Element|None=None) -> LuaTk.Element:
		try:
			Object = getattr(LuaTk,name)
		except AttributeError:
			print(f"No class called \"{name}\" was found.")
			exit(1)
		return Object(parent)

	__python:dict[str,Callable] = {
		"GetModule": __import_or_import_from,
		"GetPackage": __import_or_import_from,
		"GetModules": __import_or_import_from,
		"GetPackages": __import_or_import_from
	}

	def __is(_,name:str) -> bool: return system().lower() == name.lower()
	def __isWindows(_) -> bool: return system() in ["dos","win","nt"]
	def __isLinux(_) -> bool: return system() in ["Linux"]

	__system:dict[str,Callable|str] = {
		"os": system(),
		"is": __is,
		"isWindows": __isWindows,
		"isLinux": __isLinux
	}

	__element:dict[str,Callable] = {
		"new": __new
	}

	luaRuntime.globals().system = __system

	luaRuntime.globals().Element = __element
	luaRuntime.globals().python = __python

	luaRuntime.globals().Color = LuaTk.Color
	luaRuntime.globals().PxDim = LuaTk.PxDim

	theoretical_location:str = path.join(getcwd(),file_name)
	if path.exists(theoretical_location):
		with open(theoretical_location,"r") as file:
			contents:str = file.read()
	else:
		print(f"BOI r u HIGH dat {theoretical_location} file u speak of dont exist\nsmh")
		exit(1)
	
	luaRuntime.execute(contents)

	return
