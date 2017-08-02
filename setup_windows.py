from cx_Freeze import setup, Executable

base = None


executables = [Executable("run.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Creative Checker",
    options = options,
    version = "1.0.0",
    description = 'Moloco Creative Checker',
    executables = executables
)
