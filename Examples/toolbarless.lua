local MainWindow = new("Window");
MainWindow.Name = "MainWindow";
MainWindow.Title = "Toolbarless App";
MainWindow.Size = PxDim.new(110,70);
MainWindow.MinSize = MainWindow.Size;
MainWindow.HasToolbar = false;

local LabelOne = new("Label",MainWindow);
LabelOne.Position = PxDim.new(10,10);
LabelOne.Text = "I'm Toolbarless!";

local CloseButton = new("Button",MainWindow);
CloseButton.Text = "Close App";
CloseButton.Position = PxDim.new(15,35);

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
