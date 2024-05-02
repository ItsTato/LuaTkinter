local getcwd = python:GetPackages({ "getcwd" }, "os");

print("Current working directory is: "..getcwd());
