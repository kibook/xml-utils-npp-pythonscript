xml-utils PythonScript interface for Notepad++ - README
=======================================================

General
-------

These are a set of scripts for the
[PythonScript](http://npppythonscript.sourceforge.net) plugin which
provide an interface for using the
[xml-utils](https://github.com/kibook/xml-utils) within
[Notepad++](https://notepad-plus-plus.org).

Install
-------

Copy the `xml-utils` directory to the PythonScript user scripts folder,
typically `%APPDATA%\Notepad++\plugins\config\PythonScript\scripts`.

Functions
---------

-   **Format**

    -   **Format XML**

        Pretty-print the XML in the current buffer.

-   **Transform**

    -   **Apply XSL transformation (preserve DTD)**

        Apply an XSL transform script to the document, preserving the
        original DTD.

    -   **Apply XSL transformation**

        Apply an XSL transform script to the document.

-   **Trim**

    -   **Trim whitespace**

        Trim whitespace within specified elements.

-   **Validate**

    -   **Check against schema**

        Validate the document against its schema.
