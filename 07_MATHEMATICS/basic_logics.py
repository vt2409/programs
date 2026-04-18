
# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Time Conversion - Convert seconds into hours, minutes, and seconds
# Difficulty: Easy | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: MATHEMATICS & TIME CONVERSION                          ║
# ║  PURPOSE: Convert total seconds into hours, minutes, and seconds  ║
# ║  FEATURES: Modulo operations, integer division, time conversion   ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
Given a total number of seconds, convert it into hours, minutes, and seconds.

Example:
Input: 3696 seconds
Output: (1, 1, 36) - 1 hour, 1 minute, 36 seconds
"""

def convert_seconds(seconds):
    """
    Convert total seconds into hours, minutes, and remaining seconds.
    
    Args:
        seconds (int): Total number of seconds
        
    Returns:
        tuple: (hours, minutes, remaining_seconds)
    """
    hours = seconds // 3600
    rem_seconds = seconds % 3600
    minutes = rem_seconds // 60
    seconds = rem_seconds % 60
    return hours, minutes, seconds

print(f"Here's the output of converting seconds {convert_seconds(3600)}")

