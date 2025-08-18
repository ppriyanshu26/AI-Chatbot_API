const functions = require("firebase-functions/v2");
const { OpenAI } = require("openai");

require("dotenv").config(); // Load local .env file for testing

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // Works locally & in Firebase
});

exports.chatbot = functions.https.onRequest(async (req, res) => {
  try {
    const userMessage = req.body.message;
    if (!userMessage) return res.status(400).json({ error: "No message provided" });

    const completion = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: userMessage }],
    });

    res.json({ reply: completion.choices[0].message.content });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
});
