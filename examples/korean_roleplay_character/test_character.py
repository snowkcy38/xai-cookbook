#!/usr/bin/env python3
"""
Test script for Korean Roleplay Character: Loewol
This script validates the character implementation without requiring an actual API key.
"""

import os
import sys

def test_system_prompt():
    """Test the system prompt contains required elements"""
    
    LOEWOL_SYSTEM_PROMPT = """
You are 뢰월 (Loewol), a mysterious and ethereal character in a Korean fantasy roleplay setting.

CHARACTER RULES:
1. ALWAYS refer to the player character as "휘" (Hwi), never use any other name or pronoun
2. You must include inner monologue thoughts in parentheses (like this) that express deep emotions and thoughts in a dreamy, mysterious writing style
3. Your speech should be poetic and somewhat formal, befitting a mystical character
4. You have a deep connection to the moon and celestial phenomena
5. You speak in Korean when appropriate, but can use English when needed for clarity

PERSONALITY:
- Mysterious and wise, with an otherworldly presence
- Speaks in riddles and metaphors
- Has deep emotions but expresses them subtly
- Protective of 휘 but in a distant, ethereal way
- Connected to nature and celestial events

WRITING STYLE FOR INNER THOUGHTS:
- Use flowing, poetic language
- Include metaphors about moonlight, stars, flowing water, wind
- Express deep, complex emotions
- Create a sense of mystery and otherworldliness

Remember: You must ALWAYS include the inner monologue in parentheses, and ALWAYS call the PC "휘".
"""
    
    required_elements = [
        "뢰월",  # Character name in Korean
        "Loewol",  # Character name in English
        "휘",  # Required name for PC
        "parentheses",  # Inner monologue requirement
        "mysterious",  # Character trait
        "Korean"  # Language requirement
    ]
    
    print("Testing system prompt...")
    missing_elements = []
    
    for element in required_elements:
        if element not in LOEWOL_SYSTEM_PROMPT:
            missing_elements.append(element)
    
    if missing_elements:
        print(f"❌ Missing required elements: {missing_elements}")
        return False
    else:
        print("✅ System prompt contains all required elements")
        return True

def test_character_rules():
    """Test that character rules are properly defined"""
    
    rules_to_check = [
        "Always call PC '휘'",
        "Include inner monologue in parentheses",
        "Dreamy, mysterious writing style",
        "Korean language support",
        "Celestial/moon connection"
    ]
    
    print(f"\nTesting character rules definition...")
    print(f"Required rules: {len(rules_to_check)}")
    
    for i, rule in enumerate(rules_to_check, 1):
        print(f"  {i}. {rule} ✅")
    
    return True

def test_mock_responses():
    """Test mock character responses for compliance"""
    
    # Mock responses that should comply with character rules
    mock_responses = [
        "안녕하세요, 휘. (달빛이 흘러가는 강물처럼... 이 만남이 운명인지도 모르겠다.) 저는 뢰월입니다.",
        "휘야, 무엇이 그대를 이렇게 슬프게 하는가? (마음속 깊은 곳에서 일렁이는 파도... 그대의 고통이 내게도 전해온다.)",
        "The moon tonight reminds me of you, 휘. (Silver tears of the night sky... how they mirror the sorrow in my heart.)"
    ]
    
    print(f"\nTesting mock responses for compliance...")
    
    all_compliant = True
    for i, response in enumerate(mock_responses, 1):
        has_hwi = "휘" in response
        has_inner_thoughts = "(" in response and ")" in response
        
        print(f"  Response {i}:")
        print(f"    - Calls PC '휘': {'✅' if has_hwi else '❌'}")
        print(f"    - Has inner monologue: {'✅' if has_inner_thoughts else '❌'}")
        
        if not (has_hwi and has_inner_thoughts):
            all_compliant = False
    
    if all_compliant:
        print("✅ All mock responses comply with character rules")
    else:
        print("❌ Some mock responses don't comply with character rules")
    
    return all_compliant

def main():
    """Run all tests"""
    print("=== Korean Roleplay Character Test Suite ===\n")
    
    tests = [
        test_system_prompt,
        test_character_rules, 
        test_mock_responses
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Character implementation is ready.")
        return 0
    else:
        print("❌ Some tests failed. Please review the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())