from cx_Freeze import setup, Executable


includefiles = ['in.txt', 'out.txt']

setup(
    name = "task_3",
    version = "1.0",
    description = "Dijkstra",
    options = {'build_exe': {'include_files':includefiles}},
    executables = [Executable("main.py")]
)