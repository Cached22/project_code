document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    // Function to append message to chat box
    function appendMessage(user, text) {
        const messageElement = document.createElement('div');
        messageElement.classList.add(user === 'user' ? 'user-message' : 'ai-message');
        messageElement.innerText = text;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto scroll to the latest message
    }

    // Send message to OpenAI and append to chat
    async function sendMessageToOpenAI(message) {
        try {
            const response = await fetch('/api/openai', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });
            const data = await response.json();
            if (data.success) {
                appendMessage('ai', data.reply);
            } else {
                appendMessage('ai', 'Sorry, I am unable to respond at the moment.');
            }
        } catch (error) {
            console.error('Error while sending message to OpenAI:', error);
            appendMessage('ai', 'Error while communicating with the AI.');
        }
    }

    // Event listener for send button
    sendButton.addEventListener('click', function(event) {
        event.preventDefault();
        const message = messageInput.value.trim();
        if (message) {
            appendMessage('user', message);
            sendMessageToOpenAI(message);
            messageInput.value = ''; // Clear the input after sending
        }
    });

    // Event listener for form submit
    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        sendButton.click();
    });
});