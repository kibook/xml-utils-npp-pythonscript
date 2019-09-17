.PHONY: all clean

README=../../README.md

S1KD2DB_PARAMS+=-stringparam dmodule.is d:section
S1KD2DB_PARAMS+=-param include.emphasis.role 1

all: $(README)

$(README): DMC-XMLNPP-A-00-00-00-00A-040A-D_EN-CA.XML Makefile
	s1kd2db $< $(S1KD2DB_PARAMS) | pandoc -f docbook -t markdown_github -o $@

clean:
	rm -f $(README)
