local getcwd = Python:GetPackages({ "getcwd" }, "os");

print("Current working directory is: "..getcwd());
