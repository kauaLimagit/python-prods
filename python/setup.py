from cx_Freeze import setup, Executable

setup(
    name='autopy',
    version='1.0',
    description='abrir ferramentas de alunos automaticamente',
    executables=[Executable('pyauto.py')]
)