const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('files');
const submitBtn = document.getElementById('submit');
const status = document.getElementById('status');

const zoneResultat = document.getElementById('zone-resultat');
const contenuCv = document.getElementById('contenu-cv');

const sendBtn = document.getElementById('send-btn');
const promptInput = document.getElementById('prompt-input');
const chatHistory = document.getElementById('chat-history');


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

sendBtn.onclick = async () => {
    const question = promptInput.value;
    if (!question) return;

    chatHistory.innerHTML += `<p><strong>Vous :</strong> ${question}</p>`;
    promptInput.value = '';
    sendBtn.disabled = true;
    sendBtn.textContent = '...';

    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: question })
        });

        const data = await res.json();

        if (res.ok) {
            let reponseHTML = `<div style="background: #f0f4f8; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p><strong>IA :</strong> ${data.reponse}</p>`;
            
            if (data.source) {
                reponseHTML += `<p style="font-size: 0.9em; color: #555; margin-top: 5px;">
                    <em>Extrait de ${data.source} :</em><br>
                    "${data.extrait}"
                </p>`;
            }
            reponseHTML += `</div>`;
            
            chatHistory.innerHTML += reponseHTML;
        } else {
            chatHistory.innerHTML += `<p style="color: red;">Erreur: ${data.reponse || "Problème serveur"}</p>`;
        }

    } catch (err) {
        console.error(err);
        chatHistory.innerHTML += `<p style="color: red;">Erreur de connexion</p>`;
    }

    sendBtn.disabled = false;
    sendBtn.textContent = 'Envoyer';
    
    chatHistory.scrollTop = chatHistory.scrollHeight;
};