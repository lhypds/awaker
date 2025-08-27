#!/usr/bin/env python3
"""
Test script to check which keys are available with the keyboard library.
This helps determine the best key to use for the awaker script on different systems.
"""

import keyboard
import sys


def test_key_availability():
    """Test various keys to see which ones are available on this system."""
    
    print("Testing key availability with the keyboard library...\n")
    
    # Define categories of keys to test
    test_categories = {
        "Function Keys (Extended)": ["f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24"],
        "Lock Keys": ["caps lock", "num lock", "scroll lock", "scrolllock", "numlock", "capslock"],
        "Special Keys": ["pause", "break", "insert", "home", "end", "page up", "page down"],
        "Modifier Keys": ["shift", "ctrl", "alt", "cmd", "windows", "left shift", "right shift"],
        "Arrow Keys": ["up", "down", "left", "right"],
        "Common Alternatives": ["tab", "space", "backspace", "delete"]
    }
    
    available_keys = []
    unavailable_keys = []
    
    for category, keys in test_categories.items():
        print(f"=== {category} ===")
        category_available = []
        
        for key in keys:
            try:
                # Try to parse the key to see if it's recognized
                keyboard.parse_hotkey(key)
                print(f"✓ {key:<15} - available")
                available_keys.append(key)
                category_available.append(key)
            except Exception as e:
                print(f"✗ {key:<15} - not available")
                unavailable_keys.append(key)
        
        if category_available:
            print(f"  → Best options in this category: {', '.join(category_available[:3])}")
        print()
    
    return available_keys, unavailable_keys


def recommend_best_keys(available_keys):
    """Recommend the best keys for keeping computer awake."""
    
    # Priority order for awaker usage
    priority_keys = [
        ("f13", "Extended function key - ideal choice, rarely used by apps"),
        ("f14", "Extended function key - excellent alternative"),
        ("f15", "Extended function key - another good choice"),
        ("f16", "Extended function key - good backup option"),
        ("scroll lock", "Scroll lock - rarely used in modern apps"),
        ("scrolllock", "Scroll lock (alternative name)"),
        ("pause", "Pause key - seldom used"),
        ("insert", "Insert key - less commonly used"),
        ("num lock", "Num lock - might show indicator briefly"),
        ("numlock", "Num lock (alternative name)"),
        ("caps lock", "Caps lock - might show indicator briefly"),
        ("capslock", "Caps lock (alternative name)"),
        ("shift", "Shift key - works but might interfere with typing")
    ]
    
    print("=== RECOMMENDATIONS FOR AWAKER ===")
    print("Keys ranked from best to worst for keeping computer awake:\n")
    
    found_recommendations = []
    for key, description in priority_keys:
        if key in available_keys:
            rank = len(found_recommendations) + 1
            print(f"{rank}. {key:<15} - {description}")
            found_recommendations.append(key)
    
    if found_recommendations:
        print(f"\n🎯 BEST CHOICE: '{found_recommendations[0]}'")
        print(f"   Set KEY={found_recommendations[0]} in your .env file")
        
        if len(found_recommendations) > 1:
            print(f"\n📋 ALTERNATIVES: {', '.join(found_recommendations[1:3])}")
    else:
        print("⚠️  No ideal keys found. You may need to use a basic key like 'shift'")
    
    print(f"\nTotal available keys: {len(available_keys)}")
    print(f"Recommended keys available: {len(found_recommendations)}")


def main():
    """Main function to run the key availability test."""
    
    print("🔍 Keyboard Key Availability Tester")
    print("=" * 50)
    print("This script tests which keys are available for use with the awaker script.\n")
    
    try:
        available_keys, unavailable_keys = test_key_availability()
        recommend_best_keys(available_keys)
        
        print(f"\n📊 SUMMARY:")
        print(f"   Available keys: {len(available_keys)}")
        print(f"   Unavailable keys: {len(unavailable_keys)}")
        print(f"\n✅ Test completed successfully!")
        
    except ImportError:
        print("❌ Error: 'keyboard' library not found.")
        print("   Please install it with: pip install keyboard")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
