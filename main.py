import subprocess as sbp
import pip

pkgs = eval(str(sbp.run("pip list -o --format=json", shell=True,
                        stdout=sbp.PIPE).stdout, encoding='utf-8'))

for pkg in pkgs:
    sbp.run("pip install --upgrade " + pkg['name'], shell=True)
