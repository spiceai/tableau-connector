# Launches Tableau Desktop with the `spice` connector loaded from the source code.
run-tableau-with-connector:
	@echo "Running Tableau with connector..."
	@PLUGIN_PATH="$(CURDIR)/"; \
	TABLEAU_APP=$$(ls -d /Applications/Tableau\ Desktop\ *.app 2>/dev/null | sort -V | tail -n 1); \
	TABLEAU_APP="$$TABLEAU_APP/Contents/MacOS/Tableau"; \
	echo "Running: $$TABLEAU_APP -DConnectPluginsPath=$$PLUGIN_PATH"; \
	"$$TABLEAU_APP" -DConnectPluginsPath="$$PLUGIN_PATH" -DDisableVerifyConnectorPluginSignature=true

# Runs Tableau Desktop app with unsigned connector plugins enabled.
run-tableau-allow-unsigned:
	@echo "Running Tableau with signature verification disabled"
	@PLUGIN_PATH="$(CURDIR)/"; \
	TABLEAU_APP=$$(ls -d /Applications/Tableau\ Desktop\ *.app 2>/dev/null | sort -V | tail -n 1); \
	TABLEAU_APP="$$TABLEAU_APP/Contents/MacOS/Tableau"; \
	echo "Running: $$TABLEAU_APP -DConnectPluginsPath=$$PLUGIN_PATH"; \
	"$$TABLEAU_APP" -DDisableVerifyConnectorPluginSignature=true

# Runs TDVT tests with the Spice connector currently installed to Tableau.
.PHONY: test
test:
	make -C tdvt

# Deletes TACO files from the repository and Tableau's configuration.
clean:
	@find $(PACKAGE_DIR) -name 'spice*.taco' -exec rm -f {} +
	@rm -f ./spice.taco
	@rm -f ~/Documents/My\ Tableau\ Repository/Connectors/spice.taco
	@echo "Cleanup completed."


# Directory containing the connector packager
PACKAGE_DIR := connector-plugin-sdk/connector-packager

# Packages the connector into a TACO file and copies it to the root of the repository.
package:
	@echo "⚡ Packaging connector..."
	@cd $(PACKAGE_DIR) && \
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	python3 -m pip install --quiet --upgrade pip setuptools wheel && \
	pip install --quiet . && \
	echo "Running connector packager..." && \
	python3 -m connector_packager.package ../../spice_jdbc > /dev/null && \
	TACO_FILE=$$(find . -name 'spice*.taco' | head -n 1) && \
	echo "Packaged TACO file: $$TACO_FILE" && \
	cp "$$TACO_FILE" ../../spice.taco && \
	echo "📦 TACO package is ready: ./spice.taco"

# Creates a TACO file and copies it to the local Tableau repository.
.PHONY: package install
install: package
	@echo "⚡ Installing connector for development..."
	@TACO_FILE="./spice.taco"; \
	if [ ! -f "$$TACO_FILE" ]; then \
		echo "❌ File 'spice.taco' not found. Ensure 'make package' completed without errors."; \
		exit 1; \
	fi; \
	echo "Copying $$TACO_FILE to ~/Documents/My Tableau Repository/Connectors/"; \
	mkdir -p ~/Documents/My\ Tableau\ Repository/Connectors/ && \
	cp "$$TACO_FILE" ~/Documents/My\ Tableau\ Repository/Connectors/ && \
	echo "⚡ Connector installed";
