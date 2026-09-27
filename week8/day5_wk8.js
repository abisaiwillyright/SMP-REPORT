// Mini-Project: Browser-Based AI Tool
// A complate browser tool that accepts daily inputs, runs a resle-based prediction, generates a coaching message and diplays results in a live UI without a page reload.

// SMP Daily AI Coach (Browser Tool)
// A browser-based tool that accepts sleep, water, and step count data, predicts goal outcome with a confidence score, and generates a coaching message.
// No server needed. Everything runs client-side in JavaScript.

// Four steps:
// Step 1: Build the prediction engine in JavaScript
// Step 2: Build the coaching message generator
// Step 3: Wire the form inputs and DOM display
// Step 4: Add session history log

// Step 1: Build the prediction engine in JavaScript
// Returns { hitGoal: bool, confidence: number (0-1), score: number }

const predictGoal = (sleep, water, steps) => {
    // Weighted score (max 100)
    const sleepScore = Math.min(sleep / 8.0, 1.0) * 35; // 35% weight
    const stepsScore = Math.min(steps / 12000, 1.0) * 40; // 40$ weight
    const waterScore = Math.min(water / 10.0, 1.0) * 25; // 25% weight
    const totalScore = sleepScore + waterScore + stepsScore;
    const hitGoal = totalScore >= 60;

    // Confidence: how far from the 60-point threshold (capped at 95%)
    const distance = Math.abs(totalScore - 60);
    const confidence = Math.min(0.50 + distance * 0.012, 0.95);

    return { hitGoal, confidence, score: Math.round(totalScore)};
};

// Test cases
const testDAys = [
  { label: "Weak day", sleep: 5.5, water: 4, steps: 7800 },
  { label: "Strong day", sleep: 8.0, water: 10, steps: 12100 },
  { label: "Borderline", sleep: 7.0, water: 8, steps: 9500 },
  { label: "Sleep-focused", sleep: 9.0, water: 6, steps: 8000 }, 
];

testDAys.forEach(d => {
    const result = predictGoal(d.sleep, d.water, d.steps);
    const out = result.hitGoal ? "HIT" : "MISS";

    console.log(`${d.label.padEnd(16)} | Score: ${String(result.score).padStart(2)} | ${out} | Conf: ${(result.confidence * 100).toFixed(0)}%`);
});
console.log()


// Step 2: Build the coaching message generator
// The coaching function takes the prediction result and input values, then returns a two-sentence coaching message.

const COACHING = {
    // key: `${hitGoal ? 1 : 0}${sleep >= 7 ? 1 : 0}${water > 8 ? 1 : 0}`
    "111": ["Strong inputs, strong output. Sleep and hydration are locked in.",
        "Keep this baseline and the steps will follow."],
    "110": ["Hit the goal despite low water. Sleep is the primary driver.",
        "Close the dydration tomorrow."],
    "101": ["Water carried today despite low sleep.",
        "Shore up sleep tonight. Hitting goal on low sleep has hidden costs."],
    "100": ["Goal hit but both inputs are below threshold. That is willpower, not system.",
        "Build the foundation: sleep first, water second."],
    "010": ["Sleep is solid, hydration is low, goal was missed.",
        "Add two glasses of water tomorrow. Hydration shiftfs output more than expected."],
    "000": ["Both sleep and water are below threshold and the goal ws missed.",
        "Rest tonight: 8 hours minimum, 10 galsses tomorrow."],        
};

const getCoaching = (sleep, water, hitGoal) => {
    const key = `${hitGoal ? 1 : 0}${sleep >= 7 ? 1 : 0}${water >= 8 ? 1 : 0}`;
    const [line1, line2] = COACHING[key];
    return `${line1} ${line2}`;
};

// Test
const cases = [
    [8.0, 10, true],
    [5.5, 4, false],
    [7.5, 6, true],
    [6.0, 5, false],
];
console.log("\n===== COACHING MESSAGE =====")
cases.forEach(([sleep, water, hit]) => {
    const msg = getCoaching(sleep, water, hit);
    console.log(`[${hit ? "HIT" : "MISS"}] sleep=${sleep} water=${water}`);
        console.log(` ${msg}`);
        console.log();
});



