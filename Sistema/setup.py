from cx_Freeze import setup, Executable

setup(
    name="Herramienta-PDF",
    version="0.1",
    description="APP PDF",
    executables=[Executable("main.py")]
)