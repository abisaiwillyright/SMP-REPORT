// JavaScript Fundamentals - JavaScript is a programming language that runs inside a web browser.

// Variables: let and const 
// const declares a variable that will not be reassigned.
// let declares a variable that may be reassigned later
// Use const by default. Switch to let only when you know the value will change.

const athleteName = "Abisai";
const protocol = "SMP Phase 1";
const targetSteps = 10000;

// let for values that change
let dayNumber = 1;
let sepCount = 0;


console.log("Althlate:", athleteName);
console.log("protocol:", protocol);
console.log("Target steps:", targetSteps);

// Reasign let variable
dayNumber = 7;
let stepCount = 11240;

console.log("\nDay:", dayNumber);
console.log("Steps logged:", stepCount);
console.log("Hit goal:", stepCount >= targetSteps);

// typeof checks the data type
console.log("\nTypes:");
console.log("athleteName:", typeof athleteName);  // string
console.log("targetSteps:", typeof targetSteps);  // number
console.log("hit goal:", typeof true);    //boolean
