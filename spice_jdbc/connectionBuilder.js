(function dsbuilder(attr) {
    let server = attr[connectionHelper.attributeServer];
    let port = attr[connectionHelper.attributePort];

    if (attr["v-spice-product"] == "v-cloud") {
        server = "flight.spiceai.io";
        port = 443;
    }

    return [`jdbc:arrow-flight-sql://${server}:${port}`];
})
