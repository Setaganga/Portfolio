/*
Now we're gonna get into PROMISES.

Promises are code links Producing Code and Consuming Code

Producing code is code that takes time
Consuming code is code that has to wait for the result
*/
Output = (text) => {
    console.log(text);
    return true;
}

let promise = new Promise(function(resolve, reject) {
    outputStatus = Output("Hello there!");
    if (outputStatus == true) {
        resolve("Printed Successfully");
    }
    reject("Could not print successfully");
});

promise.then(
    function(value) {console.log(value);},
    function(error) {console.log(error);}
);

/*
To me this seems kinda redundant because we have try catch and stuff.
But I probably just don't know the differences
I have learned.
Async: Promises
Sync code: Try Catches
*/