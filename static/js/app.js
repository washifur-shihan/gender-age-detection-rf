const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const loadingBox = document.getElementById("loadingBox");
const resultBox = document.getElementById("resultBox");
const errorBox = document.getElementById("errorBox");
const genderResult = document.getElementById("genderResult");
const ageResult = document.getElementById("ageResult");

imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (e) {
    previewImage.src = e.target.result;
    previewImage.classList.remove("d-none");
  };
  reader.readAsDataURL(file);

  resultBox.classList.add("d-none");
  errorBox.classList.add("d-none");
});

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = imageInput.files[0];
  if (!file) {
    showError("Please select an image first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  loadingBox.classList.remove("d-none");
  resultBox.classList.add("d-none");
  errorBox.classList.add("d-none");

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    loadingBox.classList.add("d-none");

    if (!response.ok) {
      showError(data.error || "Something went wrong.");
      return;
    }

    genderResult.textContent = data.gender;
    ageResult.textContent = data.age_range;
    resultBox.classList.remove("d-none");
  } catch (error) {
    loadingBox.classList.add("d-none");
    showError("Failed to connect to server.");
  }
});

function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove("d-none");
}