// Strings and template literals
// A template literal is a string that uses backticks instead of quotes and can embed variables directly using ${variable}.
// This is JavaScript's equivalent of Python's f-strings.

const name = "Hassan";
const sleep = 7.5;
const steps = 12340;
const goal = 10000;

// Template literal: backticks + ${}
const report = `Athlete: ${name}
Sleep: ${sleep} hours
Steps: ${steps.toLocaleString()}
Goal: ${goal.toLocaleString()}
Result: ${steps >= goal ? "HIT" : "MISS"}`;

console.log(report)

// String methods
const city = "  nairobi ";
console.log("\nRaw city:", `"${city}"`);
console.log("Trimmed:", `"${city.trim()}"`);
console.log("length:", city.trim().length);

// String included and startsith
const skill = "phone repair";
console.log("\nIncludes 'repair':", skill.includes("repair"));
console.log("Stats with 'phone':", skill.startsWith("phone"));
console.log("replace:", skill.replace("phone", "laptop"));
