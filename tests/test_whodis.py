import whodis
import pytest
import subprocess

def pytest_namespace():
    return {'whodis_proc': subprocess.Popen(['python', 'whodis/whodis.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)}

@pytest.fixture(autouse=True)
def procSetup():
    pytest.whodis_proc = subprocess.Popen(['python', 'whodis/whodis.py'], 
                                    stdout=subprocess.PIPE, stdin=subprocess.PIPE)

def test_ProgramExists():
    whodis_output = pytest.whodis_proc.communicate(input='1'.encode())[0]
    assert whodis_output != None