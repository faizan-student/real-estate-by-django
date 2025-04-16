const phrases = [
    "Your Dream Home Awaits",
    "Smart with AI Insights",
    "Properties Across India",
    "Find Luxury Living",
    "Future-Ready Real Estate"
];

const colors = ['#5ea2ff', '#ffffff', '#7fffd4']; // blue, white, aqua

const typedText = document.querySelector(".typed-text");
const cursor = document.querySelector(".cursor");

let phraseIndex = 0;
let charIndex = 0;
let currentPhrase = "";
let isDeleting = false;
let typingDelay = 100;
let erasingDelay = 50;
let newPhraseDelay = 1500;

let wordColorMap = [];

function assignColorsToWords(phrase) {
    const words = phrase.split(' ');
    return words.map(word => ({
        word,
        color: colors[Math.floor(Math.random() * colors.length)]
    }));
}

function getColoredHTMLByChar(phraseMap, uptoChar) {
    let result = '';
    let charCount = 0;

    for (let i = 0; i < phraseMap.length; i++) {
        const word = phraseMap[i].word;
        const color = phraseMap[i].color;

        // Add a space before word (except the first one)
        if (i !== 0) charCount++; // for the space
        if (charCount >= uptoChar) break;

        let remainingChars = uptoChar - charCount;
        let visiblePart = word.slice(0, remainingChars);

        result += `${i !== 0 ? ' ' : ''}<span style="color:${color}">${visiblePart}</span>`;

        charCount += visiblePart.length;

        if (visiblePart.length < word.length) break;
    }

    return result;
}

function typeLoop() {
    currentPhrase = phrases[phraseIndex];

    if (wordColorMap.length === 0) {
        wordColorMap = assignColorsToWords(currentPhrase);
    }

    if (!isDeleting && charIndex <= currentPhrase.length) {
        typedText.innerHTML = getColoredHTMLByChar(wordColorMap, charIndex++);
        setTimeout(typeLoop, typingDelay);
    } else if (isDeleting && charIndex >= 0) {
        typedText.innerHTML = getColoredHTMLByChar(wordColorMap, charIndex--);
        setTimeout(typeLoop, erasingDelay);
    } else {
        if (!isDeleting) {
            isDeleting = true;
            setTimeout(typeLoop, newPhraseDelay);
        } else {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            wordColorMap = []; // reset for new phrase
            setTimeout(typeLoop, 400);
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(typeLoop, 500);
});
