import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	xml_validate = scriptdir + "\\bin\\xml-validate.exe"

	CREATE_NO_WINDOW=0x08000000

	args = [xml_validate, "-v"]

	p = subprocess.Popen(
		args,
		shell=True,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
                env={"XML_CATALOG_FILES": os.environ["XML_CATALOG_FILES"]},
		creationflags=CREATE_NO_WINDOW)
		
	(out, err) = p.communicate(Npp.editor.getText())
	e = p.wait()

	Npp.notepad.messageBox(err, "xml-validate")
	
main()
