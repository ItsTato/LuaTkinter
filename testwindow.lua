-- Create the MainWindow Element.
local MainWindow = new("Window");
-- new(object_name: String, parent: Element | None)
-- Window type elements cannot have a parent defined.

-- Name the Window.
MainWindow.Name = "MainWindow";

-- Change the Window's title using the
-- Title property of the Window class.
MainWindow.Title = "Example Program in "..system.os;

---- Change window's geometry to a 100x100 box.
-- MainWindow.Size = PxDim.new(400,300);     Default is 400x300

---- Alter max size of window to being 300x300.
-- MainWindow.MaxSize = PxDim.new(300,300);  Default is no max.

local HelloLabel = new("Label",MainWindow);

HelloLabel.Text = "theres a frame in here probably";

HelloLabel.Position = PxDim.new(10,10);

local testFrame = new("Frame",MainWindow);
testFrame.Position = PxDim.new(20,20);

MainWindow.onClose = function()
    print("Bye :C");

    -- If MainWindow is not destroyed it will not actually
    -- close your application! Beware!
    MainWindow:Destroy();
end;

-- Starts the MainWindow loop.
MainWindow:Start();
-- No code can be ran after this is called,
-- assign anything you need before this.
