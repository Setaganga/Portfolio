/*
What IS a callback?
Its a function thats passed as an argument to another function
Make sure to pass as: function and not function(), we don't want to call the function, we only want to use the reference
*/

Output = (text) => {
    console.log(text);
}
sum = (x,y,callback) => {
    callback(x+y);
}
sum(2,3,Output);

/*
Async or Asynchronous functions are functions that run parallel with other functions
SetTimeout() is an example of an async function

I also learned of the bind function. It allows for arguments to be passed with a function reference.
*/
setTimeout(Output.bind(Output,"Hello, world!"),3000);
/*
setInterval is another method where you can have a callback function run for every interval
*/
let c = 0; //C...
Increment = () => {
    c++;
    console.log(c);
    //Oh my that's amazing. C++.
    //What's next, C# as well?
}
interval = (n) => {
    let intervalHello = setInterval(Increment,1000);
    setTimeout(clearInterval.bind(clearInterval,intervalHello),(n * 1000) + 1000);
}
const loopcount = 5;
setTimeout(interval.bind(interval,loopcount),5000);

/*
Okay well maybe I'm going a little overboard here, but it's fun to mess around with async.
*/