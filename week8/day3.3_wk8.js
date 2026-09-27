// Fetch with DOM: Live Data Display
// The pattern used in production: fetch data, then update the DOM with the results. The user sees a loading state, then the data appears without any page reload.

// Fetch data then update the DOM
// Simulated member API
const simulatedFetch = async (endpoint) => {
    const members = [
        { name: "Brian Temba", city: "Nairobi", steps: 11240, sleep: 7.5, goal: true },
        { name: "Ben Kimeu", city: "Mombasa", steps: 8900, sleep: 6.2, goal: false },
        { name: "Kevin Kimido", city: "Kisumu", steps: 10050, sleep: 8.0, goal: true },
        { name: "Alice Oside", city: "Nakuru", steps: 12300, sleep: 8.0, goal: true },
        { name: "Vivian Agita", city: "Eldoret", steps: 7200, sleep: 7.8, goal: true },  
    ];
    return { ok: true, json: async () => members };
};

// Target element in demo panel below
const display = document.querySelector('#f3display');
const loadBtn = document.querySelector('#f3loadBtn');

const loadAndDisplay = async () => {
    display.textContent = "loading...";
    display.style.color = "#f5a623";

    try {
        const response = await simulatedFetch("/api/members");
        const members = await response.json();

        // Build HTML table from data
        const row = members.map(m => {
            const goalColor = m.goal ? "#4ecca3" : "3ff7b72";
            const goalText = m.goal ? "HIT" : "MISS";
            return `<tr>
            <td style="color:#eaeaea;padding:6px 8px;">${m.name}</td>
            <td style="color:#a0a0b0;padding:6px 8px;">${m.steps.toLocaleString()}</td>
            <td style="color:#a0a0b0;padding:6px 8px;">${m.sleep}h</td>
            <td style="color:${goalColor};font-weight:700;padding:6px 8px;">${goalText}</td>
            </tr>`;
        }).join('');

        display.style.color = "inherit";
        display.innerHTML = `
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem;">
        <thead>
        <tr style="background:#0f3460;">
        <th style="padding:6px 8px;text-align:left;">Name</th>
        <th style="padding:6px 8px;text-align:left;">Steps</th>
        <th style="padding:6px 8px;text-align:left;">Sleep</th>
        <th style="padding:6px 8px;text-align:left;">Goal</th>
        </tr>
        </thead>
        <tbody>${row}</tbody>
        </table>
        `;
        console.log(`Rendered ${members.length} members in the DOM.`);
    } catch (err) {
        display.textContent = "Error: " + err.message;
        display.style.color = "#ff7b72";
        console.log("Fetch failed:", err.message);
    }
};

// Wire the button
loadBtn.addEventListener('click', loadAndDisplay);
console.log("Click 'Load Members' in the panel below.");