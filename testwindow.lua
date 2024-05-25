-- Create the MainWindow Element.
local MainWindow = Element.new("Window");
-- Element.new(object_name: String, parent: Element | None)
-- Window type elements cannot have a parent defined.

-- Name the Window.
MainWindow.Name = "MainWindow";

-- Change the Window's title using the
-- Title property of the Window class.
MainWindow.Title = "Example Program in "..System.OS;

---- Change window's geometry to a 100x100 box.
-- MainWindow.Size = PxDim.new(400,300);     Default is 400x300

---- Alter max size of window to being 300x300.
-- MainWindow.MaxSize = PxDim.new(300,300);  Default is no max.

local testFrame = Element.new("Frame",MainWindow);
testFrame.Position = PxDim.new(20,20);

local testLabel = Element.new("Label",testFrame);
testLabel.Position = PxDim.new(10,10);
testLabel.Text = "im in a frame!\npos is: "..testLabel.Position;

MainWindow.onClose = function()
    print("Bye :C");

    -- If MainWindow is not destroyed it will not actually
    -- close your application. Beware!
    MainWindow:Destroy();
end;

-- Starts the MainWindow loop.
MainWindow:Start();
-- No code can be ran after this is called,
-- assign anything you need before this.
