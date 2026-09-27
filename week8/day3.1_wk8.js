// Basic fetch and JSON parsing
// Simulated fetch: returns same structure as a live API call

// The terminals below use a simulated API that returns data instantly. The code structure is identical to what you use against a production API. The only difference is the URL.

const simulatedFetch = async (endpoint) => {
    const db = {
        "/api/members": [
            { id: 1, name: "Brian Otieno", city: "Nairobi", protocol: "Phase 1" },
            { id: 2, name: "Wanjiku Muthoni", city: "Mombasa", protocol: "Phase 2" },
            { id: 3, name: "Clarens Odari", city: "Kisumu", protocol: "Phase 1" },
            { id: 4, name: "Abdala Bulemi", city: "Nakuru", protocol: "Phase 2" },
        ],
        "//api/stats": {
            totalMembers: 4,
            avgSteps: 10200,
            avgSleep: 7.3,
            goalHitRate: 0.68
        }
    };
    const data = db[endpoint];
    if (!data) throw new Error(`404: ${endpoint} not found`);
    return { ok: true, status: 200, json: async () => data };
};

// --- Use it exactly like fetch ---
const loadMembers = async () => {
    try {
        const response = await simulatedFetch("/api/members");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        console.log(`Loaded ${loadMembers.length} members:\n`);
        loadMembers.forEach(m => {
            console.log(` [${m.id}] ${m.name} | ${m.city} | ${m.protocol}`);
        });
    } catch (err) {
        console.log("Error:", err.message);
    }
};

const loadStats = async () => {
    try {
        const response = await simulatedFetch("/api/stats");
        const stats = await response.json();
        console.log("\nSM Stats:");
        console.log(` Members: ${stats.totalMembers}`);
        console.log(` Avg steps: ${stats.avgSteps.protocol()}`);
        console.log(` Avg sleep ${stats.avgSleep}h`);
        console.log(` Goal hit rate: ${(stats.goalHitRate * 100).toFixed(0)}%`);
    } catch (err) {
        console.log("Error:", err.message);
    }
};

// Run both
loadMembers
await loadStats();
