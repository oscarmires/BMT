# Clipping Modules

This directory contains the source code for the proposed modules: clipping and filtering.

## Use the Clipping Module
In order to use the clipping module, you must add the path to the repository to your interpreter. 
Then, import the module and create an instance. For example:

```python
import sys
sys.path.append('/home/my_user/BMT-Clipping/')

from clipping_modules.clipping import ClippingModule


# For fixed-time clipping
cm = ClippingModule(
    path_to_video_out=PATH_TO_OUTPUT_DIRECTORY, 
    window=120, 
    technique='fixed'
)

# For scene detection clipping
cm = ClippingModule(
    path_to_video_out=PATH_TO_OUTPUT_DIRECTORY, 
    technique='scene'
)

# Run
cm.get_clips(input_path=PATH_TO_VIDEO, name=VIDEO_NAME)
```

**Constructor parameters**
- `path_to_video_out`: this is the path to the directories where the clips will be stored (the directory must be created beforehand).
- `window`: size (in seconds) of the time window used for clipping. The default value is 30. Only necessary when the technique is 'fixed'.
- `technique`: the possible values are 'fixed' or 'scene'.

**Main function (`cm.get_clips`) parameters**
- `input_path`: path to the video you want to get clips from.
- `name`: name to be used as filename. The flip filenames will be generated in this format: _name@clip_id.mp4_.


##  Use the Filtering Module
Similarly, add the path to the repository to your interpreter (if you haven't already). 
Then, import the module and create an instance. For example:

```python
import sys
sys.path.append('/home/my_user/BMT-Clipping/')

from clipping_modules.filtering import FilteringModule


fm = FilteringModule()

# filter file
fm.filter_file(
    input_path=INPUT_PATH,
    output_path=OUTPUT_PATH,
)
```

**Main function (`fm.filter_file`) parameters**
- `input_path`: path to the JSON file containing BMT-generated captions.
- `output_path`: path to the JSON file where the filtered captions will be stored (the file must be created beforehand).

