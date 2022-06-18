/*
This was a coding challenge shown to me by @fabiocberg on Instagram
The task was to see how many IP addresses are between 2 IPv4's.
This challenge made me think back to the cybersecurity stuff I learned with
IP's and back to when I was making computers in minecraft and had to learn binary
*/
function IPCalculate(ip1,ip2) {
    let ip1total = 0;
    let ip2total = 0;
    let ip1nums = ip1.split(".").map(x => parseInt(x, 10));
    let ip2nums = ip2.split(".").map(x => parseInt(x, 10));

    console.log(ip1nums,ip2nums);

    ip1total += ip1nums[0] * 256 ** 3;
    ip1total += ip1nums[1] * 256 ** 2;
    ip1total += ip1nums[2] * 256;
    ip1total += ip1nums[3];

    ip2total += ip2nums[0] * 256 ** 3;
    ip2total += ip2nums[1] * 256 ** 2;
    ip2total += ip2nums[2] * 256;
    ip2total += ip2nums[3];

    return (ip2total - ip1total);
}
console.log(IPCalculate("10.0.0.0", "10.1.0.0"));
console.log(IPCalculate("10.0.1.0", "10.0.12.0"));
console.log(IPCalculate("10.0.0.0", "10.0.1.0"));
console.log(IPCalculate("192.168.0.10", "192.168.1.0"));