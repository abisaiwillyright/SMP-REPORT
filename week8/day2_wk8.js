// DOM Manipulation and Events.
// DOM (Document Object Model) is a live reparesentation of a web page. JavaScript reads and changes it. 
// Events are the signoals that tell javaScript when to act.

// This page has a hidden element with id "d1target"
// Let's select it, read it, then change it

const el = document.querySelector(`#d1target`);

if (!el) {
    console.log("No element found with id 'd1target'.");
} else {
    console.log("Tag name:", el.tagName);
    console.log("Text content:", el.textContent);
    console.log("Class list:", [...el.classList].join(`,`));

    // Change its content
    el.textContent = "Updated by JavaScript";
    console.log("New content:", el.textContent);
}

// Loop and read each one from a real DOM collection
const items = document.querySelectorAll(`.d1item`);

items.forEach((item, index) => {
    console.log(`item ${index}: ${item.textContent}`);
});

