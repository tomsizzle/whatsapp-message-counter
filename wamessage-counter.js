const fs = require('fs');

// Check if the filename was provided as an argument
if (process.argv.length < 3) {
    console.log("Please provide a .txt file as an argument.");
    process.exit(1);
}

// Get the filename from the command line arguments
const fileName = process.argv[2];

// Read the file
fs.readFile(fileName, 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        process.exit(1);
    }

    console.log("\nA warm welcome to the WhatsApp chat message counter.");
    console.log("This app processes a .txt file of WhatsApp chat history and counts the messages for each participant.\n");

    // Regular expression to match the WhatsApp message pattern
    const messagePattern = /^\[\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2}:\d{2}\] (.*?):/;
    
    let messages = 0;
    let indMes = {};

    // Split file content into lines and process each line
    const lines = data.split('\n');
    lines.forEach(line => {
        const match = messagePattern.exec(line);
        if (match) {
            const participant = match[1].trim();  // Extract participant's name
            indMes[participant] = (indMes[participant] || 0) + 1;
            messages += 1;
        }
    });

    // Output the results
    console.log(`There are ${messages} messages in the chat history.`);
    for (const participant in indMes) {
        console.log(`${participant} sent ${indMes[participant]} messages.`);
    }
});
