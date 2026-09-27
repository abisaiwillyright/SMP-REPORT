// Week 8 Gate: JavaScript and Web

// Code Challenge 1 — Greet User
// Write a JavaScript function called 
// (greetUser) that takes a (name) parameter and returns the string: (Welcome), [name]! (Ready to build?)
// Call it twice and log the results.


const greetUser = (name) => {
  return `Welcome, ${name}! Ready to build?`;
};

console.log(greetUser("Amerix"));
console.log(greetUser("SMP Member"));
console.log()





// Code Challenge 2 — Simp ROI Report
/*
A man tracked 5 weeks of effort trying to get a woman's attention. 
Loop through the records below, calculate the totals, compute the reply rate (rounded to the nearest whole number), and print the report.

Use this data and this verdict rule: 
reply rate below 20% = "Cut your losses", below 50% = "She might like you", otherwise = "Keep going".
*/

const weeks = [
  { amount_spent: 8000,  texts_sent: 40, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 55, texts_replied: 3 },
  { amount_spent: 9000,  texts_sent: 38, texts_replied: 4 },
  { amount_spent: 11000, texts_sent: 42, texts_replied: 2 },
  { amount_spent: 12000, texts_sent: 35, texts_replied: 3 },
];

let totalSpent = 0;
let totalTextsSent = 0;
let totalTextsReplied = 0;

for (const week of weeks) {
  totalSpent += week.amount_spent;
  totalTextsSent += week.texts_sent;
  totalTextsReplied += week.texts_replied;
}

const replyRate = Math.round((totalTextsReplied / totalTextsSent) * 100);

let verdict = "";
if (replyRate < 20) {
  verdict = "Cut your losses";
} else if (replyRate < 50) {
  verdict = "She might like you";
} else {
  verdict = "Keep going";
}

//console.log("\n=== ROI Report ===");
console.log(`Total spent: KES ${totalSpent}`);
console.log(`Texts sent: ${totalTextsSent}`);
console.log(`Replies received: ${totalTextsReplied}`);
console.log(`Reply rate: ${replyRate}%`);
console.log(`Verdict: ${verdict}`);


/*
Total spent: KES 52000
Texts sent: 210
Replies received: 14
Reply rate: 7%
Verdict: Cut your losses
*/