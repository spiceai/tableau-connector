(function propertiesbuilder(attr) {

    function isValueSet(value) {
        return value !== undefined && value !== null && value !== "";
    }

    // Supported params: https://arrow.apache.org/docs/java/flight_sql_jdbc_driver.html
    var props = {};

    const product = attr["v-spice-product"];
    const isUseSSL = attr["sslmode"];

    function sslRequired(product) {
        return (product === "v-cloud" || isUseSSL === "require" || isUseSSL === "required");
    }

    if (sslRequired(product)) {
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
