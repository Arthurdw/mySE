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

async function fetchData(request, data) {
    const reqValue = JSON.parse(request.responseText);
    if (request.status === 400) throw new BadRequest(reqValue["error"]);
    else if (reqValue.statusCode === 401) throw new UnauthorizedError(reqValue["error"]);
    console.log(reqValue[data]);
    return reqValue[data];
}

class BadRequest extends Error {
    constructor(message) {
        super(message);
        this.name = this.constructor.name;
        this.message = message;
    }
}

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

module.exports = {
    // Exporting Modules:
    gen_token: function(url, email) {
        const req = new XMLHttpRequest();
        req.open("POST", url + "token/add/", true);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify({email: email}));
        req.onload = function() { return fetchData(req, "token"); }
    },
    get_token: async function(url, _email) {
        const req = new XMLHttpRequest();
        req.open("POST", url + "token/", true);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify({'email': _email}));
        req.onload = async function () {
            return await fetchData(req, "token");
        }
    },
    // Exporting Errors:
    UnauthorizedError: UnauthorizedError,
    BadRequest: BadRequest
};
