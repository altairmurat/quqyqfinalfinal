const API_URL = "https://quqyqfinalfinal.onrender.com";
let token = localStorage.getItem("token");

// ... (other existing functions like fetchCourses, fetchLessons, etc.)

async function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (response.ok) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/static/courses.html";
    } else {
        alert(data.detail);
    }
}

async function register() {
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;
    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (response.ok) {
        alert("Registration successful! Please log in.");
        window.location.href = "/static/index.html";
    } else {
        alert(data.detail);
    }
}

// ... (rest of the script)

async function fetchCourses() {
    const response = await fetch(`${API_URL}/courses`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const courses = await response.json();
    const coursesList = document.getElementById("courses-list");
    coursesList.innerHTML = courses.map(course => {
        let page;
        if (course.id === 1) {
            page = "lessons";
        } else if (course.id === 2) {
            page = "material";
        } else if (course.id === 3) {
            page = "book";
        } else {
            page = "book"; // Default fallback
        }
        return `
            <div class="course-card">
                <a href="/static/${page}.html?course_id=${course.id}">
                    ${course.name}
                </a>
            </div>
        `;
    }).join("");
}

async function fetchLessons(courseId) {
    const response = await fetch(`${API_URL}/courses/${courseId}/lessons`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const lessons = await response.json();
    const lessonsList = document.getElementById("lessons-list");
    lessonsList.innerHTML = lessons.map(lesson => `
        <div>
            <a href="/static/lesson.html?id=${lesson.id}&course_id=${courseId}">${lesson.title}</a>
        </div>
    `).join("");
}

async function fetchLesson(lessonId) {
    try {
        const response = await fetch(`${API_URL}/lessons/${lessonId}`, {
            headers: { Authorization: `Bearer ${token}` }
        });
        if (!response.ok) {
            throw new Error(`Failed to fetch lesson: ${response.status} ${response.statusText}`);
        }
        const lesson = await response.json();
        document.getElementById("lesson-title").textContent = lesson.title;
        document.getElementById("transcript").innerHTML = lesson.transcript || "";
        const media = document.getElementById("media");
        const pdf_lesson = document.getElementById("pdf_lesson");
        const pdf_answers = document.getElementById("pdf_answers");
        if (lesson.pdf_lesson) {
            pdf_lesson.innerHTML = `<embed src="${lesson.pdf_lesson}" width="100%" height="200px" style="border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);">`;
        }
        if (lesson.video_url) {
            // Check if it's a Google Drive URL
            if (lesson.video_url.includes('drive.google.com/file/d/')) {
                // Use iframe for Google Drive embed
                media.innerHTML = `
                    <iframe 
                        src="${lesson.video_url}" 
                        width="100%" 
                        height="300" 
                        frameborder="0" 
                        allowfullscreen
                        style="border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);"
                    ></iframe>
                `;
            } else {
                // Standard video tag for other URLs
                media.innerHTML = `<video controls src="${lesson.video_url}" style="width: 100%; max-height: 400px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);"></video>`;
            }
        }
        if (lesson.pdf_answers) {
            pdf_answers.innerHTML = `<embed src="${lesson.pdf_answers}" width="100%" height="200px" style="border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);">`;
        }
        return lesson;
    } catch (error) {
        console.error(error);
        alert(`Error loading lesson: ${error.message}`);
    }
}

// ... (other existing functions)

async function toggleSecondaryPDF() {
    const secondaryPdf = document.getElementById("pdf_answers");
    const toggleButton = document.getElementById("toggle-pdf-btn");
    if (secondaryPdf.style.display === "none") {
        secondaryPdf.style.display = "block";
        toggleButton.textContent = "Жауаптарды тығып қою";
    } else {
        secondaryPdf.style.display = "none";
        toggleButton.textContent = "Дұрыс жауаптарын көру";
    }
}

// ... (rest of the script)

async function fetchMaterials(courseId) {
    const response = await fetch(`${API_URL}/courses/${courseId}/materials`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const materials = await response.json();
    const materialsList = document.getElementById("materials-list");
    materialsList.innerHTML = materials.map(material => `
        <div>
            <a href="/static/material.html?id=${material.id}&course_id=${courseId}">${material.title}</a>
        </div>
    `).join("");
}

async function fetchMaterial(materialId) {
    const response = await fetch(`${API_URL}/materials/${materialId}`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const material = await response.json();
    document.getElementById("material-title").textContent = material.title;
    document.getElementById("media").innerHTML = `<embed src="${material.pdf_url}" width="100%" height="400px">`;
}

async function fetchBooks(courseId) {
    const response = await fetch(`${API_URL}/courses/${courseId}/books`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const books = await response.json();
    const booksList = document.getElementById("books-list");
    booksList.innerHTML = books.map(book => `
        <div>
            <a href="/static/book.html?id=${book.id}&course_id=${courseId}">${book.title}</a>
        </div>
    `).join("");
}

async function fetchBook(bookId) {
    const response = await fetch(`${API_URL}/books/${bookId}`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    const book = await response.json();
    document.getElementById("book-title").textContent = book.title;
    document.getElementById("media").innerHTML = `<embed src="${book.pdf_url}" width="100%" height="400px">`;
}

async function submitAnswer() {
    const urlParams = new URLSearchParams(window.location.search);
    const lessonId = urlParams.get('id');
    console.log("URL Params:", urlParams.toString()); // Debug log
    console.log("lessonId:", lessonId); // Debug log
    if (!lessonId) {
        alert("No lesson selected. Please select a lesson first.");
        return;
    }
    const content = document.getElementById("answer-input").value;
    try {
        const response = await fetch(`${API_URL}/lessons/${lessonId}/answer`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ content })
        });
        if (!response.ok) {
            throw new Error(`Failed to submit answer: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        document.getElementById("answer-response").textContent = data.response;
    } catch (error) {
        console.error(error);
        alert(`Error submitting answer: ${error.message}`);
    }
}

async function goToNextLesson() {
    // Fetch next lesson ID (assumes ordered IDs for simplicity)
    const urlParams = new URLSearchParams(window.location.search);
    const lessonId = parseInt(urlParams.get('id'));
    const courseId = urlParams.get('course_id');
    window.location.href = `/static/lesson.html?id=${lessonId + 1}&course_id=${courseId}`;
}

async function goToPreviousLesson() {
    const urlParams = new URLSearchParams(window.location.search);
    const lessonId = parseInt(urlParams.get('id'));
    const courseId = urlParams.get('course_id');
    if (lessonId > 1) {
        window.location.href = `/static/lesson.html?id=${lessonId - 1}&course_id=${courseId}`;
    }

}
