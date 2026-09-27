// THE FETCH API
// fetch(url) is a built-in browser function that sends an HTTP request to a URL and returns a Promise. 
// A Promise is an object representing a value that is not available yet but will be resolved in the future. 
// You use await to pause execution until the Promise resolves.


// The full pattern every fetch request follows
const fetchData = async () => {
    try {
        const response= await fetch("https://api.example.com/data");
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.ststus}`);
        }
        const data = await response.json(); // parse JSON body
        console.log(data);
    
    } catch (err) {
        console.error("Fetch failed:", err.message);
    } 
};

fetchData();

