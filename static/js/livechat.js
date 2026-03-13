function sendMessage() {
    let msg = document.getElementById('user_input').value;
    if (!msg) return;
    fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: msg})
    })
    .then(res => res.json())
    .then(data => {
        let chatbox = document.getElementById('chatbox');
        chatbox.innerHTML += `<p><b>You:</b> ${msg}</p>`;
        chatbox.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
        document.getElementById('user_input').value = '';
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}
