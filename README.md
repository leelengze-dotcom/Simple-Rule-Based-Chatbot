# Simple Rule-Based Chatbot

A beginner-friendly Python chatbot that responds to simple user messages using a predefined dictionary of questions and answers.

## Features

- Responds to greetings such as `hi` and `hello`
- Answers simple questions
- Removes spaces and ignores uppercase or lowercase differences
- Supports exit commands such as `bye`, `quit`, and `exit`
- Displays a default message when it does not understand the input

## Requirements

- Python 3.x

No additional Python libraries are required.

## How to Run

1. Download or clone this project.

2. Open the project folder in Visual Studio Code.

3. Open the terminal in Visual Studio Code:

   ```bash
   Terminal > New Terminal
   ```

4. Run the Python file:

   ```bash
   python3 "print('Hello World').py"
   ```

   On Windows, you may need to use:

   ```bash
   python "print('Hello World').py"
   ```

## Example

```text
Bot 1: How Can I Help You Today?
You: hello
Bot 1: Hello! How can I help you?

You: what is your name
Bot 1: My name is Bot 1

You: bye
Bot: bye
```

## Supported Messages

The chatbot currently understands messages such as:

- `hi`
- `hello`
- `how are you`
- `what is your name`
- `what can you do`
- `help`
- `good morning`
- `good afternoon`
- `thank you`
- `thanks`
- `bye`
- `goodbye`

Spaces are automatically removed, so both `how are you` and `howareyou` will work.

## How It Works

The chatbot stores its responses inside a Python dictionary:

```python
responses = {
    "hi": "Hi there! How can I help you?",
    "hello": "Hello! How can I help you?"
}
```

The user's message is cleaned using:

```python
message = input("You: ").replace(" ", "").lower()
```

This removes spaces and converts the message to lowercase.

The chatbot then searches for the message in the dictionary:

```python
reply = responses.get(message, "Sorry, I don't understand that.")
```

## Possible Improvements

Future improvements could include:

- Adding more questions and responses
- Accepting punctuation such as question marks
- Creating a graphical user interface
- Saving conversation history
- Using artificial intelligence or natural language processing
- Organising the code into functions

## Author

Leng Ze
