# LuaTkinter
A simple Python program that allows you to easily write UI-based Applications in Lua.

**Note:** Everything is subject to change. Nothing is finalized yet.

# WARNING!
Howdy, person! LuaTkinter is still unfinished and if you are reading this it may still be missing key features.

Currently, it still lacks the simplest things, such as Frames. Be warned! The GitHub repo is only public for simplicity and to keep history!

# Important

## [LINUX] Have Tkinter installed!
If you are using Linux and have a system-provided Python install, make sure you have Tkinter installed!

```commandline
sudo apt install python3-tk
```

## Have Python installed!
Version 3.10 or above is recommended.

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

**Note:** In the future, packages such as `requests` may be implemented in the Lua environment as custom globals. These pre-included packages would also be installed with this command (in theory).

# What is LuaTkinter?
LuaTkinter is designed to be a simplistic, easy-to-learn, powerful, and functional framework for building desktop applications in Lua.

Of course, since LuaTkinter is made on top of other technologies (`LuaTk@Lua` -> `LuaTkinter@Python` -> `tkinter@Python` -> `Tcl/Tk`), performance cannot be guaranteed, however, performance-impact is highly minimal when compared to other frameworks for creating apps, such as Electron.

# Using LuaTkinter
Using LuaTkinter is as simple as creating  a `.lua` file. No, really!

Well... Actually, there's one more step:
- You have to run this file using the LuaTkinter module!

How? Simple! Like so:
#### Linux
```commandline
python3 -m LuaTkinter my_window.lua
```
#### Windows
```commandline
py -3 -m LuaTkinter my_window.lua
```

**File \~** `my_window.lua`
```lua
local MainWindow = Element.new("Window");
-- Element.new(object_name: String, parent: Element | nil)
-- Window type elements cannot have a parent defined.

MainWindow.Name = "MainWindow";
-- Name the element.

MainWindow.Title = "Example Program";
-- Change the Window's title using the Title property of the Window class.

MainWindow:Start();
-- Starts the MainWindow loop.
-- No code can be run after this is called, assign anything you need before this!
```

This example program creates a new Window with the title "*Example Program*". You can take this as a template and expand further on it using the LuaTkinter documentation (**CURRENTLY NOT AVAILABLE**) or you can also [check out some examples](https://github.com/ItsTato/LuaTkinter/tree/edge/Examples) made for your convenience.
