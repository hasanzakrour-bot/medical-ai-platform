// =====================================
// DASHBOARD.JS - التصحيحات الكتابية
// =====================================

const API_BASE = "http://localhost:8000";

// =====================================
// GET HEADERS WITH JWT
// =====================================
function getHeaders() {
    const token = localStorage.getItem("token");
    const headers = {};
    if (token) headers["Authorization"] = `Bearer ${token}`;
    return headers;
}

// =====================================
// LOAD DIAGNOSIS HISTORY
// =====================================
async function loadDiagnosisHistory() {
    const table = document.getElementById("history_table");
    if (!table) return;

    try {
        const res = await fetch(`${API_BASE}/diagnosis/history`, {
            headers: getHeaders()
        });
        const data = await res.json();
        table.innerHTML = "";

        data.forEach(item => {
            const row = document.createElement("tr");
            row.innerHTML = 
                `<td>${item.date}</td>
                <td>${item.disease}</td>
                <td>${(item.confidence*100).toFixed(1)}%</td>
                <td>${item.category}</td>`;
            table.appendChild(row);
        });
    } catch (err) {
        console.error("Failed to load history:", err);
        table.innerHTML = `<tr><td colspan="4">Failed to load history</td></tr>`;
    }
}

// =====================================
// LOAD DISEASE STATISTICS CHART
// =====================================
async function loadDiseaseStats() {
    const ctx = document.getElementById("diseaseChart");
    if (!ctx) return;

    try {
        const res = await fetch(`${API_BASE}/stats/diseases`, {
            headers: getHeaders()
        });
        const stats = await res.json();

        // Chart.js setup
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: stats.labels,
                datasets: [{
                    label: "Detected Diseases",
                    data: stats.values,
                    backgroundColor: "#3498db"
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: {
                        display: true,
                        text: "Disease Statistics"
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    } catch (err) {
        console.error("Failed to load chart:", err);
        const container = document.getElementById("chart_container");
        if (container) container.innerHTML = "Failed to load chart";
    }
}

// =====================================
// UPLOAD IMAGE IN DASHBOARD
// =====================================
async function uploadDashboardImage() {
    const fileInput = document.getElementById("dashboard_image_input");
    const category = document.getElementById("dashboard_disease_category").value;
    const file = fileInput;


    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);
    formData.append("category", category);

    const resultBox = document.getElementById("dashboard_diagnosis_result");
    resultBox.innerHTML = `<div class="loading-container"><div class="spinner"></div><p>Analyzing...</p></div>`;

    try {
        const res = await fetch(`${API_BASE}/diagnosis/analyze`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: formData
        });

        const data = await res.json();
        displayDashboardDiagnosis(data);

    } catch (err) {
        resultBox.innerHTML = "Server error";
    }
}

// =====================================
// DISPLAY DIAGNOSIS RESULT IN DASHBOARD
// =====================================
function displayDashboardDiagnosis(data) {
    const box = document.getElementById("dashboard_diagnosis_result");
    if (!data) {
        box.innerHTML = "No result";
        return;
    }

    const disease = data.disease || "Unknown";
    const confidence = data.confidence ? (data.confidence*100).toFixed(2) : "N/A";
    const explanation = data.explanation || "No explanation available";
    const tips = data.medical_tips || "No advice available";

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
// INIT DASHBOARD
// =====================================
document.addEventListener("DOMContentLoaded", function() {
    loadDiagnosisHistory();
    loadDiseaseStats();
});
