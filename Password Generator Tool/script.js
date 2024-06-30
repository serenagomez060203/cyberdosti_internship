document.getElementById('generate').addEventListener('click', generatePassword);
document.getElementById('length').addEventListener('input', syncLength);
document.getElementById('lengthValue').addEventListener('input', syncLength);

function syncLength(e) {
    const value = e.target.value;
    document.getElementById('length').value = value;
    document.getElementById('lengthValue').value = value;
}

function generatePassword() {
    const length = document.getElementById('length').value;
    const uppercase = document.getElementById('uppercase').checked;
    const lowercase = document.getElementById('lowercase').checked;
    const numbers = document.getElementById('numbers').checked;
    const symbols = document.getElementById('symbols').checked;
    const extended = document.getElementById('extended').checked;

    let characters = '';
    if (uppercase) characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (lowercase) characters += 'abcdefghijklmnopqrstuvwxyz';
    if (numbers) characters += '0123456789';
    if (symbols) characters += '-_.#$@%';
    if (extended) characters += '"+(){}[]?&,*<>|:;^';

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    document.getElementById('password').value = password;
}