// Step 3: Wire the form inputs and DOM display
// Wire the live form

const form = document.querySelector('#coachForm');
const display = document.querySelector('#coachDisplay');

if (form && display) {
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const sleep = parseFloat(document.querySelector('#inSleep').value);
        const water = parseInt(document.querySelector('#inWater').value, 10);
        const steps = parseInt(document.querySelector('#inSteps').value, 10);

        if (Number.isNaN(sleep) || Number.isNaN(water) || Number.isNaN(steps)) {
            display.className = 'ai-response idle';
            display.innerHTML = '<div class="label-sm">Error</div><div class="coaching">All three fields are required.</div>';
            return;
        }

        const result = predictGoal(sleep, water, steps);
        const coaching = getCoaching(sleep, water, result.hitGoal);
        const outcome = result.hitGoal ? 'HIT GOAL' : 'MISS GOAL';
        const confpct = (result.confidence * 100).toFixed(0);

        display.className = `ai-response ${result.hitGoal ? 'hit' : 'miss'}`;
        display.innerHTML = `
            <div class="label-sm">Prediction</div>
            <div class="prediction">${outcome} (${confpct}% confidence · score: ${result.score}/100)</div>
            <div class="label-sm" style="margin-top:0.8rem;">Coaching</div>
            <div class="coaching">${coaching}</div>
        `;

        console.log(`Submitted: sleep=${sleep}h water=${water}gl steps=${steps.toLocaleString()}`);
        console.log(`Result: ${outcome} | ${confpct}% confidence | score ${result.score}`);
    });
}

console.log('Form wired. Use the SM Coach tool below.');
console.log()




// Step 4: Add session history log
// Session store (lives in memory for this page session)
const sessionLog = [];

const logEntry = (sleep, water, steps, hitGoal, confidence, score) => {
  const entry = {
    id:         sessionLog.length + 1,
    time:       new Date().toLocaleTimeString(),
    sleep, water, steps, hitGoal, confidence, score
  };
  sessionLog.push(entry);
  return entry;
};

const renderHistory = () => {
  const tableEl = document.querySelector('#historyTable');
  if (!sessionLog.length) {
    tableEl.innerHTML = '<tr><td colspan="6" style="color:var(--muted);text-align:center;padding:1rem;">No entries yet.</td></tr>';
    return;
  }
  tableEl.innerHTML = sessionLog.map(e => {
    const outcomeColor = e.hitGoal ? "#4ecca3" : "#f5a623";
    const outcome = e.hitGoal ? "HIT" : "MISS";
    return `<tr>
      <td style="color:#8b949e;font-size:0.8rem;">${e.time}</td>
      <td>${e.sleep}h</td>
      <td>${e.water} gl</td>
      <td>${e.steps.toLocaleString()}</td>
      <td style="color:${outcomeColor};font-weight:700;">${outcome}</td>
      <td style="color:#a0a0b0;">${(e.confidence * 100).toFixed(0)}%</td>
    </tr>`;
  }).join('');
};

// Hook into the existing coach form

const form2 = document.querySelector('#coachForm2');
form2.addEventListener('submit', (event) => {
  event.preventDefault();
  const sleep = parseFloat(document.querySelector('#h_sleep').value);
  const water = parseInt(document.querySelector('#h_water').value);
  const steps = parseInt(document.querySelector('#h_steps').value);

  if (isNaN(sleep) || isNaN(water) || isNaN(steps)) return;

  const result = predictGoal(sleep, water, steps);
  const entry  = logEntry(sleep, water, steps, result.hitGoal, result.confidence, result.score);

  renderHistory();
  console.log(`Entry #${entry.id} logged: ${result.hitGoal ? "HIT" : "MISS"} | score ${result.score}`);

  // Reset inputs
  form2.reset();
});

// Render empty state
renderHistory();

console.log("History form wired. Submit entries using the form below.");
console.log()
