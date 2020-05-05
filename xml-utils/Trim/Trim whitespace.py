import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	xml_trim = scriptdir + "\\bin\\xml-trim.exe"

	CREATE_NO_WINDOW=0x08000000

        elem = Npp.notepad.prompt("Element specifier (e.g., para to trim all <para> elements):", "xml-trim", "")

        if elem == None or elem == "":
            return

	args = [xml_trim, "-e", elem]

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
            Npp.notepad.messageBox(err, "xml-trim error")
	
main()
