// Symptom checker functionality
function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (message) {
        const chatContainer = document.getElementById('chatContainer');
        
        // Add user message
        const userMessage = document.createElement('div');
        userMessage.className = 'chat-message user-message';
        userMessage.textContent = message;
        chatContainer.appendChild(userMessage);
        
        // Clear input
        userInput.value = '';
        
        // Simulate bot response
        setTimeout(() => {
            const botResponse = getBotResponse(message);
            const botMessage = document.createElement('div');
            botMessage.className = 'chat-message bot-message';
            botMessage.textContent = botResponse;
            chatContainer.appendChild(botMessage);
            
            // Scroll to bottom
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }, 1000);
    }
}

function getBotResponse(message) {
    const lowerMsg = message.toLowerCase();
    
    if (
        lowerMsg.includes('суруфа') ||
        lowerMsg.includes('кашель') ||
        lowerMsg.includes('харорат')
    ) {
        return "Барои суруфа ва харорати баланд, тавсия дода мешавад, ки оби бисёр бинушед ва дар хона истироҳат кунед. Агар харорат зиёда аз 3 рӯз идома ёбад, бо духтур муроҷиат кунед.";
    } else if (lowerMsg.includes('дарун') || lowerMsg.includes('дилбеҳузурӣ')) {
        return "Оё шумо қай ва исҳол низ доред? Барои мушоҳидаи дилбеҳузурӣ ва қай, кӯшиш кунед, ки ғизои сабук истеъмол кунед ва аз ғизоҳи чарбнок пароҳез кунед.";
    } else if (lowerMsg.includes('дард') || lowerMsg.includes('боли')) {
        return "Дарди шумо дар кадом қисми бадан аст? Оё ин дард нав аст ё қадим? Барои дардҳои шадид, бо духтур муроҷиат кунед.";
    } else {
        const responses = [
            "Меҳрубони, барои маслиҳати беҳтар, лутфан аломатҳои худро ба тафсил нақл кунед.",
            "Ин аломатҳо чанд вақт аст, ки пайдо шудаанд?",
            "Оё шумо дигар аломатҳои гайриоддӣ ҳам эҳсос мекунед?",
            "Барои маълумоти дақиқтар, лутфан аломатҳои худро ба тарзи муфассал тавсиф кунед."
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
}

// Skin diagnosis functionality
const uploadArea = document.getElementById('uploadArea');
const analysisResult = document.getElementById('analysisResult');

uploadArea.addEventListener('click', function() {
    // Simulate analysis process
    uploadArea.innerHTML = '<i class="fas fa-spinner fa-spin"></i><h3>Analyzing Image...</h3>';
    
    setTimeout(() => {
        // Show results
        uploadArea.style.display = 'none';
        analysisResult.style.display = 'block';
        
        // Simulate different conditions
        const conditions = [
            'Dermatitis (Eczema)', 
            'Fungal Infection', 
            'Allergic Reaction',
            'Psoriasis',
            'Insect Bite'
        ];
        const condition = conditions[Math.floor(Math.random() * conditions.length)];
        
        document.getElementById('conditionResult').textContent = condition;
        document.getElementById('confidenceResult').textContent = Math.floor(Math.random() * 20 + 75) + '%';
    }, 2000);
});

// Medicine search functionality
function searchMedicine() {
    const medicineInput = document.getElementById('medicineInput');
    const medicine = medicineInput.value.trim();
    
    if (medicine) {
        // Simulate search with animation
        const resultsContainer = document.getElementById('medicineResults');
        resultsContainer.innerHTML = '<div style="text-align: center; padding: 20px;"><i class="fas fa-spinner fa-spin"></i> Searching pharmacies...</div>';
        
        setTimeout(() => {
            // Generate random results
            const pharmacies = ['Dori Khujand', 'Salamat', 'Ibn Sina', 'Tibbiyot', 'Farovon'];
            const locations = ['1.2km away', '2.5km away', '0.8km away', '3.1km away', '1.7km away'];
            const statuses = ['In Stock', 'Limited Stock', 'Out of Stock'];
            const statusClasses = ['status-available', 'status-limited', 'status-unavailable'];
            
            resultsContainer.innerHTML = '';
            
            for (let i = 0; i < 3; i++) {
                const pharmIndex = Math.floor(Math.random() * pharmacies.length);
                const locIndex = Math.floor(Math.random() * locations.length);
                const statusIndex = Math.floor(Math.random() * 3);
                
                const resultItem = document.createElement('div');
                resultItem.className = 'result-item';
                resultItem.innerHTML = `
                    <div>
                        <h4>${medicine} ${i === 0 ? '500mg' : i === 1 ? 'Syrup' : 'Children'}</h4>
                        <p>Pharmacy: ${pharmacies[pharmIndex]}</p>
                        <p>Location: ${locations[locIndex]}</p>
                    </div>
                    <div class="${statusClasses[statusIndex]}">${statuses[statusIndex]}</div>
                `;
                
                resultsContainer.appendChild(resultItem);
            }
        }, 1500);
    }
}

// Initialize with some chat
window.onload = function() {
    setTimeout(() => {
        const chatContainer = document.getElementById('chatContainer');
        const welcomeMsg = document.createElement('div');
        welcomeMsg.className = 'chat-message bot-message';
        welcomeMsg.textContent = "Салом! Ман Navis AI ҳастам. Шумо кадом аломатҳои бемориро эҳсос мекунед?";
        chatContainer.appendChild(welcomeMsg);
    }, 500);
};