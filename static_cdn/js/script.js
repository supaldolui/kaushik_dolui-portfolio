const textEl = document.getElementById("text");
const text = "KAUSHIK DOLUI";
let idx = 0; // Start with 0 to add "|" at the beginning
let isBlinking = true;

writeText();

function writeText() {
  const displayedText = text.slice(0, idx) + (isBlinking ? "|" : "");
  textEl.innerText = displayedText;
  isBlinking = !isBlinking; // Toggle blinking

  idx++;

  if (idx > text.length) {
    idx = 0; // Reset to 0 to start over
  }

  setTimeout(writeText, 120); // Set text change interval to 500 milliseconds (half a second)
}

