-- Create the MainWindow Element.
local MainWindow = new("Window");
-- new(object_name: String, parent: Element | None)
-- Window type elements cannot have a parent defined.

-- Name the Window.
MainWindow.Name = "MainWindow";

-- Change the Window's title using the
-- Title property of the Window class.
MainWindow.Title = "Example Program";

---- Change window's geometry to a 100x100 box.
-- MainWindow.Size = PxDim.new(400,300);     Default is 400x300

---- Alter max size of window to being 300x300.
-- MainWindow.MaxSize = PxDim.new(300,300);  Default is no max.

local HelloLabel = new("Label",MainWindow);

HelloLabel.Text = "Woah! Amazing...";

HelloLabel.Position = PxDim.new(10,10);

-- Starts the MainWindow loop.
MainWindow.run();
-- No code can be ran after this is called,
-- assign anything you need before this.
