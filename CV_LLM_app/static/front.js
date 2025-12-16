const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('files');
const submitBtn = document.getElementById('submit');
const status = document.getElementById('status');

let files = [];

// Click pour ouvrir
dropzone.onclick = () => fileInput.click();

dropzone.ondragover = (e) => {
    e.preventDefault();
    dropzone.classList.add('hover');
};

dropzone.ondragleave = () => dropzone.classList.remove('hover');

dropzone.ondrop = (e) => {
    e.preventDefault();
    dropzone.classList.remove('hover');
    updateFiles(e.dataTransfer.files);
};

fileInput.onchange = (e) => updateFiles(e.target.files);

function updateFiles(newFiles) {
    files = Array.from(newFiles);
    dropzone.querySelector('p').textContent = 
        files.length ? `${files.length} fichier(s) sélectionné(s)` : 'Glissez vos fichiers ici';
}

// Envoi
submitBtn.onclick = async () => {
    if (!files.length) {
        alert('Sélectionnez des fichiers');
        return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'Envoi...';

    const formData = new FormData();
    files.forEach(f => formData.append('cv', f));

    try {
        const res = await fetch('/analyse', {
            method: 'POST',
            body: formData
        });

        const data = await res.json();
        
        if (res.ok) {
            status.textContent = data.message;
            status.className = 'success';
            files = [];
            fileInput.value = '';
            dropzone.querySelector('p').textContent = 'Glissez vos fichiers ici';
        } else {
            status.textContent = 'Erreur: ' + data.error;
            status.className = 'error';
        }
    } catch (err) {
        status.textContent = 'Erreur serveur';
        status.className = 'error';
        console.log(err);
    }

    submitBtn.disabled = false;
    submitBtn.textContent = 'Sauvegarder';
};