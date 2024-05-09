local MainWindow = new("Window");
MainWindow.Name = "MainWindow";
MainWindow.Title = "Toolbarless App";
MainWindow.HasToolbar = false;

local LabelOne = new("Label",MainWindow);
LabelOne.Position = PxDim.new(10,10);
LabelOne.Text = "I'm Toolbarless!";

local CloseButton = new("Button",MainWindow);
CloseButton.Text = "Close App";

if OS == "Windows" then
	MainWindow.Size = PxDim.new(110,70);
	CloseButton.Position = PxDim.new(15,35);
else
	MainWindow.Size = PxDim.new(130,80);
	CloseButton.Position = PxDim.new(20,35);
end;
MainWindow.MinSize = MainWindow.Size;

CloseButton:Bind(
	"MouseButton1Click",
	function()
		MainWindow:Destroy();
	end
);

MainWindow.onClose = function() -- This prevents Alt+F4 as well! :3
	print("\nTo close this Window please use");
	print("the close button on the app instead!\n");
end;

MainWindow:Start();