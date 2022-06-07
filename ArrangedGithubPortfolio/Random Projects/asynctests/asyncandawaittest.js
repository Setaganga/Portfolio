/*
Here is where we get into the Async and Await stuff

Async - Makes function return a Promise
Await - Makes function wait for a Promise
*/
Output = (text) => {
    console.log(text);
    return true;
}

//Async doesnt work for arrow funcs. Sad days.
async function helloFunc() {
    let prom = new Promise(function(resolve) {
        resolve("Hello there");
    });
    Output(await prom);
}
helloFunc();