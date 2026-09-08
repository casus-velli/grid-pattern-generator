import numpy as np
import matplotlib.pyplot as plt
import os

def generate_pattern_grid(size=10, output_path="pattern.png"):
    grid = np.random.choice([0, 1, 2], size=(size, size), p=[0.5, 0.3, 0.2])
    
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap='Pastel1')
    plt.axis('off')
    plt.title("Algorithmic Grid Pattern", fontsize=12, pad=10)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True) if os.path.dirname(output_path) else None
    plt.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close()
    print(f"Generated pattern saved successfully to {output_path}")

def main():
    print("Starting Grid Pattern Generator...")
    generate_pattern_grid(size=12, output_path="./output/generated_pattern.png")

if __name__ == "__main__":
    main()
