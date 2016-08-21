import os
import st
import subprocess


@st.make_cache
def compile_qrc(filename):
    current_dir = os.path.dirname(__file__)

    rcc_path = os.path.join(current_dir, 'bin', 'pyside-rcc.exe')
    if not os.path.exists(rcc_path):
        rcc_path = 'pyside-rcc.exe'
        if not os.path.exists(rcc_path):
            raise EnvironmentError('pyside-rcc not found')
    command = rcc_path + ' -py3 ' + filename
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    p.wait()
    output = output.decode()
    return output


def load_qrc(filename):
    code = compile_qrc(filename)
    st.run(code)
