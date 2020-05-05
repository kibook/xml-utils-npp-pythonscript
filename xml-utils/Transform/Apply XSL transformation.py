import os
import subprocess
import Npp

def main():
	scriptdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	xml_transform = scriptdir + "\\bin\\xml-transform.exe"

	CREATE_NO_WINDOW=0x08000000

	buf = Npp.notepad.getCurrentBufferID()

	Npp.notepad.menuCommand(MENUCOMMAND.FILE_OPEN)
	
	# No XSLT script was selected
	if Npp.notepad.getCurrentBufferID() == buf:
		return
	
	path = Npp.notepad.getCurrentFilename()

	Npp.notepad.close()
	Npp.notepad.activateBufferID(buf)

	args = [xml_transform, "-s", path]

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
		Npp.notepad.messageBox(err)
	
main()
