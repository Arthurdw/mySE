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

export function gen_token(url, email) {
    const req = new XMLHttpRequest();
    req.open("POST", url + "token/", true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.send(JSON.stringify({
        email: email
    }));
    req.onload = function() {
        return JSON.parse(this.responseText)["token"];
    }
}

class Client {
    constructor(url, token) {
        this.url = url;
        this.token = token;
    }
}