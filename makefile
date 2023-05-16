INSTALL_DIR = /usr/local/share
BIN_DIR = /usr/local/bin

all: horus

install:
	rm -rf ${INSTALL_DIR}/horus
	mkdir -p ${INSTALL_DIR}/horus
	cp -rf ./src/* ${INSTALL_DIR}/horus/
	chmod 777 ${INSTALL_DIR}/horus/__init__.py
	ln -s ${INSTALL_DIR}/horus/__init__.py ${BIN_DIR}/horus

uninstall:
	rm -rf ${INSTALL_DIR}/horus
	unlink ${BIN_DIR}/horus


.PHONY: all install uninstall