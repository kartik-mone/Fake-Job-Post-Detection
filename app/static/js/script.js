// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const jobForm = document.getElementById('jobForm');
    const jobDescription = document.getElementById('jobDescription');
    const resultDiv = document.getElementById('result');
    
    jobForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        if (!jobDescription.value.trim()) {
            alert("Job description cannot be empty!");
            return;
        }

        const jobData = new FormData();
        jobData.append('job_description', jobDescription.value);
        
        fetch('/predict', {
            method: 'POST',
            body: jobData
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = `<h2>Result: ${data.result}</h2>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
