# Eliza Psychotherapist Chatbot

## Description
This repository contains the implementation of a simple psychotherapist chatbot named Eliza, created as a programming assignment for CMSC 416. The chatbot engages in dialogue with the user, responding based on key words in the input and transforming statements into questions. The goal is to simulate a conversation with a psychotherapist.

## Features
- Greet user and ask for their name.
- Recognize expressions of emotion (e.g., "I feel") and inquire about the duration.
- Identify and respond to statements with "because," exploring the reasons behind the user's feelings.
- Interpret desires expressed with "I want to" and inquire about the motivations.
- Transform statements into questions using predefined responses for a more interactive experience.
- Support for a session-ending command.

## Examples
[eliza] Hi, I'm a psychotherapist. What is your name?
[user] My name is Aang.
[eliza] Hi Aang. How can I help you today?
[Aang] I feel sad and I don't know why.
[eliza] Well Aang, how long have you been feeling sad?



## How to Use
To start the chatbot, run the following command in the terminal:
```bash
python eliza.py
```
Follow the prompts and engage in a conversation with Eliza.

Implementation
The program uses a rule-based approach, employing regular expressions and predefined responses to simulate speech. It begins by obtaining the user's name, setting up response cycles, and tracking the session status. Eliza then greets the user, processes input based on identified patterns, and cycles through responses. After completing one cycle, the session ends when the user issues an exit command.

Author
Tahshon Holmes
Date: 02/05/2024
