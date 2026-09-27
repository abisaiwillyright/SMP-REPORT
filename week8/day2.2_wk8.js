// Event - is a signal that browser send when something happens.

// Wire up the buttons in the live demo below.
const addBtn = document.querySelector('#3addBtn');
const clearBtn = document.querySelector('#d3clearBtn');
const logInput = document.querySelector('#d3input');
const logList = document.querySelector('#3list');
const countE1 = document.querySelector('#d3count');

let count = 0;

addBtn.addEventListener('click', () => {
    const value = logInput.value.trim();
    if (!value) {
        console.log("No input to add.");
        return;
    }
    // Create new list item
    const li = document.createElement('li');
    li.textContent = value;
    li.style.padding = "3px 0";
    li.style.borderBottom = "1px solid #30363d";
    logList.appendChild(li);

    count++;
    CSSCounterStyleRule.textContent = `Entries: ${count}`;
    logInput.value = "";
    logInput.focus();
    console.log(`Added: "${value}"`);
})

clearBtn.addEventListener('click', () => {
    logList.innerHTML = "";
    CSSCounterStyleRule.textContent = "Entries: 0";
    console.log("Log cleared.");
})

// Keyboard shortcut: Entre key submits
logInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        addBtn.click();
    }
});

console.log("Eventlisteners attached. Use the panel below.")

