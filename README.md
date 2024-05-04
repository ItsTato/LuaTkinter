# LuaTkinter
A simple Python program that allows you to easily write UI-based Applications in Lua.

# WARNING!
**HOWDY**, Person of the past! LuaTkinter is still unfinished if you are reading this and may be missing key features.

(AS OF NOW) it still lacks the simpliest things, such as Labels and Frmaes. Be warned! It is only public for simplicity and to keep history!

# Important

## [LINUX] Have Tkinter installed!
If you are using Linux and have a system-provided Python install, make sure you have Tkinter installed!

```commandline
sudo apt intall python3-tk
```

## Meet the requirements!
Make sure you have any and all packages in `requirements.txt` installed!

#### Linux Command
```commandline
python3 -m pip install -r requirements.txt
```
#### Windows Command
```commandline
py -3 -m pip install -r requirements.txt
```

**Note:** In the future, packages such as `requests` may be implemented in the Lua environment as custom globals. These pre-included packages would also be installed with this command in theory.

**Note:** Everything is subject to change. Nothing is finalized yet.

# What is LuaTkinter?
LuaTkinter is designed to be simplistic, easy-to-learn, powerful and functional.

Of course, since LuaTkinter is made on-top of other technologies (`LuaTk@Lua` -> `LuaTkinter@Python` -> `tkinter@Python` -> `Tcl/Tk`), performance cannot be guaranteed, however, performance-impact is highly minimal when compared to other frameworks for creating apps, such as Electron.

# Using LuaTkinter
Using LuaTkinter is as simple as creating  a `.lua` file. No, really!

Well, actually there's one more step:
- You have to run this file using the LuaTkinter module!

How? Simple! Like so:
#### Linux
```commandline
python3 -m LuaTkinter my_window.lua
```
#### Windows
```commandline
py -3.10 -m LuaTkinter my_window.lua
```

**File ~** `my_window.lua`
```lua
local MainWindow = new("Window");
-- new(object_name: String, parent: Element | nil)
-- Window type elements cannot have a parent defined.

MainWindow.Name = "MainWindow"
-- Leaving an element's name to its default value can cause unforseen behavior.

MainWindow.Title = "Example Program";
-- Change the Window's title using the Title property of the Window class.

MainWindow:Start();
-- Starts the MainWindow loop.
-- No code can be ran after this is called, assign anything you need before this.
```

This example program creates a new Window with the title "*Example Program*". You can take this as a template and expand further on it using the LuaTkinter documentation (**CURRENTLY NOT AVAILABLE**) or you can [check out some examples](https://github.com/ItsTato/LuaTkinter/tree/edge/Examples)!
