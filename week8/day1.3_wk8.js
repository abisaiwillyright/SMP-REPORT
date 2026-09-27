// Objects.
// An object is a collection of key-value pairs.
// In JavaScript, objects use curly braces and are equivalent to Python dictionaries.
// Keys are strings. Values can be any type, including other objects or arrays.

const member = {
    name: "Wanjiku Muthoni",
    city: "nairobi",
    protocol: "SMP Phase 2",
    weeksComplated: 4,
    skills: ["copywriting", "social media"],
    stats: {
        avgSleep: 7.2,
        avgSteps: 9800,
        goalHitRate: 0.71
    }
};

// Access with dot notation
console.log("Name:", member.name);
console.log("City:", member.city);
console.log("Weeks done:", member.weeksComplated);

// Access nested object
console.log("Avg sleep:", member.stats.avgSleep);
console.log("Goal hit rate:", `${(member.stats.goalHitRate * 100).toFixed(0)}%`);

// Access array inside object
console.log("Skills:", member.skills.join(","));

// Add a new key
member.lastActive = '2026-09-09';
console.log("\nLast active:", member.lastActive);

// Destructure to pull out named keys
const { name, city, weeksComplated } = member;
console.log(`\n${name} | ${city} | Week ${weeksComplated}`);

// Object.key and Object.entries
console.log("\nTop-level keys:", Object.keys(member));