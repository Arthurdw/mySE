// // // // // // // // // // // // // // // // // // // // //
// API wrapper created for mySE by Arthurdw                 //
// mySE stands for My Secure Environment!                   //
// mySE was created for GO-Atheneum Oudenaarde              //
// This project and all it files are under a MIT licence.   //
// Project (mySE) started on 09/01/2020!                    //
// // // // // // // // // // // // // // // // // // // // //

// // // // // // // // // // // // // // // // // // // // //
// This file will contain all mySE errors.                  //
// // // // // // // // // // // // // // // // // // // // //

module.exports = UnauthorizedError;

class UnauthorizedError extends Error {
    constructor(message) {
        super(message);
        this.name = this.constructor.name;
    }
}
 