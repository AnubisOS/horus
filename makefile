INSTALL_DIR = /usr/local/share
BIN_DIR = /usr/local/bin

all: horus

install:
	sudo rm -rf ${INSTALL_DIR}/horus
	sudo mkdir -p ${INSTALL_DIR}/horus
	mkdir ${HOME}/.config/horus
	cp ./res/papyri.cfg  ${HOME}/.config/horus/papyri.cfg
	sudo cp -rf ./src/* ${INSTALL_DIR}/horus/
	sudo chmod 777 ${INSTALL_DIR}/horus/__init__.py
	sudo ln -s ${INSTALL_DIR}/horus/__init__.py ${BIN_DIR}/horus
	@echo "Installed Horus successfully."

uninstall:
	rm -rf ${HOME}/.config/horus
	sudo rm -rf ${INSTALL_DIR}/horus
	sudo unlink ${BIN_DIR}/horus
	@echo "Uninstalled Horus successfully."


.PHONY: all install uninstall
.SILENT: install uninstall