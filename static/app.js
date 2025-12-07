const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");
const submitBtn = document.getElementById("submitBtn");
const loader = document.getElementById("loader");
const resultCard = document.getElementById("result");
const errorBox = document.getElementById("error");

let selectedFile = null;

// Allow clicking drag-box
dropArea.onclick = () => fileInput.click();

// When file selected manually
fileInput.onchange = (e) => {
    selectedFile = e.target.files[0];
    enableButton();
    dropArea.innerHTML = `<p>📄 ${selectedFile.name} selected</p>`;
};

// Drag & drop events
dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.style.background = "#eef3ff";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.background = "white";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.style.background = "white";

    selectedFile = e.dataTransfer.files[0];
    enableButton();
    dropArea.innerHTML = `<p>📄 ${selectedFile.name} selected</p>`;
});

function enableButton() {
    if (selectedFile) {
        submitBtn.disabled = false;
    }
}

// Submit file to backend
submitBtn.onclick = async () => {
    if (!selectedFile) return;

    // Reset states
    loader.classList.remove("hidden");
    resultCard.classList.add("hidden");
    errorBox.classList.add("hidden");

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();
        loader.classList.add("hidden");

        if (!response.ok) {
            showError(data.detail || "Something went wrong.");
            return;
        }

        // Populate results
        document.getElementById("filename").innerText = data.filename;
        document.getElementById("category").innerText = data.predicted_category;
        document.getElementById("snippet").innerText = data.extracted_snippet;

        resultCard.classList.remove("hidden");

    } catch (err) {
        loader.classList.add("hidden");
        showError("Failed to connect to server.");
    }
};

function showError(msg) {
    errorBox.innerText = msg;
    errorBox.classList.remove("hidden");
}
