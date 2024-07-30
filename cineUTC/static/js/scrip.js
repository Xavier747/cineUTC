
const defaultFile = 'https://w7.pngwing.com/pngs/81/570/png-transparent-profile-logo-computer-icons-user-user-blue-heroes-logo-thumbnail.png';
const file = document.getElementById('foto');
const img = document.getElementById('img');
const clearBtn = document.getElementById('clearBtn');
const maximizeLink = document.getElementById('maximizeLink');

file.addEventListener('change', e => {
    if (e.target.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const result = e.target.result;
            img.src = result;
            maximizeLink.href = result; // Actualizar el enlace de Lightbox con la nueva imagen
        }
        reader.readAsDataURL(e.target.files[0]);
    } else {
        img.src = defaultFile;
        maximizeLink.href = defaultFile; // Actualizar el enlace de Lightbox con la imagen por defecto
    }
});

clearBtn.addEventListener('click', () => {
    file.value = ''; // Limpiar el input file
    img.src = defaultFile; // Resetear la imagen al valor por defecto
    maximizeLink.href = defaultFile; // Resetear el enlace de Lightbox con la imagen por defecto
});