from sys import argv

from .LT import Run

def main() -> None:
	Run(argv[len(argv)-1])
	return
