from src.waifu2x_ncnn_py import Waifu2x

def waifu2x_upscale(input_path: str, output_path: str,
                    noise_level: int = 1, scale: int = 2,
                    gpu_id: int = 0, tta_mode: bool = False):
    """
    Perform waifu2x upscaling and noise reduction on an image.

    Parameters:
    - input_path: str - path to input image (png, jpg, etc.)
    - output_path: str - path to save the processed image
    - noise_level: int - noise reduction level (0-3)
    - scale: int - upscaling factor (1=no scale, 2=2x, etc.)
    - gpu_id: int - GPU device id to use (set -1 for CPU)
    - tta_mode: bool - whether to use test-time augmentation for better quality
    """
    waifu2x = Waifu2x(gpuid=gpu_id, tta_mode=tta_mode, noise=noise_level, scale=scale)
    waifu2x.process(input_path, output_path)
    print(f"Processed image saved to {output_path}")

if __name__ == "__main__":
    input_image = "input.png"    # Replace with your input image path
    output_image = "output.png"  # Output image path

    # Example: noise reduction level 2, 2x upscaling, GPU 0
    waifu2x_upscale(input_image, output_image, noise_level=2, scale=2, gpu_id=0, tta_mode=True)
