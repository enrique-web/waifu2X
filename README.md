# waifu2X

Waifu2x Image Upscaler

## Description

This project provides a tool to upscale and denoise images, especially anime-style artwork, using deep convolutional neural networks. It supports noise reduction, 2x upscaling, or both combined, enhancing image resolution while preserving details.

## Features

- Noise reduction with adjustable levels (0-3)
- 2x image upscaling
- Combined noise reduction and upscaling
- Supports anime-style art and photos
- Command-line usage for batch processing

## Installation

Clone the repository:

```
git clone https://github.com/enrique-web/waifu2X.git
cd waifu2X
```

*Note: This repository may be a wrapper or implementation based on the original waifu2x project.*

## Usage Examples (based on original waifu2x commands)

- Noise reduction only:

```
th waifu2x.lua -m noise -noise_level 1 -i input_image.png -o output_image.png
```

- 2x Upscaling only:

```
th waifu2x.lua -m scale -i input_image.png -o output_image.png
```

- Noise reduction + 2x Upscaling:

```
th waifu2x.lua -m noise_scale -noise_level 2 -i input_image.png -o output_image.png
```

## Notes

- Requires Torch environment for running `.lua` scripts.
- GPU acceleration supported via cuDNN.
- Adjust `-crop_size` option if you encounter GPU memory errors.

## References

- Original waifu2x repository: https://github.com/nagadomi/waifu2x
- Online demo: https://www.waifu2x.net/

## License

Please check the LICENSE file in the repository for licensing details.

---

