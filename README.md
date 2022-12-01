# Extended Dense Video Captions Using Input Clipping in a Bi-Modal Transformer

[📄 Technical report](https://drive.google.com/file/d/1btVbFxP3_STBjPK563ynwNvZGgYmFZ0z/view?usp=share_link) · [📼 Video](https://drive.google.com/file/d/10JeLN7vhVgpjK5jFDPSA-CDMJqK8D5lT/view?usp=share_link) · [🧑‍🏫 Presentation](https://drive.google.com/file/d/1rc8oiVQbWr1Y5EwraDYdOWUKfRykKg9j/view?usp=share_link)

Repository used for experimentation over the [BMT Model by Iashin & Rahtu (2020)](https://iashin.ai/bmt).
This repository is a fork from [BMT](https://github.com/v-iashin/BMT).

## General info and structure

We maintain the structure from [BMT](https://github.com/v-iashin/BMT). 

All files created by us are located in the [clipping_experiments](https://github.com/oscarmires/BMT-Clipping/tree/master/clipping_experiments) and the [clipping_modules](https://github.com/oscarmires/BMT-Clipping/tree/master/clipping_modules) directory. Refer to each directory's readme file to know more about the execution of the experiments and the modules. We also made changes to the file [sample/single_video_prediction.py](https://github.com/oscarmires/BMT-Clipping/blob/master/sample/single_video_prediction.py)

The original Readme file from BMT is found as [Prev_README.md](https://github.com/oscarmires/BMT-Clipping/blob/master/Prev_README.md).


## Cloning the repository

Mind the `--recursive` flag to make sure `submodules` are also cloned (evaluation scripts for Python 3 and scripts for feature extraction).
```bash
git clone --recursive https://github.com/oscarmires/BMT-Clipping.git
```
