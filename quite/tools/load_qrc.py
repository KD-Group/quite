import os
import st
import subprocess
import PySide

pyside_path = os.path.dirname(PySide.__file__)
rcc_path = os.path.join(pyside_path, 'pyside-rcc.exe')
if not os.path.exists(rcc_path):
    rcc_path = 'pyside-rcc.exe'
if not os.path.exists(rcc_path):
    print('PySide Resource Compiler (pyside-rcc.exe) Not Found!')


@st.make_cache
def compile_qrc(filename):
    command = rcc_path + ' -py3 ' + filename
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    p.wait()
    output = output.decode()
    return output


def load_qrc(filename):
    code = compile_qrc(filename)
    st.run(code)
