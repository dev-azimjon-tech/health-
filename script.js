document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.getElementById('chat-body');
    const input = document.getElementById('input');
    const historyDiv = document.getElementById('history');
    let history = JSON.parse(localStorage.getItem('chatHistory') || '[]');

    function appendMessage(sender, text) {
        const msg = document.createElement('div');
        msg.classList.add('chat-msg', sender);
        msg.innerText = text;
        chatBody.appendChild(msg);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function updateHistory(symptoms, diagnosis, treatment) {
        const record = {
            symptoms,
            diagnosis,
            treatment,
            time: new Date().toLocaleString()
        };
        history.push(record);
        localStorage.setItem('chatHistory', JSON.stringify(history));
        renderHistory();
    }

    function renderHistory() {
        historyDiv.innerHTML = '';
        history.forEach(h => {
            const item = document.createElement('div');
            item.className = 'history-item';
            item.innerText =
                `${h.time}\nSymptom: ${h.symptoms}\nDiagnosis: ${h.diagnosis}\nTreatment: ${h.treatment}`;
            historyDiv.appendChild(item);
        });
    }

    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;
        appendMessage('user', text);
        input.value = '';

        const diagnosis = await getDiagnosis(text);
        const treatment = ibnSinaTreatment(text);
        appendMessage('bot', diagnosis + "\n\n🧪 Ibn Sina's treatment:\n" + treatment);
        updateHistory(text, diagnosis, treatment);
    }

    function ibnSinaTreatment(symptoms) {
        const s = symptoms.toLowerCase();
        if (s.includes('fever')) return 'Barley water, rose water compress, avoid meat.';
        if (s.includes('cough')) return 'Licorice tea, honey with lemon, steam with chamomile.';
        if (s.includes('headache')) return 'Basil oil massage, rose water steam, rest in quiet.';
        if (s.includes('cold')) return 'Garlic with honey, warm soup, avoid cold air.';
        if (s.includes('stomach')) return 'Cumin with warm water, anise tea, light meals only.';
        return 'No traditional treatment found for this description.';
    }

    async function getDiagnosis(symptoms) {
        try {
            const response = await fetch('http://localhost:5000/diagnose', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ symptoms })
            });
            const data = await response.json();
            return data.diagnosis;
        } catch (e) {
            return 'Error contacting diagnosis server.';
        }
    }

    // Support Enter key to send
    input.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    renderHistory();
});
