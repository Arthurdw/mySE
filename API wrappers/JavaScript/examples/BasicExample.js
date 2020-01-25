// // // // // // // // // // // // // // // // // // // // //
// API wrapper created for mySE by Arthurdw                 //
// mySE stands for My Secure Environment!                   //
// mySE was created for GO-Atheneum Oudenaarde              //
// This project and all it files are under a MIT licence.   //
// Project (mySE) started on 09/01/2020!                    //
// // // // // // // // // // // // // // // // // // // // //

// // // // // // // // // // // // // // // // // // // // //
// A basic example file to showcase the mySE.js wrapper.    //
// // // // // // // // // // // // // // // // // // // // //

import * as mySE from '../mySE/meSE.js';

const local_url = "http://127.0.0.1:5000/", mail = "mail@mail.mail";

const token = mySE.gen_token(local_url, mail);
console.log(token);