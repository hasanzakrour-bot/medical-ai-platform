// =====================================
// CONFIGURATION
// =====================================

const API_BASE = "http://localhost:8000";

let authToken = localStorage.getItem("token") || null;


// =====================================
// AUTH TOKEN MANAGEMENT
// =====================================

function setAuthToken(token) {
    authToken = token;
    localStorage.setItem("token", token);
}

function getHeaders() {
    const headers = {};
    if (authToken) {
        headers["Authorization"] = `Bearer ${authToken}`;
    }
    return headers;
}

// =====================================
// UI HELPERS
// =====================================

function showMessage(elementId, message, error=false) {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.innerText = message;
    el.style.color = error ? "#ff4d4d" : "#2ecc71";
}

// =====================================
// LOGIN
// =====================================

async function login() {
    const email = document.getElementById("login_email").value;
    const password = document.getElementById("login_password").value;

    try {
        const res = await fetch(`${API_BASE}/auth/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await res.json();

        if (data.access_token) {
            setAuthToken(data.access_token);
            showMessage("login_msg", "Login successful");
        } else {
            showMessage("login_msg", data.detail || "Login failed", true);
        }

    } catch (err) {
        showMessage("login_msg", "Server error", true);
    }
}

// =====================================
// IMAGE PREVIEW
// =====================================

function previewImage() {
    const fileInput = document.getElementById("image_input");
    const preview = document.getElementById("image_preview");
    const file = fileInput;
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };
    reader.readAsDataURL(file);
}

// =====================================
// LOADING UI
// =====================================

function showLoading() {
    const resultBox = document.getElementById("diagnosis_result");
    resultBox.innerHTML = 
        `<div class="loading-container">
            <div class="spinner"></div>
            <p>Analyzing medical image...</p>
        </div>`;
}

// =====================================
// UPLOAD IMAGE + AI DIAGNOSIS
// =====================================

async function uploadMedicalImage() {
    const fileInput = document.getElementById("image_input");
    const category = document.getElementById("disease_category").value;
    const file = fileInput;

    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);
    formData.append("category", category);

    showLoading();

    try {
        const res = await fetch(`${API_BASE}/diagnosis/analyze`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${authToken}`
            },
            body: formData
        });

        const data = await res.json();
        displayDiagnosis(data);

    } catch (err) {
        document.getElementById("diagnosis_result").innerHTML = "Server error";
    }
}

// =====================================
// DISPLAY DIAGNOSIS RESULT
// =====================================

function displayDiagnosis(data) {
    const box = document.getElementById("diagnosis_result");
    if (!data) {
        box.innerHTML = "No result returned";
        return;
    }
    const disease = data.disease || "Unknown";
    const confidence = data.confidence ? (data.confidence * 100).toFixed(2) : "N/A";
    const explanation = data.explanation || "No explanation available";
    const tips = data.medical_tips || "No medical advice available";

    box.innerHTML = 
        `<div class="diagnosis-card">
            <h2>Diagnosis Result</h2>
            <p><strong>Disease:</strong> ${disease}</p>
            <p><strong>Confidence:</strong> ${confidence}%</p>
            <h3>Explanation</h3>
            <p>${explanation}</p>
            <h3>Medical Advice</h3>
            <p>${tips}</p>
        </div>`;
}

// =====================================
// CHAT STREAMING EFFECT
// =====================================

function streamText(element, text, speed=20) {
    let i = 0;
    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }
    typing();
}

// =====================================
// MEDICAL CHAT
// =====================================

async function sendMedicalQuestion() {
    const input = document.getElementById("chat_input");
    const message = input.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat_box");
    chatBox.innerHTML += `<div class="chat-user">${message}</div>`;
    input.value = "";

    const aiMsg = document.createElement("div");
    aiMsg.className = "chat-ai";
    chatBox.appendChild(aiMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const res = await fetch(`${API_BASE}/chat/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                ...getHeaders()
            },
            body: JSON.stringify({
                question: message
            })
        });

        const data = await res.json();
        streamText(aiMsg, data.answer || "No response");

    } catch (err) {
        aiMsg.innerHTML = "Server error";
    }
}

// =====================================
// ENTER KEY FOR CHAT
// =====================================

document.addEventListener("DOMContentLoaded", function() {
    const chatInput = document.getElementById("chat_input");
    if (chatInput) {
        chatInput.addEventListener("keypress", function(e) {
            if (e.key === "Enter") {
                e.preventDefault();
                sendMedicalQuestion();
            }
        });
    }
});

// =====================================
// DRAG & DROP IMAGE UPLOAD
// =====================================

function initDragDrop() {
    const dropArea = document.getElementById("drop_area");
    const fileInput = document.getElementById("image_input");
    if (!dropArea) return;

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.classList.add("drag-over");
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.classList.remove("drag-over");
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.classList.remove("drag-over");

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            previewImage();
        }
    });
}

document.addEventListener("DOMContentLoaded", initDragDrop);
