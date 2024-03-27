import os


def html():
    # Replace this with your WebSocket URL
    ws_url = f"ws://{os.getenv('API_HOST')}/chat/sync"

    # Your HTML content
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Chat</title>
            <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body class="bg-gray-100 min-h-screen flex items-center justify-center">
        
            <div class="w-full max-w-md p-4 bg-white rounded shadow-md grid gap-4">
        
                <h1 class="text-2xl font-bold mb-4">WebSocket Chat</h1>
        
                <form action="" onsubmit="sendMessage(event)" class="grid grid-cols-2 gap-4">
                    <input type="text" id="messageText" autocomplete="off" class="border p-2 col-span-1">
                    <button class="bg-blue-500 text-white px-4 py-2 rounded col-span-1">Send</button>
                </form>
        
                <ul id="messages" class="list-disc pl-4">
                </ul>
        
                <script>
                    var ws = new WebSocket("{ws_url}");
                    ws.onmessage = function(event) {{
                        var messages = document.getElementById('messages')
                        var message = document.createElement('li')
                        var content = document.createTextNode(event.data)
                        message.appendChild(content)
                        messages.appendChild(message)
                    }};
                    function sendMessage(event) {{
                        var input = document.getElementById("messageText")
                        ws.send(input.value)
                        input.value = ''
                        event.preventDefault()
                    }}
                </script>
        
            </div>
        
        </body>
        </html>
        """

    # Return the HTML content with the appropriate response class
    return html_content
