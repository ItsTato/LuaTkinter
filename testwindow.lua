-- Create the MainWindow Element.
local MainWindow = new("Window");
-- new(object_name: String, parent: Element | None)
-- Window type elements cannot have a parent defined.

-- Name the Window.
MainWindow.Name = "MainWindow"
-- Leaving an element's name to its default value is
-- NOT recommended and can cause unforseen behavior.

-- Change the Window's title using the
-- Title property of the Window class.
MainWindow.Title = "Example Program";

--[[ Change window's geometry to a 100x100 box.
MainWindow.Width = 100;           By default: 400
MainWindow.Height = 100;          By default: 300
--]]

--[[ Alter max size of window to being 300x300.
MainWindow.MaxWidth = 300;        By default: nil
MainWindow.MaxHeight = 300;       By Default: nil
--]]

local HelloLabel = new("Label",MainWindow);

-- Starts the MainWindow loop.
-- No code can be ran after this is called,
-- assign anything you need before this.
MainWindow.run();
