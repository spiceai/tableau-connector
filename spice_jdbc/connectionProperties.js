(function propertiesbuilder(attr) {

    function isValueSet(value) {
        return value !== undefined && value !== null && value !== "";
    }

    // Supported params: https://arrow.apache.org/docs/java/flight_sql_jdbc_driver.html
    var props = {};

    const product = attr["v-spice-product"];
    const tlsMode = attr["sslmode"];

    function tlsRequired(product) {
        return (product === "v-cloud" || tlsMode === "require" || tlsMode === "required");
    }

    if (tlsRequired(product)) {
        props["useEncryption"] = "true";
    } else {
        props["useEncryption"] = "false";
    }

    // API key
    if (isValueSet(attr["password"])) {
        props["user"] = attr[""];
        props["password"] = attr["password"];
    }

    props["disableCertificateVerification"] = attr["v-disable-cert-verification"];

    return props;
})
