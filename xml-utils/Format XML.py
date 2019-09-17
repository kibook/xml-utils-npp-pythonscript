import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.abspath(__file__))
	xml_format = scriptdir + "\\bin\\xml-format.exe"

	CREATE_NO_WINDOW=0x08000000

	args = [xml_format]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate(Npp.editor.getText())
	e = p.wait()

        if e == 0:
            Npp.editor.setText(out)
        else:
            Npp.notepad.messageBox(err, "xml-format error")
	
main()
