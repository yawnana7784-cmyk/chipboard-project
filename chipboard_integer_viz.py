def draw_chips(number, label=""):
    if number >= 0:
        chips = "⚫ " * number  # Black = positive
        print(f"{label} +{number}: {chips}")
    else:
        chips = "🔴 " * abs(number)  # Red = negative  
        print(f"{label} {number}: {chips}")
    return number

def add_integers(a, b):
    print(f"\n=== Solving {a} + {b} ===")
    draw_chips(a, "First")
    draw_chips(b, "Second")
    
    result = a + b
    if a >= 0 and b < 0:
        cancelled = min(a, abs(b))
        print(f"Cancel {cancelled} zero pairs: ⚫🔴")
    
    draw_chips(result, "Result")
    print(f"Answer: {a} + {b} = {result}")
    print("-" * 30)

if __name__ == "__main__":
    print("Chipboard Integer Visualizer")
    print("From BSc Thesis: Using Chipboard Models to Teach Integers")
    print("Black ⚫ = +1, Red 🔴 = -1\n")
    
    add_integers(5, -3)
    add_integers(2, -7)
    
    print("\nRun successful. Ready for GitHub.")