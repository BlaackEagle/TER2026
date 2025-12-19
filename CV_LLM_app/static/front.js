const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('files');
const submitBtn = document.getElementById('submit');
const status = document.getElementById('status');

const zoneResultat = document.getElementById('zone-resultat');
const contenuCv = document.getElementById('contenu-cv');
const promptInput = document.getElementById('user-prompt');

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
    formData.append('prompt', promptInput.value);
    try {
        const res = await fetch('/analyse', {
            method: 'POST',
            body: formData
        });

        const data = await res.json();

        if (res.ok) {
            status.textContent = data.message;
            status.className = 'success';

            const listeCVs = data.data;

            if (zoneResultat) {
                zoneResultat.style.display = 'block';
                zoneResultat.innerHTML = "";

                listeCVs.forEach(cv => {
                    const box_result = document.createElement('div');

                    box_result.className = 'cv-card';

                    const vectorPreview = cv.vecteur.slice(0, 8).map(n => n.toFixed(5)).join(', ');

                    box_result.innerHTML = `
                       <h3>${cv.nom_fichier}</h3>
                        
                        <div class="cv-stats">
                            <p><strong>Dimensions :</strong> ${cv.forme_vecteur}</p>
                            <p><strong>Vecteur (extrait) :</strong> <span class="vector-data">[ ${vectorPreview}, ... ]</span></p>
                            <p><strong>Pertinence : ${cv.pertinence} %</strong></p>
                        </div>

                        <p class="text-label"><strong>Contenu du CV :</strong></p>
                        
                        <div class="cv-content-box">
                            ${cv.texte_fichier}
                        </div>`;

                        zoneResultat.appendChild(box_result);
                    });
                }

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

// rajout fichiers
function updateFiles(newFiles) {
    const nouveauxFichiers = Array.from(newFiles);
    nouveauxFichiers.forEach(nouveau => {
        if (!files.some(f => f.name === nouveau.name)) {
            files.push(nouveau);
        }
    });

    const p = dropzone.querySelector('p');

    if (files.length > 0) {
        p.innerHTML = `
            <span style="font-weight: bold; font-size: 1.1em; color: #2d3748;">
                ${files.length} fichier(s) prêt(s) à l'analyse
            </span>
            <br>
            <span style="font-size: 0.85em; opacity: 0.7;">
                Glissez d'autres fichiers ici ou <span class="link">parcourir</span>
            </span>
        `;
    } else {
        p.innerHTML = 'Glissez vos fichiers ici ou <span class="link">parcourir</span>';
    }
}