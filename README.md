# Image_Processing_Toolkit
 Beyond basic libraries: Building an Image Processing Toolkit from scratch using Python & NumPy!

I recently wanted to dive deeper into how images are actually treated under the hood in programming—not just using high-level black-box filters, but manipulating the pixel matrices directly.

To do this, I built a terminal-based Image Processing Toolkit from scratch! Using PIL (Pillow) for image loading/saving and NumPy for data manipulation, the script allows users to interactively apply adjustments through a clean CLI menu.

Key Features implemented:

 Brightness Adjustment: Using matrix addition and np.clip to prevent color clipping overflows (handling uint8 constraints).

Horizontal & Vertical Flips: Leveraging matrix slicing ([::-1]) for efficient axis inversions.

Grayscale & Inversion (Negative): Implementing dot product calculations to apply custom luminosity weightings [0.2989, 0.5870, 0.1140] for an accurate grayscale conversion.

 State Tracking: Built-in safeguards allowing users to preview changes before deciding to overwrite or discard them, with a quick reset to the original file state.

This project reinforced my understanding of working with multi-dimensional arrays, handling edge cases (like file-not-found and invalid user inputs), and structuring interactive command-line loops.



