# Spice Tableau Connector

Spice Tableau Connector is a JDBC-based connector that allows Tableau users to easily connect to and visualize data from Spice Cloud Platform and self-hosted Spice.ai OSS instances.

## Features

- Connect Tableau to Spice data sources: [Spice Cloud Platform](https://spice.ai/), self-hosted [Spice.ai OSS](https://spiceai.org/)
- API key authentication
- SSL encryption for secure connections
- Advanced SQL query [optimizations](https://tableau.github.io/connector-plugin-sdk/docs/capabilities) for enhanced performance, leveraging the [Apache Arrow Flight SQL JDBC Driver](https://arrow.apache.org/docs/java/flight_sql_jdbc_driver.html) to provide high-speed data access compared to standard JDBC connector.

## Installation

### Install Arrow Flight SQL JDBC Driver

#### macOS

```bash
curl -L https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/16.1.0/flight-sql-jdbc-driver-16.1.0.jar -o ~/Library/Tableau/Drivers/flight-sql-jdbc-driver-16.1.0.jar
```

#### Windows

```powershell
Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/16.1.0/flight-sql-jdbc-driver-16.1.0.jar" -OutFile "C:\Program Files\Tableau\Drivers\flight-sql-jdbc-driver-16.1.0.jar"
```

### Pre-built Connector

1. Download the latest `spice.taco` file from the [releases page](https://github.com/spiceai/tableau-connector/releases)
2. Copy to your Tableau connectors directory:
   - macOS: `~/Documents/My Tableau Repository/Connectors/`
   - Windows: `C:\Users\[USERNAME]\Documents\My Tableau Repository\Connectors\`

### Build from Source

```bash
# Clone the repository
git clone https://github.com/spiceai/tableau-connector.git
cd tableau-connector

# Package and install
make install
make run-tableau-allow-unsigned
```

## Development

### Prerequisites

- `make` command-line tool
- Python 3.x installed

### Run Connector

```bash
# Run Tableau with the connector loaded from source
make run-tableau-with-connector

# Clean build artifacts
make clean
```

### Run Tests

The connector uses [TDVT framework](https://tableau.github.io/connector-plugin-sdk/docs/tdvt).

```bash
# Package and install
make install

# Run Spice instance
cd tdvt && spice run 

# Run TDVT tests with the installed Spice connector
make test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
