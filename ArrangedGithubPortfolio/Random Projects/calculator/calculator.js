//functype to check which function to do
//check if its in radians, default is in degrees
var functype = '';
var radflag = false;

//Set functype
function setfunc(text) {
    functype = text;
    document.getElementById('func').innerHTML = text;
}
//Auto process pi and e
function pe(num) {
    if (num != 1) {
        document.getElementById('ans').innerHTML = Math.PI;
    }
    else {
        document.getElementById('ans').innerHTML = Math.E;
    }
}
//Separate function that is called by main if its a trig function
function trig() {
    var in1 = document.getElementById("input1").value;
    var answer;
    //If its in radians, let it run, but if in degrees, convert degrees to radians
    if (radflag == true) {
        in1 = parseFloat(in1);
    }
    else {
        in1 = (parseFloat(in1) * Math.PI) / 180;
    }
    switch (functype) {
        case 'SIN':
            answer = Math.sin(in1);
            break;
        case 'COS':
            answer = Math.cos(in1);
            break;
        case 'TAN':
            answer = Math.tan(in1);
            break;
        case 'SIN-1':
            if (in1 > 1 || in1 < -1) {
                window.alert("Must be between -1 and 1 Radians");
            }
            answer = Math.asin(in1);
            break;
        case 'COS-1':
            if (in1 > 1 || in1 < -1) {
                window.alert("Must be between -1 and 1 Radians");
            }
            answer = Math.acos(in1);
            break;
        case 'TAN-1':
            answer = Math.atan(in1);
            break;
        default:
            answer = "Something went wrong...Trig";
            break;
    }
    //Set answer
    if (isNaN(answer)) {
        document.getElementById('ans').innerHTML = "ERROR";
    }
    else {
        document.getElementById('ans').innerHTML = answer;
    }
}
//Main process function (called by html button)
function main() {
    //If a trig function, send it to trig.
    if (functype == 'SIN' || functype == 'COS' || functype == 'TAN' || functype == 'SIN-1' || functype == 'COS-1' || functype == 'TAN-1') {
        trig();
    }
    else {
    var in1 = document.getElementById("input1").value;
    var in2 = document.getElementById("input2").value;
    var answer;
    in1 = parseFloat(in1);
    in2 = parseFloat(in2);
    switch (functype) {
        case '+':
            answer = in1 + in2;
            break;
        case '-':
            answer = in1 - in2;
            break;
        case '*':
            answer = in1 * in2;
            break;
        case '/':
            if (in2 == 0) {
                answer = "Division by 0 Error";
            }
            else {
                answer = in1 / in2;
            }
            break;
        case 'sqrt':
            answer = Math.sqrt(in1);
            break;
        case 'cbrt':
            answer = Math.cbrt(in1);
            break;
        case '^':
            answer = Math.pow(in1,in2);
            break;
        case '10^x':
            answer = Math.pow(10,in1);
            break;
        case 'ROUND':
            answer = Math.round(in1);
            break;
        case 'LOG':
            answer = Math.log(in1);
            break;
        case 'LOG2':
            answer = Math.log2(in1);
            break;
        case 'LOG10':
            answer = Math.log10(in1);
            break;
        default:
            answer = "Something went wrong...Main";
            break;
    }
    //Set answer
    if (isNaN(answer)) {
        document.getElementById('ans').innerHTML = "ERROR";
    }
    else {
        document.getElementById('ans').innerHTML = answer;
    }
}
}
//Toggle DEG <-> RAD
function toggledegrad() {
    radflag = !radflag
    if (radflag == true) {
        document.getElementById('flag').innerHTML = "Rad";
    }
    else {
        document.getElementById('flag').innerHTML = "Deg";
    }
}