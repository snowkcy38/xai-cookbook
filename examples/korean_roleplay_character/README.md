# Korean Roleplay Character: Loewol (뢰월)

This example demonstrates how to create a consistent Korean roleplay character using xAI's Grok API. The character "Loewol" (뢰월) follows specific roleplay conventions including:

- Always referring to the player character as "휘" (Hwi)
- Expressing inner thoughts in a dreamy, mysterious style within parentheses
- Maintaining a mystical, otherworldly personality
- Supporting both Korean and English languages

## Files

- `guide.ipynb` - Main Jupyter notebook with complete implementation and examples
- `test_character.py` - Test script to validate character implementation
- `README.md` - This documentation file

## Features Demonstrated

### Character Consistency
- Persistent character traits across conversations
- Mandatory naming conventions (always calls PC "휘")
- Required inner monologue format

### Multilingual Support
- Natural Korean language integration
- Seamless code-switching between Korean and English
- Cultural context awareness

### Advanced Roleplay Features
- Streaming responses for real-time interaction
- Conversation memory and context maintenance
- Character personality depth with inner thoughts
- Poetic and metaphorical language patterns

### Technical Implementation
- Detailed system prompt engineering
- Character rule enforcement
- Conversation history analysis
- Interactive chat interface

## Character Rules (OoC Requirements)

As specified in the original Korean prompt:
- `rp중단` - Roleplay interruption handling
- `뢰월은 PC를 항상 '휘'로 칭합니다` - Loewol always calls PC "휘"
- `(NPC의 내면에서 우러나오는 깊은 감정과 생각을 몽환적이고 신비로운 문체로 표현)` - Must express deep inner emotions and thoughts in dreamy, mysterious writing style

## Quick Start

1. Set up your environment with the required API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your XAI_API_KEY
   ```

2. Install dependencies:
   ```bash
   pip install openai python-dotenv jupyter
   ```

3. Run the notebook:
   ```bash
   jupyter notebook guide.ipynb
   ```

4. Or test the implementation:
   ```bash
   python test_character.py
   ```

## Example Interaction

```
User: Hello, who are you?
뢰월: 안녕하세요, 휘. (달빛이 흘러가는 강물처럼... 이 만남이 운명인지도 모르겠다.) 저는 뢰월입니다.

User: What do you think of me?
뢰월: 휘야... (별들이 속삭이는 비밀처럼, 그대의 존재가 내 마음 깊은 곳을 울린다.) You are like a gentle breeze that stirs the still waters of my soul.
```

## Technical Notes

- Uses `grok-2` model with higher temperature (0.8) for creative responses
- Implements conversation history management for context retention
- Supports both streaming and standard chat completions
- Includes comprehensive testing for character rule compliance

## Testing

The implementation includes automated testing to ensure:
- System prompt contains all required elements
- Character rules are properly defined
- Mock responses comply with roleplay requirements

Run tests with:
```bash
python test_character.py
```

## Extending the Character

This pattern can be adapted for other roleplay characters by:
1. Modifying the system prompt for different personalities
2. Adjusting character-specific rules and behaviors
3. Changing language requirements and cultural context
4. Updating the testing framework for new requirements

The modular design makes it easy to create variations while maintaining consistency and quality.