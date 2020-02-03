// // // // // // // // // // // // // // // // // // // // //
// API wrapper created for mySE by Arthurdw                 //
// mySE stands for My Secure Environment!                   //
// mySE was created for GO-Atheneum Oudenaarde              //
// This project and all it files are under a MIT licence.   //
// Project (mySE) started on 09/01/2020!                    //
// // // // // // // // // // // // // // // // // // // // //


// // // // // // // // // // // // // // // // // // // // //
// Main API wrapper file.                                   //
// This will include the client object and the methods to-  //
// - generate or fetch a token.                             //
// // // // // // // // // // // // // // // // // // // // //

// const errors = require("./error");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

module.exports = {
    gen_token: function(url, email) {
        const req = new XMLHttpRequest();
        req.open("POST", url + "token/", true);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify({email: email}));
    },
    get_token: function(url, email) {
        const req = new XMLHttpRequest();
        req.open("GET", url + "token/", true);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify({email: email}));
        req.onload = function() {
            const reqValue = JSON.parse(req.responseText);
            console.log(reqValue);
            console.log(reqValue.message);
            if (reqValue["statusCode"] === 401) throw new UnauthorizedError(reqValue["error"]);
            return reqValue["token"];
        }
    }
};

class UnauthorizedError extends Error {
    constructor(message) {
        super(message);
        this.name = this.constructor.name;
        this.message = message;
    }
}

class Client {
    constructor(url, token) {
        this.url = url;
        this.token = token;
    }
}
