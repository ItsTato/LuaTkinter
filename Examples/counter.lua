local MainWindow = Element.new("Window");
MainWindow.Name = "MainWindow";
MainWindow.Title = "Counter App";
MainWindow.WidthResizable = false;
MainWindow.HeightResizable = false;

if System:isWindows() then
	MainWindow.Size = PxDim.new(240,80);
else
	MainWindow.Size = PxDim.new(260,80);
end;

local CountLabel = Element.new("Label",MainWindow);
CountLabel.Position = PxDim.new(10,10);

local Add1Button = Element.new("Button",MainWindow);
Add1Button.Text = "Add 1 to count!";
Add1Button.Position = PxDim.new(10,35);

local Add100Button = Element.new("Button",MainWindow);
Add100Button.Text = "Add 100 to count!";
Add100Button.Position = PxDim.new(120,35);

local count = 0;
CountLabel.Text = "Count is "..count;

Add1Button:Bind(
	"MouseButton1Click",
	function()
		count = count + 1;
		CountLabel.Text = "Count is "..count;
	end
);

Add100Button:Bind(
	"MouseButton1Click",
	function()
		count = count + 100;
		CountLabel.Text = "Count is "..count;
	end
);

MainWindow:Start();
